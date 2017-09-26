# coding:utf-8
"""
python2 -m pip install pdfminer
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def convert_pdf_to_txt(fp):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    textstr = retstr.getvalue()
    retstr.close()
    return textstr

path = r'D:\admin\Pictures\1506410204362.pdf'
fp = file(path, 'rb')
text = convert_pdf_to_txt(fp)
dda = text.replace(r"", "")
dda = unicode(dda)
import re
pa = re.compile(r"\s{6,8}\d+\s{6}\d+\s{6}\S+")
dada = re.findall(pa, dda)
from collections import defaultdict
sk = defaultdict(lambda: 0)
for fd in dada:
    sk[fd.split()[2]] += 1
da2 = sorted(sk.iteritems(), key=lambda d: d[1], reverse=True)
for sxa in da2:
    print sxa[0], "  :  ", sxa[1]

"""
杭州摇号重名检测
摇了2年多，一直没戏
今天又发榜，还是没戏，把数据拉下来，简单处理，看看都是哪些人最容易摇到号码
后续会做分析，看看摇号到底有什么规则

以下是运行结果，截取重名最多的部分
李萍   :   4
王燕   :   4
王婷   :   4
李芳   :   3
李丹   :   3
李佳   :   3
张强   :   3
王洁   :   3
王辉   :   3
杨波   :   3
李琪   :   3
陈芳   :   3
沈雨婷   :   3
陈杰   :   3
王伟   :   3
周颖   :   3
冯俊   :   2
俞峰   :   2
陈军   :   2
张琦   :   2
黄英   :   2
杨平   :   2
孙磊   :   2
王萍   :   2
方华   :   2
孙科   :   2
王旭   :   2
黄杰   :   2
陈璐   :   2

嗯炸一看，果然短名字最容易摇到号。。
"""
