# import requests
# query = input("请输入你要搜索的内容：")
# url = f"https://www.sogou.com/web?query={query}"
# dic = {
#    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
# }
# resp = requests.get(url,headers=dic)
# print(resp.text)


import requests
url = "https://fanyi.baidu.com/sug"
s = input("请输入你要翻译的英文:")
data = {
   "kw":s
}
resp = requests.post(url,data=data)
print(resp.json())


















