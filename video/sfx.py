"""Tự tổng hợp âm thanh phụ (không bản quyền): click chuột, gõ phím, whoosh, bling, tinh.
Và hàm trộn vào tiếng nói: python3 sfx.py <thư mục chứa joined.mov + events.json> <video_noaudio> <out.mp4>"""
import sys, json, subprocess, numpy as np, imageio_ffmpeg

SR = 48000
rng = np.random.default_rng(7)
FF = imageio_ffmpeg.get_ffmpeg_exe()

def env(n, attack, decay):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(attack, 1e-4)) * np.exp(-t / decay)

def onepole_hp(x, a=0.85):
    y = np.zeros_like(x); p = 0.0; px = 0.0
    for i, v in enumerate(x):
        p = a * (p + v - px); px = v; y[i] = p
    return y

def click(pitch=1.0):
    """tiếng click chuột: tách giòn + thân ngắn"""
    n = int(0.05 * SR); t = np.arange(n) / SR
    tick = onepole_hp(rng.standard_normal(n)) * env(n, 0.0003, 0.004)
    body = np.sin(2 * np.pi * 1900 * pitch * t) * env(n, 0.0005, 0.009) * 0.6
    body2 = np.sin(2 * np.pi * 3400 * pitch * t) * env(n, 0.0005, 0.005) * 0.3
    x = tick + body + body2
    return x / np.abs(x).max()

def keys(count=5, gap=(0.075, 0.12)):
    """gõ bàn phím: chuỗi click trầm hơn, lệch nhịp tự nhiên"""
    parts, total = [], 0.0
    for i in range(count):
        c = click(pitch=0.55 + 0.12 * rng.random()) * (0.7 + 0.3 * rng.random())
        parts.append((total, c)); total += rng.uniform(*gap)
    out = np.zeros(int((total + 0.06) * SR))
    for st, c in parts:
        i = int(st * SR); out[i:i + len(c)] += c
    return out / np.abs(out).max()

def bell(freq, dur=0.9, decay=0.28):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * freq * r * t) * np.exp(-t / (decay / (1 + 0.6 * k)))
            for k, (r, a) in enumerate([(1, 1), (2.0, .35), (3.01, .18), (4.2, .08)]))
    return x * np.minimum(1, t / 0.003)

def ding():
    """tiếng 'tinh' trong trẻo"""
    x = bell(1760, 1.0, 0.35)
    return x / np.abs(x).max()

def bling():
    """bling lấp lánh: 3 nốt chuông lướt lên + ánh kim"""
    out = np.zeros(int(1.0 * SR))
    for k, f in enumerate([1318.5, 1760, 2637]):
        b = bell(f, 0.8, 0.22) * (0.9 - 0.15 * k); i = int(k * 0.055 * SR)
        out[i:i + len(b)] += b[:len(out) - i]
    n = len(out); t = np.arange(n) / SR
    shimmer = onepole_hp(rng.standard_normal(n), 0.97) * np.exp(-t / 0.18) * 0.06
    out += shimmer * np.sin(2 * np.pi * 9 * t) ** 2
    return out / np.abs(out).max()

def whoosh(dur=0.38):
    """vút gió: nhiễu lọc thông dải quét lên rồi xuống"""
    n = int(dur * SR); t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    y = np.zeros(n); lp = 0.0; bp = 0.0
    for i in range(n):
        p = i / n
        fc = 300 + 3200 * np.sin(np.pi * p) ** 1.5
        g = 2 * np.sin(np.pi * fc / SR)
        hp = noise[i] - lp - 0.9 * bp
        bp += g * hp; lp += g * bp
        y[i] = bp
    y *= np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 2
    return y / np.abs(y).max()

BANK = {"click": (click(), 0.16), "keys2": (keys(3), 0.13), "keys": (keys(6), 0.14),
        "ding": (ding(), 0.13), "bling": (bling(), 0.16), "whoosh": (whoosh(), 0.20)}

if __name__ == "__main__":
    d, vid, out = sys.argv[1], sys.argv[2], sys.argv[3]
    # tiếng nói: chuẩn hóa -14 LUFS trước, rồi trộn âm phụ theo mức cố định
    raw = subprocess.run([FF, "-loglevel", "error", "-i", f"{d}/joined.mov", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                          "-ar", str(SR), "-ac", "2", "-f", "f32le", "-"], capture_output=True).stdout
    voice = np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
    for name, t in json.load(open(f"{d}/events.json")):
        x, g = BANK[name]
        i = max(0, int(t * SR)); j = min(len(voice), i + len(x))
        voice[i:j] += (x[:j - i] * g)[:, None]
    mixed = np.clip(voice, -0.98, 0.98).astype(np.float32)
    subprocess.run([FF, "-loglevel", "error", "-y", "-i", vid, "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "alimiter=limit=0.95",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out],
                   input=mixed.tobytes(), check=True)
    print("ok", out)
