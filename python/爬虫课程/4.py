# 安装requests
#pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple requests
import requests

query = input("请输入你要搜索的内容：")


url = f"https://www.sogou.com/web?query={query}"
#浏览器地址栏里的链接都是使用的是get的请求

dic = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头里的ua，定义成字典形式
resp=requests.get(url,headers=dic )#处理了一个反爬

print(resp)     #<Response [200]>响应状态正常
print(resp.text)#拿到页面源代码
#这里缺少请求头里的user agent，可能会出现反爬拦截，服务器认为我们是爬虫程序






































