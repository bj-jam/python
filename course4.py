# \(在行尾时) 	续行符
# \\ 	反斜杠符号
# \' 	单引号
# \" 	双引号
# \a 	响铃
# \b 	退格(Backspace)
# \000 	空
# \n 	换行
# \v 	纵向制表符
# \t 	横向制表符
# \r 	回车
# \f 	换页
# \oyy 	八进制数，yy 代表的字符，例如：\o12 代表换行，其中 o 是字母，不是数字 0。
# \xyy 	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other 	其它的字符以普通格式输出


# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True 	'H' in a 输出结果 True
# not in 	成员运算符 - 如果字符串中不包含给定的字符返回 True 	'M' not in a 输出结果 True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
#
# print( r'\n' )
# print( R'\n' )
#
# %	格式字符串

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
#       %c	 格式化字符及其ASCII码
#       %s	 格式化字符串
#       %d	 格式化整数
#       %u	 格式化无符号整型
#       %o	 格式化无符号八进制数
#       %x	 格式化无符号十六进制数
#       %X	 格式化无符号十六进制数（大写）
#       %f	 格式化浮点数字，可指定小数点后的精度
#       %e	 用科学计数法格式化浮点数
#       %E	 作用同%e，用科学计数法格式化浮点数
#       %g	 %f和%e的简写
#       %G	 %f 和 %E 的简写
#       %p	 用十六进制数格式化变量的地址
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
# f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')
# 将字符串的第一个字符转换为大写
string = "this is string example from runoob....wow!!!"
print("str.capitalize() : ", string.capitalize())
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
str = "[runoob]"
print("str.center(40, '*') : ", str.center(40, '*'))
print("str.center(40, '*') : ", str.center(40))

# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))
sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))
# 以 encoding 指定的编码格式编码字符串、解码字符串
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'dfasdfasdfas'))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
str = "this is\tstring example....wow!!!"
print("原始字符串: " + str)
print("替换 \\t 符号: " + str.expandtabs())
print("使用16个空格替换 \\t 符号: " + str.expandtabs(16))

# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
print(s1.join(seq))
print(s2.join(seq))

str = "runoob"
print(len(str))
