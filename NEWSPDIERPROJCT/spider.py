import os
import RULSEREADER
import ZHANGJIESQL
import guolu
import sqlconnter
import DOWNLOAD_IMG
import urllib.request
import time
import importlib
import sys
import ssl
from lxml import etree
import ZHENWENWRITER
importlib.reload(sys)  
ssl._create_default_https_context = ssl._create_unverified_context
RULES = RULSEREADER.RULESCONT()
get_url = urllib.request.Request(RULES[13])
get_url.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
HTMLX= urllib.request.urlopen(get_url).read().decode(RULES[9],'ignore')
index_html = etree.HTML(HTMLX)
net_url_list = index_html.xpath(RULES[0])
if RULES[10] =="ture" :
    for x in range(len(net_url_list)):
        net_url_list[x] = RULES[12]+net_url_list[x]
for y in net_url_list:
    print(y)
    get_urp = urllib.request.Request(y)
    get_urp.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    xinxiHTML= urllib.request.urlopen(get_urp).read().decode(RULES[9],'ignore')
    xinxi = etree.HTML(xinxiHTML)
    novelname = xinxi.xpath(RULES[1])[0]
    noveljianjie = xinxi.xpath(RULES[3])[0]
    novelwriter = xinxi.xpath(RULES[2])[0]
    novel_img = xinxi.xpath(RULES[4])[0]
    novelleixin = xinxi.xpath(RULES[5])[0]
    bianhao = "GANRO"+str(time.time())+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    bianhao =bianhao.replace(".","")
    update = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    print(novelname+"\n\n"+noveljianjie+"\n\n"+novelwriter+"\n\n"+novel_img+"\n\n"+novelleixin+"\n\n"+bianhao+"\n\n")
    sqlconnter.novelindexconnter(novelname,bianhao,novelleixin,update,novelwriter,noveljianjie,bianhao+".jpg",y,RULES[18],RULES[14],RULES[15],RULES[16])
    DOWNLOAD_IMG.IMG_DOWNLOAD(novel_img,bianhao)
    zhangjiename = xinxi.xpath(RULES[6])
    zhangjieurl = xinxi.xpath(RULES[7])
    if RULES[11] =="ture":
        for u in range(len(zhangjieurl)):
            zhangjieurl[u]=zhangjieurl[12]+zhangjieurl[u]
    os.system("mkdir "+os.getcwd()+"\\zhenwen"+"\\"+novelname)
    for h in range(len(zhangjieurl)):
        get_ury = urllib.request.Request(zhangjieurl[h])
        get_ury.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
        zhenwenHTML= urllib.request.urlopen(get_ury).read().decode(RULES[9],'ignore')
        zhenwen_HTML = etree.HTML(zhenwenHTML)
        zhenwen_x =""
        zhenwen = zhenwen_HTML.xpath(RULES[8])
        for k in range(len(zhenwen)):
            zhenwen_x = guolu.guolu(zhenwen_x+ zhenwen[k]+"\n")
        ZHENWENWRITER.Writer(zhenwen_x,zhangjiename[h],novelname)
        ZHANGJIESQL.zhangjiesqlWriter(RULES[14],RULES[15],RULES[16],zhangjiename[h],bianhao)
        print(zhangjiename[h]+"\n\n"+zhenwen_x+"\n\n")
        time.sleep(int(RULES[17]))