# HW10 第1題：製作自己的廣告成效報表
# 姓名：吳宜蓁　學號：D1399089


def ad_report(impressions, clicks, target=3.0):
    """計算 CTR（%）並判斷是否達標，回傳 (ctr, passed)。"""
    if impressions == 0:          # 沒有曝光，無法計算 CTR
        return (None, False)
    ctr = clicks / impressions * 100
    passed = ctr >= target        # 用原始 CTR 判斷，不先四捨五入
    return (ctr, passed)


# ---- 共同設定：讀取學號 ----
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# ---- 依學號產生資料 ----
ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0),
]
target = 2.5 + 0.1 * c

print(f"學號：{student_id}")
print(f"CTR門檻：{target:.2f}%")

passed_count = 0
for name, impressions, clicks in ads:
    ctr, passed = ad_report(impressions, clicks, target=target)  # 關鍵字引數傳入門檻
    if ctr is None:
        ctr_text = "無曝光資料"
    else:
        ctr_text = f"{ctr:.2f}%"
    if passed:
        passed_count += 1
    print(f"{name}：曝光={impressions}，點擊={clicks}，CTR={ctr_text}，達標={passed}")

print(f"達標廣告數：{passed_count}")
print(f"預設門檻測試：{ad_report(1000, 30)}")
print(f"零點擊測試：{ad_report(1000, 0)}")
