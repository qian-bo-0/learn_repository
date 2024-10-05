#随机模块的使用    random
'''
#1. 导入随即模块
import random
#2. 使用 random 模块调用 randint(a,b) 方法,会得到 a-b 之间的随机整数
num = random.randint(1,999)
#3. 输出查看随机数
print(num)
'''
'''
# 小游戏：石头 剪刀 布
# 先得到电脑输出一个数
import random
num = random.randint(1,3)
# 玩家输入招数
num2 = int(input('请输入你的招数（1：剪刀， 2：石头， 3：布）：'))
# 判断输赢
if (num2  == 1 and num == 3)or(num2 > num):
    print('你赢了电脑')
elif num2 = num:
    print('平局了，再来一次！')
else:
    print('嘿嘿，你输了！')
'''
'''
and 的优先级高于 or
'''


#循环
#while循环
#循环使用场景一：循还次数确定的循环
'''
    while 当。。。时
    死循环 ： while True:
'''
'''
#定义一个循环变量
#设置循环条件
#循环增量
i = 0
while i < 10:
    print('xxr是小狗')
    i += 1

'''
#循环的使用场景二：遍历循环变量
'''
#定义循环变量
#循环条件
#循环增量
i = 66
while i < 89:
    print(i)
    i += 1
'''
#循环的使用场景三：找出指定范围中复合特定条件的数
'''
#找出1 ~ 100之间的偶数
i = 1
while i <= 100:
    if i % 2 = 0:
        print(i,end = '\t')
    i += 1    
'''
#循环的使用场景四：求累加和 与 平均值
'''
#求出1-100之间的所有整数的累加和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
'''
#循环的使用场景五: 穷举
'''
#有一筐鸡蛋，两个两个数多一个，三个三个数多一个，四个四个数多一个，至少有几个？
eggs = 2
while True:       #不知道什么时候结束的循环就是死循环
    if eggs % 2 == 1 and eggs % 3 == 1 and eggs % 4 == 1:
        print(f'eggs = {eggs}')
        #条件一旦成立就应该跳出循环
        break
    eggs += 1
'''
#循环的使用场景六： 计数
'''
#统计 1 ~ 100 之间满足3倍数的数值有多少个
i = 1
num = 0
while i <= 100:
    if i % 3 == 0:
        num += 1
    i += 1
print(f'num = {num}')
'''


# 内置函数 range
'''
Python的内置函数 ： range(start, stop, step)
作用： 生成指定范围的序列。
while 循环像生成一个[1， 2， 3， 4， 5， ..., 10]
i = 1               start(默认为0)
while i <= 10:      stop (不包含，不含等于)
    i += 1          step(默认为1)
    print(i)
'''
'''
#生成一个 1 ~ 10的序列如下：
range(1,11,1)
'''
'''
#查看range()函数生成的序列的每个数值
#格式： for 循环变量 in range函数
for i in range(1,11,1):
    print(i,end = '\t')
'''
'''
# 用for循环求1 ~ 100 之间的整数累加和
sum = 0
for i in range(1,101,1):
    sum += i
print(f'sum = {sum}')
'''
'''
#打印出50个'-'
print('-' * 50)  
'''
'''
while和for的使用场景
    1.不知道循环次数的情况下
    2.for + range()在知道循环次数的情况下使用
'''
'''
#地球的自传与公转
count = 0
for i in range(1,2):
    for j in range(365):
        count += 1
print(f'地球公传{i}圈，自传{count}圈')
'''
'''
#小练习：打印一个5行5列的正方形:
for i in range(5):
    for j in range(5):
        print('*',end='\t')
    print('\n')
'''
'''
#小练习：输出一个直角三角形
for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print('\n')
'''
'''
#小练习：输出一个直角三角形
for i in range(5):
    for j in range(i):   #range()里是0时不会取值输出
        print('*',end=' ')
    print('\n')
'''
'''
#打印倒立的直角三角形
for i in range(5,0,-1):
    for j in range(i):
        print('*',end = ' ')
    print('\n')
'''


#循环控制流程语句（break,continue）
'''
#continue:结束本次循环继续下次循环
for i in range(10):
    #需求：当i = 5的时候不要输出
    if i == 5:
        continue
    print(i,end='\t')
'''


#else语句
'''
#需求： 用户输入密码,有三次机会，如果正确，登录成功，如果三次都输入错误，冻结此账户
for i in range(3):
    password = input('请输入密码:')
    if password == '666':
        print('登录成功')
        break
    else:
        print('密码错误，请重新输入！')
else:
    print('账户被冻结，请联系工作人员。')
    #else会进行的条件：循环执行完毕/循环条件为False，而不是遇到break
'''


#String类的驻留机制
'''
字符串的内存驻留机制：
相同的字符串在程序运行期间，其内存中仅存储一份。
说明：如何查看‘对象’在内存中的地址。      id(对象名)
说明：基本数据类型不需要考虑地址的问题，int float ~~~只有对象类型才需要考虑
作用：节省内存空间的开销
'''
'''
#驻留机制
s1 = 'python'
s2 = 'python'
s3 = 'python'
print(f's1 = {s1}, id(s1) = {id(s1)}')
print(f's2 = {s2}, id(s2) = {id(s2)}')
print(f's3 = {s3}, id(s3) = {id(s3)}')
'''


#字符串的切片
'''
切片： 将原来的字符串实现切割。
语法： [start:stop:step]
start : 开始默认为0
stop:   结束，默认不包含结尾
step:   默认为1
'''
'''
字符串是一个序列
例如：     h   e   l   l   o   ,   p   y   t   h   o   n
正下标是：  0   1   2   3   4   5   6   7   8   9   10  11
逆下标：   -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
下标也叫索引：index
逆向下标：从-1开始
'''
'''

'''
str = 'hello,python'
print(str[6])  #这不是切片，这是通过索引获取字符串中对应的字符，index=6
print(str[-6])  #一般我们不用逆向索引
print(str[6:12])#这是切片，从6开始切，切到12（不包含12） =>  python
print(str[0:5])#hello



























































