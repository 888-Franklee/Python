# ユーザーから年を入力
year = int(input("年を入力してください: "))

def is_leap_year(year):
    """
    引数で与えられた年が閏年かどうかを判定します。
    条件:
    - 4で割り切れるが100で割り切れない
    - または400で割り切れる
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("是闰年")  # 閏年
        return True
    else:
        print("是平年")  # 平年
        return False

# 関数を呼び出して結果を判定
is_leap_year(year)
