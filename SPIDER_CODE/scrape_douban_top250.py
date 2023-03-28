import requests
my_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}  #字典数据结构
response=requests.get("https://movie.douban.com/top250",headers=my_headers)

print(response)
print(response.status_code)
if response.ok:
    print(response.text)
    with open("./SPIDER_RESULT/douban_top250.html","w",encoding="utf-8") as f:
        f.write(response.text)
else:
    print("请求失败")