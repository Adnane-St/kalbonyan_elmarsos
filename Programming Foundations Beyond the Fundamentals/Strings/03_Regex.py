import re

five_digit_zip = '46000'
nine_digit_zip = '46000-2223'
tel = '+212-710-126-810'
reg = r'\d{5}'

print(re.match(reg,five_digit_zip))
print(re.match(reg,nine_digit_zip))
print(re.match(reg,tel))
