import requests
from bs4 import BeautifulSoup
my_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}  #字典数据结构
response=requests.get("http://books.toscrape.com/",headers=my_headers)     #接受返回的响应体

#下面是获取数据阶段
print(response.status_code)  #打印状态码
if response.ok:
    content=response.text
    with open("./SPIDER_RESULT/book.html","w",encoding="utf-8") as f:    #写入本地文件
        f.write(content)
else:
    print("请求失败")

#下面是数据分析阶段
soup=BeautifulSoup(content,"html.parser")  #后面的参数是解析器,如果是html类型的网页就用这个解析器
#上面的Beautisoup将html内容解析成dom树的形式,便于我们分析
#举例:
print(f"这个html网页的第一个p元素的内容为:{soup.p}")

#接下来根据元素特征提取出书名,价格和图片元素
price_list=[]
book_list=[]
#图片
all_images=soup.findAll("img")   #因为图片没有干扰因素,所以直接提取就好
for image in all_images:
    print(image)

#价格
all_prices=soup.findAll("p",attrs={"class":"price_color"})    #价格元素在p元素中,但界面里太多p元素干扰,所以要用attrs筛选器,筛选其他特征,经过观察价格元素的类都是price_color
print("以下价格均为美元:")
for price in all_prices:
    print(price.string[2:])   #这个.string是把标签的其他内容忽略掉,只保留值.[2:]是切片操作,保留索引>=2的元素,这里的作用是把美元符号切了,只保留数字价格
    price_list.append(price.string[2:])

#书名
#这个不好直接找,经观察所有书名都是a元素,但有其他非书名a元素干扰,所以观察到所有书名a元素都是h3元素的子元素,所以思路是先选出所有h3元素,再找出里面所有a元素
#而a元素里的值是显示在网页上给用户看的值,如果书名过长会被...省略号替代,若要获取完整书名,经观察,我们可以不取a元素的值,而取其title属性的值
all_h3s=soup.findAll("h3")
for h3 in all_h3s:
    name=h3.find("a")['title']     #因为观察到每个h3元素里只会有一个书名a元素,所以我们直接用find找第一个,不用findAll了
    print(name)
    book_list.append(name)

dirc={}
for i in range(len(book_list)):
    dirc[book_list[i]]=price_list[i]

print(dirc)
for bookname,bookprice in dirc.items():
    print(f"书名:{bookname},价格:{bookprice},单位:美元")
