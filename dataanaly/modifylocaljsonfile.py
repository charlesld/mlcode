#coding:utf-8
#!/usr/bin/env python
#Created by Charles on 2017/11/21.\\\d
#修改JSON文件指定内容

srcuuid = "8999211293481sasdja"
dstuuid = "helloworld"
import json
def resoveJson(JsonData):

    f = open(JsonData,'r',encoding="utf-8")
    content = f.read()
    rlt = json.loads(content)
    return rlt

def searchUUIDandWrtite(JsonData,srcuuid,detuuid):

    for k,v in JsonData.items():
        print(k)

        search_dict(k,v,srcuuid,dstuuid,JsonData)

    savejsonfile("sa2.json",JsonData)


def savejsonfile(wrfile,jsondata):
    jsondata = json.dumps(jsondata)
    f = open(wrfile,'w')
    f.write(jsondata)

def search_dict(k,v,srcuuid,dstuuid,jsondata=None):
    if isinstance(v,list):
        for kk in v:
            search_dict(None,kk,srcuuid,dstuuid,kk)
    elif isinstance(v,dict):
        for kk in v.keys():
            search_dict(kk,v[kk],srcuuid,dstuuid,v)
    else:
        if k =='uidd' and v == srcuuid:
            print(k,v)
            jsondata[k] = dstuuid
            print("new :", k,jsondata[k])
        # print(k)





jsondata = resoveJson("sa.json")

searchUUIDandWrtite(jsondata,srcuuid,dstuuid)





# 输出
"""
aucctions
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
auctions
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
auctio1ns
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
auctionss
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
auctsions
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld
uidd 8999211293481sasdja
new : uidd helloworld

"""
