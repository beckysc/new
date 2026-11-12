"""把原始照片整理成蝦皮上架用圖片。

做法：依 EXIF 轉正、補白邊成 1:1 正方形、縮到 1200x1200、
存成 JPEG（小於 2MB），並移除 EXIF（含 GPS 位置）。

用法: python3 process_photos.py <原始照片資料夾> <輸出資料夾>
"""
import os
import sys

from PIL import Image, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

from products import PRODUCTS

SIZE = 1200


def to_square(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    im.thumbnail((SIZE, SIZE), Image.LANCZOS)
    canvas = Image.new("RGB", (SIZE, SIZE), "white")
    canvas.paste(im, ((SIZE - im.width) // 2, (SIZE - im.height) // 2))
    return canvas


def main(src, dst):
    for p in PRODUCTS:
        folder = os.path.join(dst, p["folder"])
        os.makedirs(folder, exist_ok=True)
        for i, name in enumerate(p["photos"], 1):
            out = os.path.join(folder, f"{i:02d}.jpg")
            to_square(os.path.join(src, name)).save(out, "JPEG", quality=85, optimize=True)
            print(out, os.path.getsize(out) // 1024, "KB")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
