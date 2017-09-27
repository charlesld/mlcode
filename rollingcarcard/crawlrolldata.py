#!/usr/bin/env python
# coding:utf-8
# 2017/9/27

import importlib
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument
from io import StringIO
from da import ROLLDATA
import re
from collections import defaultdict
import time

importlib.reload(sys)


def parse(url):
    # fp = open(url, 'rb')  # rb以二进制读模式打开本地pdf文件
    time.sleep(10)
    Resq = Req(getprfurl(url))
    praser_pdf = PDFParser(Resq.resp())
    doc = PDFDocument()
    praser_pdf.set_document(doc)
    doc.set_parser(praser_pdf)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        retstr = StringIO()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in doc.get_pages():
            interpreter.process_page(page)
            # layout = device.get_result()
            # for out in layout:
            #     if isinstance(out, LTTextBoxHorizontal):
            #         results = out.get_text()
            #         print(results)
        device.close()
        textstr = retstr.getvalue()
        retstr.close()
        return textstr


class Req(object):
    def __init__(self, url):
        self.url = url

    def resp(self):
        req = Request(self.url)
        req.add_header('User-Agent',
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36")
        response = urlopen(req)
        return response


def getprfurl(url):
    Resq = Req(url)
    bsobg = BeautifulSoup(Resq.resp(), "html.parser")
    ccasd = bsobg.find_all("a")
    for as1 in ccasd:
        if u"个人摇号指标配置结果" in as1.text:
            return as1.attrs["href"]


def write2file(content):
    with open("rolldata.txt", "a+") as wf:
        wf.write(content)
        wf.write("\n")


def parseresult(url):
    text = parse(url)
    dda = text.replace(r"", "")
    write2file(dda)


def getrest(file):
    pa = re.compile(r"\s{6,8}\d+\s{6}\d+\s{6}\S+")
    dd = open(file, "r")
    sk = defaultdict(lambda: 0)
    sklen = defaultdict(lambda: 0)
    sklen1w = defaultdict(lambda: 0)
    for i in range(212975):
        dda = dd.readline()
        dada = re.match(pa, dda)
        if dada != None:
            sk[dada.string.split()[2]] += 1
    da2 = sorted(sk.items(), key=lambda d: d[1], reverse=True)
    # print(da2)
    n = 0
    lifewinner = []
    for sxa in da2:
        namesot(sxa, sklen, True)
        n += 1
        if n <= 3000:
            namesot(sxa, sklen1w)
            lifewinner.append([sxa[0],sxa[1]])

    print("摇号总数命中：",sklen.items())
    print("高频命中：",sklen1w.items())
    print("人生赢家系列：",[i[0] for i in lifewinner[0:80]] )
    print("人生赢家系列：", [[i[1]] for i in lifewinner[0:80]] )


def namesot(round, sotname, flag=False):
    if len(round[0]) == 2:
        sotname[u"2名字中次数"] += 1
    elif len(round[0]) == 3:
        sotname[u"3名字中次数"] += 1
    elif len(round[0]) == 4:
        sotname[u"4名字中次数"] += 1
    else:
        if flag:
            # print(round[0])
            pass


def downloadalldata():
    num = len(ROLLDATA)
    for i in range(num):
        url = ROLLDATA[i][0]
        print("正在下载 %s " % ROLLDATA[i][1])
        parseresult(url)


if __name__ == '__main__':
    downloadalldata()
    getrest("rolldata.txt")
