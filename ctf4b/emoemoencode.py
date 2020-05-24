#!/usr/bin/env python3
text = '🍣🍴🍦🌴🍢🍻🍳🍴🍥🍧🍡🍮🌰🍧🍲🍡🍰🍨🍹🍟🍢🍹🍟🍥🍭🌰🌰🌰🌰🌰🌰🍪🍩🍽 '
diff = ord('🍡') - ord('a')
flag = ''
for s in text:
    flag += chr(ord(s) - diff)
print(flag)