#基础数据类型
name = '你好'
'''
python中的数据类型：
Number数字:int、float、bool（True、False）
String字符串
Tuple元组
List列表
Set集合
Dictionary字典
'''
'''
#整型
num1 = 999
print(f'num1 = {num1}')   
#输出的固定格式. f -> format 格式化，特点就是在单引号字符串中可以书写{}
#大括号中能够放入‘变量名’，作用就是将变量名对应的’变量值‘输出
'''
'''
#查看变量的类型: type(变量名)
print(f'num1 = {num1},type(num1) = {type(num1)}')
'''
'''
#浮点型
num2 = 66.6
print(f'num2 = {num2},type(num2) = {type(num2)}')
'''
'''
#布尔型
is_visited = True   #变量名为被访问，结果为真，即为被访问过
print(f'is_visited = {is_visited},type(is_visited) = {type(is_visited)}')
'''
'''
#字符串类型
#三种书写类型：单引号、双引号、单引号
#好处：嵌套书写非常简单，不需要转义
#三引号常用于多行字符串
'''
name1 = '你好'
name2 = "你好"
name3 = '''你好'''
name4 = """你好"""


#python中的高级数据类型（存储多个数据的类型）
'''
#列表类型
#特点：有序、可重复、可扩展
names = ['张三','李四','王五','张三','李四']
print(f'names = {names},type(names) = {type(names)}')
'''
'''
#元组类型
#特点：有序、可重复、不可扩展
names = ('张三','李四','王五','张三','李四')
print(f'names = {names},type(names) = {type(names)}')
'''
'''
#集合类型
#特点：无序、不可重复、可扩展
#无序：内部是通过一套算法实现的，可能使用到了当前时间戳变量
names = {'张三','李四','王五','张三','李四'}
print(f'names = {names},type(names) = {type(names)}')
'''
'''
#字典类型
#key->value  键值对/夫妻
stu_dict = {'stu_id': '1001','name': '张三','age': 18,'score':100 }
print(f'stu_dict  = {stu_dict },type(stu_dict ) = {type(stu_dict )}')
'''









