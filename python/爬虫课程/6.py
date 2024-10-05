import requests
url = "https://movie.douban.com/j/chart/top_list"
#这里的参数太长，我需要重新封装参数
params = {
"type": "24",
"interval_id": "100:90",
"action": "",
"start": "0",
"limit": "20"
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
resp=requests.get(url,params=params,headers=headers)
#这里会直接进行扩充成原本的url，
print(resp.request.url)
print(resp.text)#这里运行出来什么都没有，遭到反爬阻截，需要一个一个尝试到底是什么原因
#遭到反爬，首先查看ua
print(resp.request.headers)
#{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#如上是默认的user-agent，需要修改headers
print(resp.json())

#上边的参数params中的start是页面刷新的参数，可以直接填写20，40，60等等，可以大规模获取刷新资源

resp.close()#关掉请求，防止访问次数过多容易报错










