import sys

import course10

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

course10.printinfo(name="liuchunxiao", age=20)
course10.fib(20)
print(course10.fib2(20))
