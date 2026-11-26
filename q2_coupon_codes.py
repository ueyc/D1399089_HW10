# HW10 第2題：整理兩場電子報活動的個人優惠碼
# 姓名：吳宜蓁　學號：D1399089


def collect_codes(raw_codes, saved=None):
    """整理優惠碼：去空白、轉大寫、略過空字串、去重複並保留首次出現順序。
    每次都回傳新串列，不修改 saved 與 raw_codes。"""
    if saved is None:
        result = []              # 未傳入 saved：從新的空串列開始
    else:
        result = saved.copy()    # 複製一份，避免修改原本的 saved
    for code in raw_codes:
        clean = code.strip().upper()
        if clean == "":
            continue             # 空字串略過
        if clean not in result:
            result.append(clean)
    return result


# ---- 共同設定：讀取學號 ----
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]            # 保留字串，開頭的 0 不會消失
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# ---- 依學號產生資料 ----
saved = ["BASE"]
raw_a = [" welcome" + tail + " ", "vip" + tail, "",
         "WELCOME" + tail, " "]
raw_b = [" new" + tail + " ", " welcome" + tail + " "]

activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

print(f"學號：{student_id}")
print(f"活動A：{activity_a}")
print(f"活動B：{activity_b}")
print(f"原始saved：{saved}")
print(f"原始raw_a：{raw_a}")
print(f"空資料：{collect_codes([])}")
