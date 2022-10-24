# 函数
# 函数的发明和使用是为了重复使用一段代码

# 函数的定义
# 首先需要写def关键字，define的前三个字母
# 然后写函数名称
# 函数的命名规则和变量的一致
# 然后后边加括号，括号里需要写参数
# 如果没有参数，可以不写
# 然后写冒号
# 为了表示一段代码属于某个函数
# 必须使用相同的缩进
# python代码是使用相同的缩进来表示层级关系的
# 函数有输入和输出
# 参数为输入，return后边跟函数返回值，即输出
def demo(x):
    return x + 5

# 如果函数有返回值，则函数的运行结果为指定的值
# 这个值可以赋值给变量等
y = demo(10)
print('y=', y)

# 两个参数的函数
def add(a, b):
    return a + b
print('add(10, 20)=', add(10, 20))

# 函数体中可以写任意多的代码
def test(x, y):
    print('Hi')
    print('现在开始计算x+y')
    z = x + y
    return z
print(test(5, 8))

# 计算正方形面积
def square(x):
    return x ** 2

# 计算长方形面积
def rec(x, y):
    return x * y

# 计算三角形面积
def tri(x, y):
    return x * y / 2

print('边长为10的正方形面积', square(10))
print('长10宽5的长方形面积', rec(10, 5), rec(5, 10))
print('低10高5的三角形面积', tri(10, 5), tri(5, 10))
