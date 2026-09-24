"""Ghép đoạn quay MƯỢT: cắt khoảng lặng, hòa âm (acrossfade) + hòa hình (xfade) ở mỗi vết cắt.
Xuất: <out>/joined.mov, cuts.json (thời điểm vết cắt), remap.json (đổi mốc thời gian bản cũ -> bản mới).
Dùng: python3 pipeline.py v1|v2"""
import re, sys, json, subprocess, numpy as np, imageio_ffmpeg

D = __import__("os").environ.get("WORKDIR", ".")
FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS, XF, MIN_SEG = 30, 0.10, 0.30  # XF: độ dài hòa âm/hình ở mỗi vết cắt (giây, thời gian gốc)

CFG = {
    "v1": dict(out="", clips=[("src.mov", 0.45, 9.32), ("b.mov", 0.0, 14.0), ("c.mov", 0.0, 13.15)],
               pad=0.09, gap=0.22, target=29.9, hold=None, freeze=0.0, join=[9.3209, 14.0016]),
    "v2": dict(out="v2/", clips=[("v2/p1.mov", 0.85, 10.843), ("v2/p2.mov", 0.0, 7.95)],
               pad=0.12, gap=0.34, target=20.0, hold=(1, 7.95, 8.70), freeze=2.0, join=[10.843]),
}
C = CFG[sys.argv[1]]

def silences(path):
    err = subprocess.run([FF, "-i", path, "-af", "silencedetect=n=-32dB:d=0.18", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return list(zip([float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)],
                    [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]))

def build_segs():
    segs = []
    for i, (f, a, b) in enumerate(C["clips"]):
        cur = a
        for s, e in silences(f"{D}/{f}"):
            if e - s < C["gap"] or e <= a or s >= b:
                continue
            ca, cb = max(s + C["pad"], a), min(e - C["pad"], b)
            if ca > cur + 0.05:
                segs.append((i, cur, ca))
            cur = max(cur, cb)
        if b > cur + 0.05:
            segs.append((i, cur, b))
    if C["hold"]:
        segs.append(C["hold"])
    return segs

old = build_segs()

# ---- bản gốc liên tục: nối các file tại điểm trùng âm thanh (không hòa, không mất chữ) ----
MASTER = f"{D}/{C['out']}master.mov"
mp_parts, labs = [], []
ends = C["join"] + [None]
for i, (f, a, b) in enumerate(C["clips"]):
    e = ends[i]
    tv = f"trim=0:{e}," if e else ""
    ta = f"atrim=0:{e}," if e else ""
    mp_parts.append(f"[{i}:v]{tv}setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920[mv{i}]")
    mp_parts.append(f"[{i}:a]{ta}asetpts=PTS-STARTPTS,aresample=48000[ma{i}]")
    labs.append(f"[mv{i}][ma{i}]")
mp_parts.append("".join(labs) + f"concat=n={len(labs)}:v=1:a=1[mv][ma]")
cmd = [FF, "-loglevel", "error", "-y"]
for f, _, _ in C["clips"]:
    cmd += ["-i", f"{D}/{f}"]
subprocess.run(cmd + ["-filter_complex", ";".join(mp_parts), "-map", "[mv]", "-map", "[ma]", "-c:v", "libx264",
                      "-crf", "10", "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", MASTER], check=True)
OFF = [sum(C["join"][:i]) for i in range(len(C["clips"]))]  # vị trí đầu mỗi file trong bản gốc
m_a = OFF[0] + C["clips"][0][1]
m_b = OFF[-1] + C["clips"][-1][2]  # đúng như bản đã dựng trước (dùng để đổi mốc phụ đề/hiệu ứng)
old_total = sum(e - s for _, s, e in old)
old_speed = min(max(1.0, old_total / (C["target"] - C["freeze"] if C["freeze"] else C["target"])), 1.12) \
    if not C["hold"] else 1.0

# bản mới: cắt khoảng lặng trên bản gốc liên tục; đoạn quá ngắn thì giữ luôn khoảng lặng kề (không cắt)
new, cur = [], m_a
for s_, e_ in silences(MASTER):
    if e_ - s_ < C["gap"] or e_ <= m_a or s_ >= m_b:
        continue
    ca, cb = max(s_ + C["pad"], m_a), min(e_ - C["pad"], m_b)
    if ca - cur >= MIN_SEG:
        new.append((0, cur, ca))
        cur = max(cur, cb)
if m_b > cur + 0.05:
    new.append((0, cur, m_b))
if C["hold"]:
    hi, hs, he = C["hold"]
    new.append((0, OFF[hi] + hs, OFF[hi] + he))
new = [(0, round(a_ * FPS) / FPS, round(b_ * FPS) / FPS) for _, a_, b_ in new]
n = len(new)
new_total = sum(e - s for _, s, e in new) - XF * (n - 1)
speed = min(max(1.0, new_total / (C["target"] - C["freeze"])), 1.12)
print(f"{n} đoạn, {n - 1} vết cắt hòa {XF}s, tốc độ x{speed:.3f} -> {new_total / speed + C['freeze']:.2f}s")

# ---- filter: xfade hình + acrossfade tiếng nối tiếp ----
parts = []
for k, (i, s, e) in enumerate(new):
    parts.append(f"[{i}:v]trim={s:.4f}:{e:.4f},setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920,settb=1/{FPS}[v{k}]")
    parts.append(f"[{i}:a]atrim={s:.4f}:{e:.4f},asetpts=PTS-STARTPTS,aresample=48000[a{k}]")
vlab, alab, acc = "v0", "a0", new[0][2] - new[0][1]
starts = [0.0]  # thời điểm (gốc, sau nối) mỗi đoạn bắt đầu
for k in range(1, n):
    off = acc - XF
    starts.append(off)
    parts.append(f"[{vlab}][v{k}]xfade=transition=fade:duration={XF}:offset={off:.4f}[vx{k}]")
    parts.append(f"[{alab}][a{k}]acrossfade=d={XF}:c1=qsin:c2=qsin[ax{k}]")
    vlab, alab = f"vx{k}", f"ax{k}"
    acc = off + (new[k][2] - new[k][1])
tp = f",tpad=stop_mode=clone:stop_duration={C['freeze']}" if C["freeze"] else ""
ap = f",apad=pad_dur={C['freeze']}" if C["freeze"] else ""
parts.append(f"[{vlab}]setpts=PTS/{speed:.5f},fps={FPS}{tp}[vo]")
parts.append(f"[{alab}]atempo={speed:.5f}{ap}[ao]")
cmd = [FF, "-loglevel", "error", "-y", "-i", MASTER]
cmd += ["-filter_complex", ";".join(parts), "-map", "[vo]", "-map", "[ao]", "-c:v", "libx264", "-crf", "12",
        "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", f"{D}/{C['out']}joined.mov"]
subprocess.run(cmd, check=True)

cuts = [round((st + XF / 2) / speed, 3) for st in starts[1:]]  # giữa mỗi lần hòa
json.dump(cuts, open(f"{D}/{C['out']}cuts.json", "w"))

# ---- đổi mốc: t (bản cũ, giây) -> t (bản mới) qua thời gian trong file gốc ----
def old_to_src(t):
    u, acc = t * old_speed, 0.0
    for i, s, e in old:
        if u <= acc + (e - s):
            return i, s + (u - acc)
        acc += e - s
    i, s, e = old[-1]
    return i, e + (u - acc)  # phần dừng hình cuối

def src_to_new(i, x):
    i, x = 0, OFF[i] + x
    best = None
    for k, (j, s, e) in enumerate(new):
        if j != i:
            continue
        if s <= x <= e:
            return (starts[k] + (x - s)) / speed
        d = min(abs(x - s), abs(x - e))
        if best is None or d < best[0]:
            best = (d, (starts[k] + (min(max(x, s), e) - s)) / speed)
    return best[1]

old_end = old_total / old_speed
grid = np.arange(0, old_end + C["freeze"] + 0.6, 0.01)
new_end = new_total / speed
m = []
for t in grid:
    if t <= old_end:
        m.append(src_to_new(*old_to_src(t)))
    else:
        m.append(new_end + (t - old_end))
m = np.maximum.accumulate(np.array(m))  # bảo đảm tăng dần
json.dump({"old": grid.round(3).tolist(), "new": m.round(3).tolist()}, open(f"{D}/{C['out']}remap.json", "w"))
print("cuts", cuts)
