# dec = int(input("输入数字："))
#
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))
#
# # 用户输入字符
# c = input("请输入一个字符: ")
#
# # 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
#
# print(c + " 的ASCII 码为", ord(c))
# print(a, " 对应的字符为", chr(a))

import calendar

print(calendar.mdays)
print(calendar.mdays[9])

import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:

    input("")  # 如果是 python 2.x 版本请使用 raw_input()
    starttime = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\n ")
            # print("---")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break
