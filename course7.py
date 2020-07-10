class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter), end="  ")
print(next(myiter), end="  ")
print(next(myiter), end="  ")
print(next(myiter), end="  ")
print(next(myiter))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x, end="  ")


# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#         print("+")
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end="")
#         print("--", end="")
#     except StopIteration:
#         sys.exit()


def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo("dfadf", 50)


def printinfo(arg1, *ddd):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(ddd)


# 调用printinfo 函数
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3, c=5, d=6)


def f(a, b, *, c):
    return a + b + c


print(f(1, 2, c=5))

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x, numbers))
print(newNumbers)
print(map(lambda x: x, numbers))