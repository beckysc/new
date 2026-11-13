"""二手拍賣商品資料（照片分組、標題、描述、建議售價）。

價格為參考行情的建議價，上架前請自行確認。
weight_kg 為含包裝的估計重量，用來判斷能否超商寄送。
"""

COMMON_NOTE = (
    "\n\n【購買須知】\n"
    "・二手自用品，介意者請勿下標\n"
    "・實際狀況以照片為準，有問題歡迎先聊聊\n"
    "・商品出貨前會再檢查一次"
)

PRODUCTS = [
    {
        "folder": "01_iCandy_Apple2Pear推車",
        "photos": ["IMG_1250.JPG", "IMG_1255.JPG", "IMG_1248.JPG", "IMG_1249.JPG",
                   "IMG_1253.JPG", "IMG_1254.JPG", "IMG_1256.JPG"],
        "category": "嬰幼兒用品 > 嬰兒推車",
        "title": "【二手】英國 iCandy Apple 2 Pear 嬰兒推車 含睡箱 座椅 雨罩 轉接器 說明書",
        "price": 7500,
        "stock": 1,
        "weight_kg": 15,
        "shipping": "宅配 / 面交",
        "description": (
            "英國 iCandy Apple 2 Pear 嬰兒推車，鋁合金車架，大後輪推起來穩。\n\n"
            "【內容物】\n"
            "・推車車架\n"
            "・睡箱（新生兒可平躺）\n"
            "・座椅布套與遮陽篷（黑色、藍色兩組）\n"
            "・透明雨罩\n"
            "・蚊帳\n"
            "・汽座轉接器一組\n"
            "・中文使用說明書\n\n"
            "【商品狀況】\n"
            "・功能正常，煞車與收折皆可使用\n"
            "・睡箱內襯有正常使用痕跡，詳見照片\n\n"
            "【運送】\n"
            "體積較大，無法超商取貨，限宅配或面交。"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "02_Graco推車",
        "photos": ["IMG_1258.JPG", "IMG_1262.JPG", "IMG_1261.JPG", "IMG_1259.JPG", "IMG_1263.JPG"],
        "category": "嬰幼兒用品 > 嬰兒推車",
        "title": "【二手】GRACO CITINEXT CTS 購物型雙向嬰幼兒手推車 豪華休旅 咖啡色 附雨罩",
        "price": 1800,
        "stock": 1,
        "weight_kg": 8,
        "shipping": "宅配 / 面交",
        "description": (
            "GRACO 購物型雙向嬰幼兒手推車 豪華休旅 CITINEXT CTS，咖啡卡其配色。\n"
            "（與官網同款，花色不同）\n\n"
            "【規格】\n"
            "・適用：滿月起至約 3 歲，體重 15 公斤以下\n"
            "・展開尺寸：長 93~98 x 寬 53 x 高 97.5~105.5 cm\n"
            "・收折尺寸：長 37 x 寬 53 x 高 95 cm\n"
            "・車重：5.8 公斤\n"
            "・符合美國 ASTM 安全標準\n\n"
            "【商品特色】\n"
            "・雙向推把，可面向爸媽或面向前方\n"
            "・靠背多段式調整\n"
            "・座椅高度 56 cm，加寬座椅\n"
            "・全罩式遮陽篷\n"
            "・立體透氣坐墊\n"
            "・Carry Travel System，可搭配同品牌提籃\n"
            "・下方置物籃容量大\n\n"
            "【內容物】\n"
            "・推車本體\n"
            "・透明雨罩\n\n"
            "【商品狀況】\n"
            "・功能正常，可正常收折\n"
            "・布料有正常使用痕跡，詳見照片\n\n"
            "【運送】\n"
            "體積較大，無法超商取貨，限宅配或面交。"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "03_Cybex_Pallas_S-fix汽座",
        "photos": ["IMG_1264.JPG", "IMG_1265.JPG"],
        "category": "嬰幼兒用品 > 汽車安全座椅",
        "title": "【二手】德國 Cybex Pallas S-fix 成長型汽座 9-36kg ISOFIX 含緩衝屏",
        "price": 6000,
        "stock": 1,
        "weight_kg": 12,
        "shipping": "宅配 / 面交",
        "description": (
            "德國 CYBEX Pallas S-fix 成長型安全座椅，可從約 1 歲一路用到 12 歲左右。\n\n"
            "【規格】\n"
            "・Group I：9~18kg，使用緩衝屏 + 底盤 + ISOFIX\n"
            "・Group II/III：15~36kg，拆下緩衝屏改用車上三點式安全帶\n"
            "・前向安裝\n"
            "・產品淨重 10.3 公斤\n"
            "・製造日期 2021 年 9 月，有效期限為購買日起 11 年\n"
            "・台灣代理商公司貨，有中文標示\n\n"
            "【內容物】\n"
            "・座椅本體\n"
            "・緩衝屏\n"
            "・ISOFIX 底盤\n"
            "・配件與原廠配件盒\n\n"
            "【商品狀況】\n"
            "・無事故紀錄\n"
            "・布套有正常使用痕跡，詳見照片\n\n"
            "【運送】\n"
            "體積較大，無法超商取貨，限宅配或面交。"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "04_Fisher-Price安撫躺椅",
        "photos": ["IMG_1266.JPG", "IMG_1267.JPG", "IMG_1268.JPG", "IMG_1269.JPG"],
        "category": "嬰幼兒用品 > 嬰兒搖椅",
        "title": "【二手】Fisher-Price 費雪 可攜式安撫躺椅 搖椅 新生兒到幼兒 附玩具吊架",
        "price": 900,
        "stock": 1,
        "weight_kg": 4,
        "shipping": "宅配 / 面交",
        "description": (
            "費雪 Fisher-Price 可攜式安撫躺椅，新生兒可躺、長大後可改成幼兒座椅。\n\n"
            "【商品特色】\n"
            "・可固定或搖擺兩種模式\n"
            "・內建震動安撫功能（需電池）\n"
            "・附可拆式玩具吊架與兩個吊飾\n"
            "・座墊可拆下清洗\n"
            "・腳架可收折，方便收納\n\n"
            "【商品狀況】\n"
            "・功能正常\n"
            "・布墊已清洗，有正常使用痕跡\n\n"
            "【運送】\n"
            "收折後尺寸較大，建議宅配或面交。"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "05_Hape小騎士平衡車",
        "photos": ["IMG_1271.JPG", "IMG_1270.JPG", "IMG_1272.JPG"],
        "category": "嬰幼兒用品 > 嬰幼兒玩具 > 騎乘玩具",
        "title": "【全新】德國 Hape 小騎士平衡車 Little Rider 白色 3歲以上 原盒",
        "price": 1800,
        "stock": 1,
        "weight_kg": 4,
        "shipping": "宅配 / 面交",
        "description": (
            "德國 Hape 小騎士平衡車 Little Rider Balance Bike，白色奶茶配色。\n\n"
            "【商品特色】\n"
            "・適合 3 歲以上\n"
            "・座椅高度可調整\n"
            "・輕量車身，小朋友容易操控\n"
            "・無踏板設計，練習平衡感\n\n"
            "【內容物】\n"
            "・平衡車（原盒裝）\n"
            "・中文組裝說明書\n\n"
            "【商品狀況】\n"
            "・全新未使用，原盒保存（開盒拍照確認內容物）\n\n"
            "【運送】\n"
            "外盒較長，無法超商取貨，限宅配或面交。\n\n"
            "【購買須知】\n"
            "・有問題歡迎先聊聊\n"
            "・商品出貨前會再檢查一次"
        ),
    },
    {
        "folder": "06_PUKU環抱揹巾",
        "photos": ["IMG_1274.JPG"],
        "category": "嬰幼兒用品 > 揹巾/揹帶",
        "title": "【二手】PUKU 藍色企鵝 多功能環抱揹巾 Lite Baby Wrap Carrier 0-36個月",
        "price": 500,
        "stock": 1,
        "weight_kg": 1,
        "shipping": "7-11 / 全家 / 萊爾富 / 宅配",
        "description": (
            "PUKU 藍色企鵝 多功能環抱揹巾 Lite Baby Wrap Carrier。\n\n"
            "【規格】\n"
            "・適用 0~36 個月\n"
            "・最大承重 15 公斤\n"
            "・環扣設計，可快速調整鬆緊\n\n"
            "【內容物】\n"
            "・揹巾（原盒裝）\n\n"
            "【商品狀況】\n"
            "・保存良好，詳見照片"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "07_絨毛娃娃組",
        "photos": ["IMG_1273.JPG"],
        "category": "嬰幼兒用品 > 嬰幼兒玩具 > 絨毛玩具",
        "title": "【二手】絨毛娃娃 4 隻一組 灰色長耳兔 小羊 白色小狗 吊飾",
        "price": 250,
        "stock": 1,
        "weight_kg": 1,
        "shipping": "7-11 / 全家 / 萊爾富 / 宅配",
        "description": (
            "絨毛娃娃 4 隻一起出清。\n\n"
            "【內容】\n"
            "・灰色長耳兔安撫娃娃 x1\n"
            "・小羊娃娃 x1\n"
            "・白色小狗（抱紅蘿蔔）x1\n"
            "・藍色小吊飾 x1\n\n"
            "【商品狀況】\n"
            "・已清洗，有正常使用痕跡"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "08_玩具軌道",
        "photos": ["IMG_1275.JPG"],
        "category": "嬰幼兒用品 > 嬰幼兒玩具 > 軌道玩具",
        "title": "【二手】兒童火車軌道 彎道直道 一組 可圍成一圈",
        "price": 150,
        "stock": 1,
        "weight_kg": 1,
        "shipping": "7-11 / 全家 / 萊爾富 / 宅配",
        "description": (
            "兒童玩具火車軌道一組，含彎道與直道，可組成一整圈（如照片）。\n"
            "可搭配一般木製或塑膠玩具火車使用，購買前請先確認接頭是否相容。\n\n"
            "【商品狀況】\n"
            "・有正常使用痕跡"
            + COMMON_NOTE
        ),
    },
    {
        "folder": "09_大顆粒積木",
        "photos": ["IMG_1276.JPG"],
        "category": "嬰幼兒用品 > 嬰幼兒玩具 > 積木",
        "title": "【二手】大顆粒積木 一盒 含溜滑梯 小鴨 椰子樹 風車 配件",
        "price": 300,
        "stock": 1,
        "weight_kg": 2,
        "shipping": "7-11 / 全家 / 萊爾富 / 宅配",
        "description": (
            "大顆粒積木一批，適合幼兒抓握。\n\n"
            "【內容】\n"
            "・各色基本積木\n"
            "・溜滑梯、彎道、風車、椰子樹、小鴨等造型配件\n"
            "・數量以照片為準\n\n"
            "【商品狀況】\n"
            "・有正常使用痕跡\n"
            "・零件細小部分請在大人陪同下使用"
            + COMMON_NOTE
        ),
    },
]
