# HW10 第4題：清理素材點擊資料並產生排名
# 姓名：吳宜蓁　學號：D1399089


def select_clicks(raw_clicks, min_clicks=10):
    """清理點擊資料並篩選達門檻的紀錄，回傳 (numbers, qualified)。"""
    stripped = map(lambda text: text.strip(), raw_clicks)   # 1. 去掉頭尾空白
    non_empty = filter(None, stripped)                       # 2. 刪掉空字串（"0" 仍保留）
    numbers = list(map(int, non_empty))                      # 3. 轉整數並保存
    qualified = list(filter(lambda x: x >= min_clicks, numbers))  # 4. 篩選合格項目
    return (numbers, qualified)


# ---- 共同設定：讀取學號 ----
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# ---- 依學號產生資料 ----
raw_clicks = [str(10 + a), "0", "", " " + str(5 + b) + " ",
              " ", str(15 + c), str(5 + b)]
min_clicks = 5 + b

numbers, qualified = select_clicks(raw_clicks, min_clicks)

print(f"學號：{student_id}")
print(f"點擊門檻：{min_clicks}")
print(f"清理結果：{numbers}")
print(f"合格結果：{qualified}")
print(f"合格筆數：{len(qualified)}")
print(f"合格合計：{sum(qualified)}")

# 由大到小排序後編排名次
for rank, clicks in enumerate(sorted(qualified, reverse=True), start=1):
    print(f"第{rank}名：{clicks}次")

# 門檻 100 的測試
_, qualified_100 = select_clicks(raw_clicks, 100)
print(f"門檻100合格結果：{qualified_100}")
print(f"門檻100合格筆數：{len(qualified_100)}")
print(f"門檻100合格合計：{sum(qualified_100)}")
if len(qualified_100) == 0:
    print("無符合門檻的素材")
