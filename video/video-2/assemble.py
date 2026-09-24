"""Ghép 3 đoạn quay liền mạch, cắt khoảng lặng (jump-cut như mẫu), chỉnh tốc độ nhẹ để về ~30s."""
import re, subprocess, json, imageio_ffmpeg

D = __import__("os").environ.get("WORKDIR", ".")
FF = imageio_ffmpeg.get_ffmpeg_exe()
TARGET, PAD, MIN_GAP = 20.0, 0.12, 0.34
# (file, bắt đầu, kết thúc) — điểm nối lấy từ tương quan âm thanh (3 file là 1 lần quay cắt ra)
CLIPS = [("v2/p1.mov", 0.85, 10.843), ("v2/p2.mov", 0.0, 7.95)]
HOLD = (1, 7.95, 8.70)  # giữ khoảnh khắc cười sau CTA, trước khi tay với tắt máy
FREEZE = 1.5  # dừng hình cuối làm khung kết

def silences(path):
    err = subprocess.run([FF, "-i", path, "-af", "silencedetect=n=-32dB:d=0.18", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    return list(zip(st, en))

segs = []  # (input index, start, end)
for i, (f, a, b) in enumerate(CLIPS):
    cur = a
    for s, e in silences(f"{D}/{f}"):
        if e - s < MIN_GAP or e <= a or s >= b:
            continue
        cut_a, cut_b = max(s + PAD, a), min(e - PAD, b)
        if cut_a > cur + 0.05:
            segs.append((i, cur, cut_a))
        cur = max(cur, cut_b)
    if b > cur + 0.05:
        segs.append((i, cur, b))

segs.append(HOLD)
total = sum(e - s for _, s, e in segs)
speed = min(max(1.0, total / TARGET), 1.12)
print(f"{len(segs)} đoạn, tổng {total:.2f}s + dừng hình {FREEZE}s -> {total / speed + FREEZE:.2f}s")

parts, labels = [], []
for k, (i, s, e) in enumerate(segs):
    d = e - s
    parts.append(f"[{i}:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS,fps=30,scale=1080:1920[v{k}]")
    parts.append(f"[{i}:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,"
                 f"afade=t=in:d=0.015,afade=t=out:st={d - 0.02:.3f}:d=0.02[a{k}]")
    labels.append(f"[v{k}][a{k}]")
parts.append("".join(labels) + f"concat=n={len(segs)}:v=1:a=1[vc][ac]")
parts.append(f"[vc]setpts=PTS/{speed:.4f},fps=30,tpad=stop_mode=clone:stop_duration={FREEZE}[vo]")
parts.append(f"[ac]atempo={speed:.4f},apad=pad_dur={FREEZE}[ao]")
cmd = [FF, "-loglevel", "error", "-y"]
for f, _, _ in CLIPS:
    cmd += ["-i", f"{D}/{f}"]
cmd += ["-filter_complex", ";".join(parts), "-map", "[vo]", "-map", "[ao]",
        "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le",
        f"{D}/v2/joined.mov"]
subprocess.run(cmd, check=True)

# thời điểm các vết cắt trên timeline đầu ra (để đổi mức zoom đúng vết cắt, che jump-cut)
cuts, t = [], 0.0
for _, s, e in segs[:-1]:
    t += (e - s) / speed
    cuts.append(round(t, 3))
json.dump(cuts, open(f"{D}/v2/cuts.json", "w"))
print("cuts", cuts)
