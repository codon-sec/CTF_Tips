# 用途: 先頭から数えた数字→アルファベット変換
alpha_list = []
alpha_list = [chr(ord('a') + i) for i in range(26)]
target_list = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5,
               14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
result_list = []
for i in target_list:
    result_list.append(alpha_list[i-1])
[print(i, end="") for i in result_list]
