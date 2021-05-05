import math

x = input("2分探索したい数字を入力してください")

y_min = 0
y_max = 10 ** 300  # ここは適当
y_jou = 101

for num in range(0, 2000):  # 2000も適当
    mid = (y_min + y_max) // 2
    guess = pow(mid, y_jou)
    if guess == x:
        print(mid)
        break
    elif guess > x:
        y_max = mid
        print("大きすぎ")
    elif guess < x:
        y_min = mid
        print("小さすぎ")
    keta = int(math.log10(mid) + 1)
    print(str(num) + ": " + str(keta) + "桁")
