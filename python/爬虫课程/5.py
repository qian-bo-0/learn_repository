import requests
url = "https://fanyi.baidu.com/sug"
s = input("请输入你要查找的单词：")
data = {
    "kw":s
}
#这里的kw在f12的负载里
#发送post请求，发送的数据必须放在字典中，通过data参数传递
resp = requests.post(url,data=data)
print(resp.text)#可能出现乱码，这是直接使用resp.json()将内容直接转换为json
print(resp.json())#将服务器返回的内容直接转换为json，也就是字典
























