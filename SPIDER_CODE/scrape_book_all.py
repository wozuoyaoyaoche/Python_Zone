#之前的是爬取单页的,这个pro版本可以爬取50页,并且对之前的爬取做了封装函数处理
import requests
from bs4 import BeautifulSoup
my_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}  #字典数据结构

book_list=[]
price_list=[]

def price(page):
    all_prices=page.findAll("p",attrs={"class":"price_color"})    #价格元素在p元素中,但界面里太多p元素干扰,所以要用attrs筛选器,筛选其他特征,经过观察价格元素的类都是price_color
    print("以下价格均为美元:")
    for price in all_prices:
        print(price.string[2:])   #这个.string是把标签的其他内容忽略掉,只保留值.[2:]是切片操作,保留索引>=2的元素,这里的作用是把美元符号切了,只保留数字价格
        price_list.append(price.string[2:])

def book(page):
    all_h3s=page.findAll("h3")
    for h3 in all_h3s:
        name=h3.find("a")['title']     #因为观察到每个h3元素里只会有一个书名a元素,所以我们直接用find找第一个,不用findAll了
        print(name)
        book_list.append(name)

for i in range(1,5):
    print(f"正在爬取第{i}页")
    response=requests.get(f"http://books.toscrape.com/catalogue/page-{i}.html",headers=my_headers)
    if response.ok:
        content=response.text
        soup=BeautifulSoup(content,"html.parser")
        price(soup)
        book(soup)

    else:
        print(f"有错误,状态码为{response.status_code}")
    
dirc={}                                   #这里做个整合,把上面的书名和价格用键值对的形式汇总出来
for i in range(len(book_list)):
    dirc[book_list[i]]=price_list[i]

print(dirc)
for bookname,bookprice in dirc.items():   #.items函数把dirc返回一个[(key,value),(key,value)]形式的
    print(f"书名:{bookname},价格:{bookprice},单位:美元")


