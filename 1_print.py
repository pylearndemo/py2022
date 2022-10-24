# print
# print函数用于将指定内容输出到终端
# 终端的打开方式：点击VS Code左下角叉子和感叹号，
# 然后在出现的界面中点击终端
# 请注意，代码需要使用英语环境
# 因此，引号，逗号等符号需要使用英语符号
# 在写代码时，请设定英语输入法

# 输出字符串
# 字符串需要使用两个单引号或两个双引号引起来
print('Hello World!')
print("Hello World!")

# 如果字符串内有双引号或单引号，
# 那么需要用单引号或双引号引用字符串
print('Tom said, "Hi!"')
print("Tom said, 'Hi!'")
# 也可以使用反斜杠
print("Tom said, \"Hi\"")
# 反斜杠的其他使用
# 另起一行 \n
print('1\n2')
# tab \t
print('1\t2')

# 一对引号引起的字符串必须在同一行，不能换行
# 如果要换行，可以使用三对单引号或者三对双引号
print('''
Hello,
World!
''')
print("""
   *
  ***
 *****
*******
""")

# 输出数字
# 字符串和数字是两种基本类型
# 数字不需要用引号引起来
print(100)
# 如果数字用引号引起来，那么就是字符串类型，不是数字类型
print('100')
# 数字可用于加减乘除次方等运算
# 加号：+  减号：-  乘号：*  除号：/  次方：**
# print一次性可以打印多个值，用逗号隔开
print('1+1=', 1 + 1)
print('5-3=', 5 - 3)
print('2*2=', 2 * 2)
print('6/2=', 6 / 2)
print('2**2=', 2 ** 2)

# 更复杂的运算
print(10 ** 2 * 8 - 20 + 3 ** 10 / 10 - (5 -3))

# 字符串也可以用于“计算”
# +号代表拼接字符串
print('Hello ' + 'World!')
# *号代表重复
# 把字符串重复10遍
print('Hello' * 10)
