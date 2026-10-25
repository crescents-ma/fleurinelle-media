"""Make 1080x1920 TikTok versions of every post image: design centred in the
safe zone on a blurred, softened backdrop of the same image."""
from PIL import Image, ImageFilter, ImageEnhance
import os, glob
ROOT = "/home/claude/fleurinelle-media/posts"
W, H = 1080, 1920
for folder in sorted(glob.glob(f"{ROOT}/*")):
    out = os.path.join(folder, "tiktok"); os.makedirs(out, exist_ok=True)
    for f in sorted(glob.glob(f"{folder}/*.jpg")):
        im = Image.open(f).convert("RGB")
        # backdrop: cover-fit, heavy blur, slightly lighter
        s = max(W / im.width, H / im.height)
        bg = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
        l = (bg.width - W) // 2; t = (bg.height - H) // 2
        bg = bg.crop((l, t, l + W, t + H)).filter(ImageFilter.GaussianBlur(40))
        bg = ImageEnhance.Brightness(bg).enhance(0.92)
        # design: full width, placed in TikTok's visible zone (clear of the top bar and the bottom caption)
        fg = im.resize((1080, 1350), Image.LANCZOS)
        y = 190
        bg.paste(fg, (0, y))
        bg.save(os.path.join(out, os.path.basename(f)), quality=88, optimize=True)
print("done", len(glob.glob(f"{ROOT}/*/tiktok/*.jpg")), "images")
