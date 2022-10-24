# 列表
# 列表是一列有序的元素
# 有序代表着有顺序
# 元素可以各种各样的值，例如已经学习的数字和字符串
# 每个元素都有自己的位置
# 位置又叫下标，使用数字表示
# 需要注意的是，通常，代码是从0开始计数的
# 第一个元素的下标为0，第二个为1，以此类推

# 创建一个简单的列表
l = [1, 2, 3, 'hello', 'hi', 100]
print(l)
# 请注意，如果你将刚刚创建的列表l的
# 变量名——字母l——看成了数字1
# 并且没有产生任何疑惑，还照抄下来的话
# 说明你没有理解变量的命名规则
# 请查看前边课程的变量命名规则的说明

# 列表是用来存储数据的
# 列表创建后，需要对其进行一系列的操作才有意义
# 列表的操作有很多，总结起来就是增删改查

# 查询列表
# 查询下标为1的元素
print('下标为1的元素', l[1])
# 可以看到下标为1的元素是2，也就是列表的第二个元素
# 查询第一个元素
print('第一个元素', l[0])

# 切片
# 切片的意思就是查询某个区间的元素
# 例如，查询第2个到第4个元素
# 那么就要设置查询的起始位置和结束位置
# 注意，区间含头不含尾
# 即包含起始位置的元素，但是不包含结束位置的元素
print('第2到第4个元素', l[1:4])
# 起始和结束的下标用逗号隔开
# 第二个元素的下标为1，第4个元素的下标为3
# 因为含头不含尾，所以区间应该是1到4，即1:4

# 跳读
# 默认情况，查询一个区间的元素时，
# 会一个接着一个读取
# 但有时候，需要隔几个读一个
# 例如，想要隔两个读一个
print('从第1个到第5个隔2个读一个', l[0:5:2])
# 此时，读取区间为0:5，间隔设置为2，可以运行一下看看效果

# 更改
# 可以更改某个位置的值
# 更改第3个元素的值
l[2] = 99
print('更改第3个元素的值', l)

# 插入新的值
# 可以在某个位置插入新的值
# 第一个参数为下标，第二个参数为需要插入的值
# 在第4个位置插入999
l.insert(3, 999)
print('在第4个位置插入999', l)
# 在最后插入新的元素
l.append(66)
print('在最后插入新的元素', l)

# 删除
# 删除某个位置的值
# 删除第二个元素
# del为delete的前三个字母
del l[1]
print('删除第2个元素', l)

# 删除某个指定的元素
l.remove(999)
print('删除999', l)

# 如果指定的元素有多个
# 那么只会删除第一个
# 先插入多个一样的元素
l.insert(0, 88)
l.insert(0, 88)
l.insert(0, 88)
print('插入多个88', l)
# 此时删除88
l.remove(88)
print('删除88', l)

# 删除最后一个元素
# pop有弹出之意，即弹出最后一个
l.pop()
print('删除最后一个元素', l)

# 求列表的长度
# 使用python的内置函数，len
print('列表长度', len(l))

