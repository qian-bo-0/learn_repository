#转义字符
r'''
#python解释器把字符串中的 \ 当成了一个字符，而不是寻址的反斜杠。错误写法：'D：\Games' 正确写法：r'D：\Games' 或 'D：\\Games'
#解决方法：1.在引号前加r   2.将\改为\\
\t    水平制表符（类似与四个空格）
\n    换行符
\     字符反斜杠
\r    回车
\b    退格
\'    单引号
\"    双引号
'''
'''
#print输出函数，默认会自动换行.
print('hello')           #默认end = '\n'
print('world')
print('hello',end = '')  #end = 空字符串
print('world')
print('hello',end = '\t')  
print('world')
'''


#.format()填充参数
'''
num1 = 10
num2 = 20
print('num1 = {0},num2 = {1}'.format(num1,num2))
#意思是把第0个变量填充到第0个位置，把第1个变量填充到第1个位置
'''


#数据类型转换
'''
int,str,float之间的转化比较常用
格式：
1.整型 int()
2.浮点型 float()
3.字符串类型 str()
'''
'''
#字符串类型转换为整型
num1 = '10'
num2 = '20'
result = num1 + num2
print(f'result = {result}')  #两个字符串相加结果就是相拼接
#网页中的输入框：input 标签 获取的数据都是字符串类型
n1 = int(num1)
n2 = int(num2)
result = n1 + n2
print('result = {0}'.format(result))
#整型相加就是数学相加
'''
'''
#浮点型转换为整型
f1 = 66.66
f2 = 88.88
result = f1 + f2
print(f'result = {result}')  #155.54
i1 = int(f1)
i2 = int(f2)
result = i1 + i2
print(f'result = {result}')  #154
#浮点型转换为整型是直接舍弃小数部分，保留整数部分
'''
'''
#整型转换为浮点型
i1 = 10
i2 = 20
f1 = float(i1)
f2 = float(i2)
result = f1 + f2
print(f'result = {result}') #30.0
'''
'''
#int + float
n = 10
f = 66.66
result = n + f
print(f'result = {result}') #76.66
#只要有浮点型参与运算，那么结果就是浮点型，要保证结果的精确性
'''


#input()
'''
    格式：
        input(提示信息)  该函数会返回用户在键盘中的输入的结果
        但是返回的类型都是str类型
        由于input()函数会返回结果，所以一定要定义一个变量来接收
        input()是一个阻塞函数，不输入就不会继续进行
'''
'''
#input()
name = input('请输入姓名。')
age = int(input('请输入年龄。'))
print('你的姓名是%s，年龄是%d岁'% (name,age))
'''


#算数运算符
'''
+ - * / // ** %
加、减、乘、除、整除,幂运算，取余
'''
'''
#复合赋值运算符：如果一个变量在自身的基础上发生改变，那么此时就可以使用复合赋值运算符
num1 = 10
num1 = num1 + 1
num1 += 1
print(f'num1 = {num1}')   
#复合赋值运算符：
'''


#逗号表达式
'''
#逗号表达式
#原理：元组解包
# num1, num2, num3 = 10, 20,30
num1, num2, num3 = (10,20,30)
#这里是正确的
num1, num2, num3 = (10,20,30,40)
#出现错误
#ValueError: too many values to unpack (expected 3)
#太多的值参与了解包过程
num1, num2, num3 = 10, 20, 30, 40
#同样的，这样也会报错
print(f'num1 = {num1},num2 = {num2},num3 = {num3}')
'''


#比较运算符
'''
<,>,<=,>=,==,!=
'''


#逻辑运算符
'''
and, or, not
'''


#if条件语句
'''
if 条件表达式：
    条件执行体
'''
'''
#输入出生年份，判断是否成年
year = int(input('请输入你的出生年份。'))
if (2024-year) < 18:
    print('你还未成年，不能观看这些视频')
'''
'''
if语句是一个整体，如果条件成立，整体就会被执行
'''
'''
#if语句的双分支结构
score = float(input('请输入你的考试成绩：'))
if score < 60:
    print('恭喜挂科')
else：
    print('恭喜及格')    
'''
'''
#if语句的多分支结构
score = float(input('请输入你的成绩：'))
if score < 30:
    print('欠揍')
elif score < 60:
    print('恭喜挂科')
else:
    print('恭喜及格')
'''
'''
一个条件一旦成立，剩下的语句就不会执行了
'''


#if实现三目运算
'''
    三目运算符： 其实就是 if...else...双分支结构的缩写形式
    格式：
           结果1 if 条件 else 结果2
    结果1 ： 条件成立时返回的结果
    结果2 ： 条件不成立时返回的结果
'''
'''
#使用三目运算符来实现三数字比较大小判断
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
num3 = int(input('请输入第三个数字：'))
second_max = num1 if num1 > num2 else num2
first_max = second_max if second_max > num3 else num3
print(first_max)
'''


























