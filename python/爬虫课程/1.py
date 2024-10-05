# 爬虫： 通过编写程序来获取到互联网上的资源
#百度
#需求：用程序模拟浏览器，输入一个网址，从网址中获取到资源或者内容
#python搞定以上需求，特别简单
#1.导入一个包
from urllib.request import urlopen
#url  是和网址相关的一个库，在url中找到一个叫做request（请求）的库，在request中找到一个叫做urlopen（网址打开）的库

url = "http://www.baidu.com"
resp = urlopen(url)
#打开网址后返回一个结果叫做：response（resp）响应
#我们只想要得到响应的主体

# print(resp.read().decode("utf-8"))#这里需要decode()函数解码,具体的解码需求需要具体观察读取信息
with open("mybaidu.html",mode="w",encoding="utf--8") as f:#这里的encoding = "utf-8"是为了防止出现乱码
    f.write(resp.read().decode("utf-8"))
print("over")





























