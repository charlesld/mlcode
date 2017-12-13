#coding:utf-8
#!/usr/bin/env python
#Created by Charles on 2017/12/13.


import  random

def gendata():
    dja = []
    for i in range(1,5):
        for ii in range(int(random.choice([str(iia) for iia in range(10)]))):
            ssa = "%s-%3s"%(i,random.randint(1,320))
            dja.append(ssa)

    dja.sort()
    return dja
    # print(dja)

def gengroup(dja):
    one,two,three,four = [],[],[],[]
    for ii in dja:
        kes = ii.split("-")
        if int(kes[0]) == 1:
            one.append(ii)
        elif int(kes[0]) ==2:
            two.append(ii)
        elif int(kes[0]) ==3:
            three.append(ii)
        elif int(kes[0]) ==4:
            four.append(ii)

    return [one,two,three,four]

    # print(one)
    # print(two)
    # print(three)
    # print(four)


def gentips(dja,bandwith):
    dt = gengroup(dja)
    lennum = 0
    for ii in dt:
        if len(ii) !=0:
            lennum+=1
    bandgroup = cas(lennum)
    print(bandgroup)
    if bandgroup == 0 :
        return None

    bandtips = {}

    groupnum = 0
    for ii in dt:
        print(groupnum)
        if len(ii)==0:
            # groupnum +=1
            print ("none level")
            continue
        # print("%s ...."%bandgroup[groupnum])
        baseband = bandgroup[groupnum]*bandwith*0.8
        # print("baseband",baseband)
        pid_group_band = cas(len(ii))
        pid_num = 0
        for pid_key in range(len(ii)):
            bandtips[ii[pid_key]] = baseband + bandwith*pid_group_band[pid_num]*bandgroup[groupnum]*0.2
            pid_num += 1
        groupnum+=1
    return bandtips



def cas(n):
    # 等差分配
    if n == 0 :
        return 0
    else:
        res = []
        na = 1/n
        for ii in range(1,n+1):
            res.append(ii*na)
        delta = sum(res)
        fina = []
        for ii in res:
            fina.append(ii/delta)
        return sorted(fina,reverse=True)

if __name__ == '__main__':
    ssa = gendata()
    # ssa = ["1-3"]
    # ssa = [[], [], [], ['4- 80', '4- 98', '4-128', '4-150', '4-183', '4-233']]
    print(gengroup(ssa))
    print(gentips(ssa,1500000))


