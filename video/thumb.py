"""Thumbnail theo mẫu: ảnh cười cận mặt, nền mờ tông ấm, đáy đen, tiêu đề 2 dòng trắng + vàng, chữ ký viết tay."""
import sys, subprocess, numpy as np, cv2, imageio_ffmpeg, mediapipe as mp
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = __import__("os").environ.get("WORKDIR", ".")
NAME = sys.argv[1] if len(sys.argv) > 1 else ""  # tên hiển thị dưới tiêu đề, vd "Thu Hà"
T = 9.5
W, H = 1080, 1920
TITLE = [["*ĐỪNG XIN PHÉP*", "NGƯỜI KHÁC"], ["ĐỂ ĐƯỢC SỐNG", "*CUỘC ĐỜI CỦA MÌNH*"]]
YELLOW, WHITE = (255, 198, 43), (255, 255, 255)

raw = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-ss", str(T), "-i", f"{D}/src.mov",
                      "-frames:v", "1", "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                     capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(H, W, 3).copy()

# tách nền + xóa phông
seg = mp.tasks.vision.ImageSegmenter.create_from_options(mp.tasks.vision.ImageSegmenterOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=f"{D}/seg_mc.tflite"), output_confidence_masks=True))
m = 1 - seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(cv2.resize(f, (540, 960))))
                    ).confidence_masks[0].numpy_view().astype(np.float32)
m = np.clip((cv2.GaussianBlur(cv2.resize(m, (W, H)), (0, 0), 5) - 0.35) / 0.45, 0, 1)[..., None]
bg = cv2.resize(cv2.GaussianBlur(cv2.resize(f, (W // 3, H // 3)), (0, 0), 9), (W, H))
f = (f * m + bg * (1 - m)).astype(np.uint8)

# tông ấm (giống video)
lut = np.arange(256, dtype=np.float32) / 255
curve = lut + 0.08 * np.sin(np.pi * (lut - 0.5)) * (1 - np.abs(2 * lut - 1))
luts = [np.clip((curve * a + b) * 255, 0, 255).astype(np.uint8) for a, b in [(1.05, .025), (1.0, .008), (.88, 0)]]
f = np.dstack([cv2.LUT(f[..., c], luts[c]) for c in range(3)])
glow = cv2.GaussianBlur(f, (0, 0), 25).astype(np.float32)
f = np.clip(f + 0.10 * np.clip(glow - 150, 0, None) * np.array([1.0, .75, .35]), 0, 255).astype(np.uint8)

# cận mặt hơn (như mẫu, mặt chiếm ~1/2 bề ngang), hạ người xuống để chừa đáy cho chữ
z = 1.10  # điểm mặt (540,560) -> (540,640)
M = np.float32([[z, 0, 540 - 540 * z], [0, z, 640 - 560 * z]])
f = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

# đáy chuyển đen
yy = np.arange(H, dtype=np.float32)[:, None, None]
a = np.clip((yy - H * 0.56) / (H * 0.20), 0, 1) ** 1.3
f = (f * (1 - a)).astype(np.uint8)

img = Image.fromarray(f)
dr = ImageDraw.Draw(img)
size = 110
while True:  # tự co cỡ chữ để dòng dài nhất vừa 88% bề ngang
    TF = ImageFont.truetype(f"{D}/fonts/BarlowCondensed-Bold.ttf", size)
    if max(dr.textlength(" ".join(p.strip("*") for p in L), font=TF) for L in TITLE) <= W * 0.88:
        break
    size -= 2
y = int(H * 0.745)
for parts in TITLE:
    segs = [(p.strip("*"), YELLOW if p.startswith("*") else WHITE) for p in parts]
    sp = dr.textlength(" ", font=TF)
    ws = [dr.textlength(t, font=TF) for t, _ in segs]
    x = (W - sum(ws) - sp * (len(ws) - 1)) / 2
    for (t, c), w in zip(segs, ws):
        dr.text((x, y), t, font=TF, fill=c)
        x += w + sp
    y += int(size * 1.15)

# chữ ký viết tay + nét lượn
sig_y = int(H * 0.895)
if NAME:
    SF = ImageFont.truetype(f"{D}/fonts/DancingScript-VF.ttf", 58)
    SF.set_variation_by_name("Medium")
    s = f"- {NAME} -"
    dr.text(((W - dr.textlength(s, font=SF)) / 2, sig_y - 40), s, font=SF, fill=(235, 235, 235))
xs = np.linspace(-1, 1, 200)
pts = [(W / 2 + 260 * x, sig_y + 75 - 14 * np.sin(np.pi * (x + 1) * 0.9) * (1 - x * 0.3)) for x in xs]
dr.line(pts, fill=(230, 230, 230), width=4, joint="curve")
dr.line([(W / 2 - 262, sig_y + 70), (W / 2 - 240, sig_y + 60)], fill=(230, 230, 230), width=4)

img.save(f"{D}/thumbnail.jpg", quality=95)
print("ok")
