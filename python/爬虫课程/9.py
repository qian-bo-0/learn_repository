#拿到页面源代码
#通过re来提取想要的有效信息
import requests
import re
url = "https://movie.douban.com/top250"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
resp = requests.get(url,headers=headers)
print(resp.text)
page_content = resp.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">'
                 r'.*?<br>(?P<year>.*?)&nbsp',re.S)
#开始匹配
result = obj.finditer(page_content)
for i in result:
    print(i.group("name"))
    print(i.group("year".strip()))



















