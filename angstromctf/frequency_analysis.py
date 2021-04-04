# python 3.7.3+ required
import re

is_code_regex = re.compile(r"[a-zA-Z]+")
text = input()
mo = is_code_regex.findall(text)

mo_join = "".join(mo).lower()

count_code = {}
for i in mo_join:
    if i in count_code.keys():
        count_code[i] += 1
    else:
        count_code[i] = 1

for k, v in sorted(count_code.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))