#re模块
import re
#这里的findall是一个列表
list = re.findall(r"\d+","我的电话号码是：10086,我女朋友的电话是：10010")#正则表达式引号之前需要加上“r”，防止正则表达式被识别乘转义字符
#re.findall(正则形式，字符串)----->匹配字符串中所有复合正则的内容
print(list)

#finditer: 匹配字符串中的所有内容[返回的是迭代器]
it = re.finditer(r"\d+","我的电话号码是：10086,我女朋友的电话是：10010")
#<callable_iterator object at 0x0000013E58EC3220>    这个是结果
#从迭代器中提取
for i in it:
    print(i.group())
#通过group()函数可以拿到我们要查找的字符串
#迭代器的效率要远高于列表
print(it)

#search找到一个结果就返回，返回的结果是match对象，拿数据需要group(),search是全文匹配
s = re.search(r"\d+","我的电话号码是：10086,我女朋友的电话是：10010")
print(s.group())
#这里只能查找出10086，查不出10010

#match是从头开始匹配，可以认为默认在正则前加了^
s = re.match(r"\d+","10086,我女朋友的电话是：10010")
print(s.group())

#预加载正则表达式
obj = re.compile(r"\d+")#缓存预加载，可以反复使用
rep = obj.finditer("我的电话号码是：10086,我女朋友的电话是：10010")
for i in rep:
    print(i.group())
i = obj.findall("赶紧还我1000000")
print(i)


#
s = ("""
<div class='gan'><span id='2'>西游记</span></div>
<div class='ban'><span id='3'>西游记</span></div>
<div class='nan'><span id='1'>西游记</span></div>
""")
obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)
#re.S: 让.能匹配换行符（）
result = obj.finditer(s)
for i in result:
    print(i.group())#这里的结果和字符串s是一样的

#(?P<分组名字>正则)    可以单独的从正则匹配的内容中进一步提取内容
#但我想要提取出我匹配出字符的一部分内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)
#这里的变动是将()中的.*?匹配的内容放到<wahaha>里去
result = obj.finditer(s)
for i in result:
    print(i.group("wahaha"))
    print(i.group("id"))



























