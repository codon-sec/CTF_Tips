import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


# 円周率 とりあえず100桁
pi = ""
x = 0

while x < 90:
    num = int(pi[x: x + 10])  # 10桁の円周率を抽出
    if is_prime(num):
        print(num)
        break
    x += 1
