"""產生蝦皮上架資料：Excel 總表 + 每個商品的文字檔（方便複製貼上）。

用法: python3 build_listing.py <輸出資料夾>
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

from products import PRODUCTS

HEADERS = ["編號", "圖片資料夾", "圖片數", "分類", "商品名稱", "字數", "商品描述",
           "建議售價", "庫存", "估計重量(kg)", "運送方式"]
WIDTHS = [6, 26, 7, 28, 50, 6, 70, 10, 6, 12, 26]


def main(dst):
    wb = Workbook()
    ws = wb.active
    ws.title = "上架清單"
    ws.append(HEADERS)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="EE4D2D")
    for i, p in enumerate(PRODUCTS, 1):
        ws.append([i, p["folder"], len(p["photos"]), p["category"], p["title"], len(p["title"]),
                   p["description"], p["price"], p["stock"], p["weight_kg"], p["shipping"]])
    for col, w in zip("ABCDEFGHIJK", WIDTHS):
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"
    total = len(PRODUCTS) + 1
    ws.append([])
    ws.append(["", "", "", "", "合計", "", "", f"=SUM(H2:H{total})"])
    wb.save(os.path.join(dst, "蝦皮上架清單.xlsx"))

    for p in PRODUCTS:
        with open(os.path.join(dst, p["folder"], "上架文案.txt"), "w", encoding="utf-8") as f:
            f.write(f"商品名稱：\n{p['title']}\n\n分類：{p['category']}\n"
                    f"售價：{p['price']}\n庫存：{p['stock']}\n運送：{p['shipping']}\n\n"
                    f"商品描述：\n{p['description']}\n")
    print("done")


if __name__ == "__main__":
    main(sys.argv[1])
