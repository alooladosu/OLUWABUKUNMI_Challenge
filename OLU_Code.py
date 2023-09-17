from itertools import groupby
import re

pattern = re.compile(r'(?:\d{4}-){3}\d{4}|\d{16}')

def count_consecutive(num):
    return max(len(list(g)) for _, g in groupby(num))

num = '6244-5567-8912-3458'
if not pattern.fullmatch(num) or count_consecutive(num.replace('-', '')) >= 4:
    print('Failed')
else:
   print('Success')
   
   