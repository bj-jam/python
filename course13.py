import glob
import os

print(os.getcwd())
print(glob.glob('*.py'))

from datetime import date
import datetime
import time

now = date.today()
print(now)

b = date(1989, 6, 3)
age = now - b
print(age.days)

today = date.today()  # 今天
print(today)
yesterday = today - datetime.timedelta(days=1)  # 昨天
print(yesterday)
last_month = today.month - 1 if today.month - 1 else 12  # 上个月
print(last_month)
time_stamp = time.time()  # 当前时间戳
print(time_stamp)
datetime.datetime.fromtimestamp(time_stamp)  # 时间戳转datetime
print(datetime.datetime.fromtimestamp(time_stamp))
# datetime转时间戳
int(time.mktime(today.timetuple()))
# datetime转字符串
today_str = today.strftime("%Y-%m-%d")
# 字符串转datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
# 补时差
today + datetime.timedelta(hours=8)

# 文件操作

import re

s = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(s)

import random

b = random.choice(['apple', 'pear', 'banana'])
print(b)

c = random.sample(range(10), 8)  # 无放回抽样
print(c)

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)


import zlib

s = b"witch which has which witches wrist watch"
print(len(s))
d = zlib.compress(s)
print(d)
