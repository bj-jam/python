s = 'Hello, Runoob'
print(str(s))
print(repr(s))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

str = input("请输入：");
print("你输入的内容是: ", str)

f = open("test", "r")

f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

# 关闭打开的文件
f.close()

import pickle

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
