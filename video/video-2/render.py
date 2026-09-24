"""Dựng lại video theo mẫu Hoa Tara: nền mờ, tông ấm, zoom nhịp, phụ đề cụm + từ khóa cyan, 3 hiệu ứng nhấn."""
import subprocess, numpy as np, cv2, imageio_ffmpeg, mediapipe as mp
from PIL import Image, ImageDraw, ImageFont

D = __import__("os").environ.get("WORKDIR", ".")
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
SRC, OUT = f"{D}/v2/joined.mov", f"{D}/v2/out_noaudio.mp4"
import json
_R = json.load(open(f"{D}/v2/remap.json"))
RM = lambda t: float(np.interp(t, _R["old"], _R["new"]))
CUTS = sorted(json.load(open(f"{D}/v2/cuts.json")) + [RM(5.28), RM(15.86)])  # thêm điểm đổi zoom ở đoạn dài không có vết cắt
END_CARD = RM(17.19)  # hết lời nói -> khung kết

# ---------- Phụ đề: (bắt đầu, kết thúc, [dòng...]) ; *từ* = tô cyan ----------
SUBS = [
    (0.00, 1.12, ["ĐỪNG *XIN*", "PHÉP NGƯỜI KHÁC"]),
    (1.12, 2.02, ["ĐỂ *SỐNG*", "CUỘC ĐỜI"]),
    (2.02, 2.40, ["CỦA *MÌNH*"]),
    (2.40, 3.78, ["NGƯỜI *GÓP* *Ý*", "NHIỀU NHẤT"]),
    (3.78, 5.28, ["CHƯA CHẮC CHỊU", "*TRÁCH* *NHIỆM* CHO BẠN"]),
    (5.28, 6.66, ["HỌ *KHÔNG*", "TRẢ HÓA ĐƠN"]),
    (6.66, 8.00, ["CŨNG KHÔNG CHỊU", "*HẬU* *QUẢ* THAY BẠN"]),
    (8.00, 9.32, ["*VẬY* *SAO*", "MÌNH CỨ"]),
    (9.32, 10.44, ["SỢ HỌ KHÔNG", "*HÀI* *LÒNG*"]),
    (10.44, 11.48, ["NGHE THÌ", "*ĐƯỢC* NHƯNG"]),
    (11.48, 12.76, ["QUYẾT ĐỊNH THÌ", "PHẢI LÀ *BẠN*"]),
    (12.76, 13.90, ["CUỘC ĐỜI", "CỦA *MÌNH*"]),
    (13.90, 14.90, ["MÌNH CHỊU", "*TRÁCH* *NHIỆM*"]),
    (14.90, 15.86, ["BẠN *NGHĨ*", "SAO?"]),
    (15.86, 17.19, ["BÌNH LUẬN CHO", "*GIÀU* BIẾT NHÉ"]),
]
CYAN, WHITE = (72, 232, 238), (255, 255, 255)
FONT = ImageFont.truetype(f"{D}/fonts/BeVietnamPro-ExtraBold.ttf", 76)
SUB_Y = int(H * 0.80)  # tâm khối phụ đề (1/3 dưới, ngay trên ngực như mẫu)

def render_sub(lines):
    pad, lh = 40, 104
    img = Image.new("RGBA", (W, lh * len(lines) + pad * 2), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    space = dr.textlength(" ", font=FONT)
    for i, line in enumerate(lines):
        words = line.split(" ")
        widths = [dr.textlength(w.strip("*"), font=FONT) for w in words]
        x = (W - (sum(widths) + space * (len(words) - 1))) / 2
        y = pad + i * lh
        for w, wd in zip(words, widths):
            col = CYAN if w.startswith("*") else WHITE
            # bóng mềm
            dr.text((x + 3, y + 5), w.strip("*"), font=FONT, fill=(0, 0, 0, 150), stroke_width=7, stroke_fill=(0, 0, 0, 150))
            dr.text((x, y), w.strip("*"), font=FONT, fill=col, stroke_width=6, stroke_fill=(10, 10, 10))
            x += wd + space
    arr = np.array(img)
    # làm mềm bóng một chút
    return arr

SUBS = [(RM(a), RM(b), l) for a, b, l in SUBS]
SUB_IMGS = [render_sub(s[2]) for s in SUBS]

# ---------- Khung kết: đáy tối + CTA 2 dòng trắng/vàng + chữ ký (giống thumbnail) ----------
def make_end_card():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = np.zeros((H, W, 4), np.uint8)
    yy_ = np.arange(H)[:, None]
    g[..., 3] = (np.clip((yy_ - H * 0.52) / (H * 0.22), 0, 1) ** 1.3 * 235).astype(np.uint8)
    img = Image.fromarray(g)
    dr = ImageDraw.Draw(img)
    TF = ImageFont.truetype(f"{D}/fonts/BarlowCondensed-Bold.ttf", 118)
    for i, (txt, col) in enumerate([("BẠN NGHĨ SAO?", (255, 198, 43)), ("BÌNH LUẬN CHO GIÀU BIẾT NHÉ", (255, 255, 255))]):
        f2 = TF if i == 0 else ImageFont.truetype(f"{D}/fonts/BarlowCondensed-Bold.ttf", 92)
        dr.text(((W - dr.textlength(txt, font=f2)) / 2, H * 0.735 + i * 130), txt, font=f2, fill=col)
    SF = ImageFont.truetype(f"{D}/fonts/DancingScript-VF.ttf", 58)
    SF.set_variation_by_name("Medium")
    sig = "- Ngọc Giàu -"
    sy = int(H * 0.895)
    dr.text(((W - dr.textlength(sig, font=SF)) / 2, sy - 40), sig, font=SF, fill=(235, 235, 235))
    xs = np.linspace(-1, 1, 200)
    dr.line([(W / 2 + 260 * x, sy + 75 - 14 * np.sin(np.pi * (x + 1) * 0.9) * (1 - x * 0.3)) for x in xs],
            fill=(230, 230, 230), width=4, joint="curve")
    return np.array(img)
END_IMG = make_end_card()


def overlay(dst, rgba, cx, cy, scale=1.0, alpha=1.0):
    if scale != 1.0:
        rgba = cv2.resize(rgba, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    h, w = rgba.shape[:2]
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    xa, ya, xb, yb = max(x0, 0), max(y0, 0), min(x0 + w, W), min(y0 + h, H)
    if xa >= xb or ya >= yb:
        return
    s = rgba[ya - y0:yb - y0, xa - x0:xb - x0]
    a = s[..., 3:4].astype(np.float32) / 255 * alpha
    roi = dst[ya:yb, xa:xb].astype(np.float32)
    dst[ya:yb, xa:xb] = (roi * (1 - a) + s[..., :3] * a).astype(np.uint8)

# ---------- Tông màu ấm như mẫu (nắng chiều) ----------
lut = np.arange(256, dtype=np.float32) / 255
curve = lut + 0.08 * np.sin(np.pi * (lut - 0.5)) * (1 - np.abs(2 * lut - 1))  # S-curve nhẹ
LUT_R = np.clip((curve * 1.05 + 0.025) * 255, 0, 255).astype(np.uint8)
LUT_G = np.clip((curve * 1.00 + 0.008) * 255, 0, 255).astype(np.uint8)
LUT_B = np.clip((curve * 0.88) * 255, 0, 255).astype(np.uint8)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
VIG = (1 - 0.28 * (((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H * 0.42) / (H * 0.7)) ** 2)).clip(0.6, 1)[..., None]

def grade(f):
    g = np.dstack([cv2.LUT(f[..., 0], LUT_R), cv2.LUT(f[..., 1], LUT_G), cv2.LUT(f[..., 2], LUT_B)])
    # ánh vàng ấm ở vùng sáng
    glow = cv2.GaussianBlur(g, (0, 0), 25).astype(np.float32)
    g = g.astype(np.float32) + 0.10 * np.clip(glow - 150, 0, None) * np.array([1.0, 0.75, 0.35])
    return np.clip(g * VIG, 0, 255).astype(np.uint8)

# ---------- Zoom nhịp: đổi mức zoom mỗi cụm phụ đề (jump-zoom) ----------
# đổi mức zoom ngay tại vết cắt (che jump-cut), bỏ các vết cắt quá sát nhau
ZCUTS = [0.0]
for c in CUTS:
    if c - ZCUTS[-1] >= 0.9:
        ZCUTS.append(c)
ZOOMS = [1.00, 1.09, 1.02, 1.12, 1.04, 1.10]
FACE = (540, 640)  # tâm khuôn mặt trong khung gốc

ZT = 0.15  # thời gian đẩy zoom sang mức mới

def zoom_at(t):
    k = max(i for i, c in enumerate(ZCUTS) if c <= t)
    z = zoom_level(k, t)
    if k > 0 and t - ZCUTS[k] < ZT:
        z0 = zoom_level(k - 1, ZCUTS[k])
        z = z0 + (z - z0) * ease((t - ZCUTS[k]) / ZT)
    return z

def zoom_level(k, t):
    end = ZCUTS[k + 1] if k + 1 < len(ZCUTS) else 20.0
    return ZOOMS[k % len(ZOOMS)] + 0.025 * min(1, (t - ZCUTS[k]) / (end - ZCUTS[k]))  # trôi chậm vào

def ease(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def apply_zoom(f, z):
    if z <= 1.0001:
        return f
    cw, ch = W / z, H / z
    x0 = np.clip(FACE[0] - cw / 2, 0, W - cw); y0 = np.clip(FACE[1] - ch * 0.36, 0, H - ch)
    M = np.float32([[z, 0, -x0 * z], [0, z, -y0 * z]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def ease(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

# Hiệu ứng 1: thu khung thành thẻ bo góc (PiP) — "CỦA MÌNH"
BLUR = RM(8.00)
FLASHES = []
PIP = (RM(1.96), RM(2.50))
def pip(f, t):
    a, b = PIP
    k = min(ease((t - a) / 0.14), ease((b - t) / 0.14))
    if k <= 0:
        return f
    bg = cv2.GaussianBlur(cv2.resize(f, None, fx=0.25, fy=0.25), (0, 0), 8)
    bg = (cv2.resize(bg, (W, H)) * 0.85).astype(np.uint8)
    s = 1 - 0.56 * k
    card = cv2.resize(f, (int(W * s), int(H * s)))
    r = int(40 * k) + 1
    m = np.zeros(card.shape[:2], np.uint8)
    cv2.rectangle(m, (r, 0), (m.shape[1] - r, m.shape[0]), 255, -1)
    cv2.rectangle(m, (0, r), (m.shape[1], m.shape[0] - r), 255, -1)
    for cx, cy in [(r, r), (m.shape[1] - r, r), (r, m.shape[0] - r), (m.shape[1] - r, m.shape[0] - r)]:
        cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
    rgba = np.dstack([card, m])
    cy = H / 2 + (H * 0.36 - H / 2) * k
    overlay(bg, rgba, W / 2, cy)
    return bg

# Hiệu ứng 2: nhòe mờ nhanh — mở ý "THẾ MÀ TẠI SAO" (như "THẾ THÌ" của mẫu)
def blur_pulse(f, t, c, d=0.30):
    k = 1 - abs(t - c) / d
    if k <= 0:
        return f
    return cv2.GaussianBlur(f, (0, 0), 1 + 14 * k)

# Hiệu ứng 3: lóe sáng trắng — "CHÍNH MÌNH"
def flash(f, t, c):
    if t < c - 0.08 or t > c + 0.9:
        return f
    k = ease((t - (c - 0.08)) / 0.08) if t < c else 1 - ease((t - c) / 0.9)
    soft = cv2.GaussianBlur(f, (0, 0), 20).astype(np.float32)
    g = f.astype(np.float32) * (1 - 0.45 * k) + (soft * 0.5 + 255 * 0.5) * 0.45 * k
    return np.clip(g, 0, 255).astype(np.uint8)

# ---------- Tách nền (người sắc nét, kệ sách mờ như máy ảnh xóa phông) ----------
seg = mp.tasks.vision.ImageSegmenter.create_from_options(mp.tasks.vision.ImageSegmenterOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=f"{D}/seg_mc.tflite"),
    running_mode=mp.tasks.vision.RunningMode.VIDEO, output_confidence_masks=True))

dec = subprocess.Popen([FF, "-loglevel", "error", "-i", SRC, "-vf", f"fps={FPS},scale={W}:{H}",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen([FF, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                        "-pix_fmt", "yuv420p", OUT], stdin=subprocess.PIPE)
prev_mask, i = None, 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3:
        break
    f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
    t = i / FPS
    small = np.ascontiguousarray(cv2.resize(f, (W // 4, H // 4)))
    res = seg.segment_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=small), int(t * 1000))
    m = 1 - res.confidence_masks[0].numpy_view().astype(np.float32)  # lớp 0 = nền
    m = cv2.GaussianBlur(cv2.resize(m, (W, H)), (0, 0), 6)
    prev_mask = m if prev_mask is None else 0.6 * m + 0.4 * prev_mask
    m3 = np.clip((prev_mask - 0.35) / 0.45, 0, 1)[..., None]
    bg = cv2.GaussianBlur(cv2.resize(f, (W // 3, H // 3)), (0, 0), 7)
    bg = cv2.resize(bg, (W, H))
    f = (f * m3 + bg * (1 - m3)).astype(np.uint8)

    f = grade(f)
    f = apply_zoom(f, zoom_at(t))
    f = pip(f, t)
    f = blur_pulse(f, t, BLUR)
    f = flash(f, t, RM(12.78))  # CUỘC ĐỜI CỦA MÌNH
    for (a, b, _), img in zip(SUBS, SUB_IMGS):
        if a <= t < b:
            p = ease((t - a) / 0.10)
            overlay(f, img, W / 2, SUB_Y, scale=0.86 + 0.14 * p, alpha=min(1, 0.3 + p))
    if t >= END_CARD:
        overlay(f, END_IMG, W / 2, H / 2, alpha=ease((t - END_CARD) / 0.35))
    enc.stdin.write(f.tobytes())
    i += 1
enc.stdin.close(); enc.wait(); dec.wait()

# ---------- Âm thanh phụ tại các điểm chuyển ----------
import re as _re
flashes = [RM(float(x)) for x in _re.findall(r"flash\(f, t, RM\(([\d.]+)\)\)", open(__file__).read())]
ev = [("whoosh", PIP[0] - 0.12), ("click", PIP[1] - 0.05), ("whoosh", BLUR - 0.18)] + [("bling", c - 0.04) for c in flashes]

ev += [('keys', END_CARD + 0.1), ('ding', END_CARD + 0.75)]
busy = [t for _, t in ev]
for i, c in enumerate(ZCUTS[1:]):
    if all(abs(c - b) > 0.4 for b in busy):
        ev.append(("click" if i % 3 != 2 else "keys2", c - 0.02))
json.dump(sorted(ev, key=lambda e: e[1]), open(f"{D}/v2/events.json", "w"))
print("events", sorted(ev, key=lambda e: e[1]))
print("frames", i)
