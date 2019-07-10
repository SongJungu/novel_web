import re
import os
def RULESCONT():
    def RulseReader(Rulesname):
        wenben = open(Rulesname,"r",encoding="utf-8").read()
        novel_name = re.findall("<novel_name>(.*?)</novel_name>",wenben)[0] # novelname
        next_url = re.findall("<next_url>(.*?)</next_url>",wenben)[0] # 索引URL
        novel_writer = re.findall("<novel_writer>(.*?)</novel_writer>",wenben)[0]# novelwriter
        novel_jianjie = re.findall("<novel_jianjie>(.*?)</novel_jianjie>",wenben)[0]#noveljianjie
        novel_leixin = re.findall("<novel_leixin>(.*?)</novel_leixin>",wenben)[0]#novel leixin
        novel_zhenwen = re.findall("<novel_zhenwen>(.*?)</novel_zhenwen>",wenben)[0]#novel zhenwen
        novel_zhangjieURLlist = re.findall("<novel_zhangjieURLlist>(.*?)</novel_zhangjieURLlist>",wenben)[0]#nvoelzhangjieurl
        novel_zhangjiename = re.findall("<novel_zhangjiename>(.*?)</novel_zhangjiename>",wenben)[0]#novel zhangjiename
        novel_img = re.findall("<novel_img>(.*?)</novel_img>",wenben)[0]#novel img url
        wenbianma = re.findall("<web_bianma>(.*?)</web_bianma>",wenben)[0] #wenbianma
        nethengcheng = re.findall("<NEXT_HECHENG>(.*?)</NEXT_HECHENG>",wenben)[0]#xiao shuo next hecheng
        zhanghecheng = re.findall("<ZhangjieURL_HECHENG>(.*?)</ZhangjieURL_HECHENG>",wenben)[0]
        HEURL = re.findall("<HECHENG_URL>(.*?)</HECHENG_URL>",wenben)[0]
        index_url = re.findall("<index_url>(.*?)</index_url>",wenben)[0]
        sql_mim = re.findall("<sql_mima>(.*?)</sql_mima>",wenben)[0]
        sql_zhanghao = re.findall("<sql_zhanghao>(.*?)</sql_zhanghao>",wenben)[0]
        sql_IP =re.findall("<sql_IP>(.*?)</sql_IP>",wenben)[0]
        sleep_time = re.findall("<sleep_time>(.*?)</sleep_time>",wenben)[0]
        Rules = [next_url,novel_name,novel_writer,novel_jianjie,novel_img,novel_leixin,novel_zhangjiename,novel_zhangjieURLlist,novel_zhenwen,wenbianma,nethengcheng,zhanghecheng,HEURL,index_url,sql_mim,sql_zhanghao,sql_IP,sleep_time]
    # 0 下个URL 1名字 2作者 3简介 4IMG——URL  5 类型 6 章名 7章URL 8 正W 9web编码 10小说信息页URL是否合成 11 章节URL是否合成 12需要合成进的URL 13开始爬取的初始URL 14 sql密码 15sql账号 16sql_IP 17睡眠时间 18规则名称
        return Rules
    print("扫描规则中....\n\n")
    wenjianname = os.listdir(os.getcwd())
    Ruleswenben =[]
    for i in range(len(wenjianname)):
        if wenjianname[i][-6:]==".ganro":
            Ruleswenben.append(wenjianname[i])
    if Ruleswenben == []:
        print("扫描无规则文件,如果有其它规则文件请输入名字:")
        shuru = input()
    else:
        for x in range(len(Ruleswenben)):
            print("输入"+str(x)+"  启动"+Ruleswenben[x]+"\n\n")
        shuru = input()
        for p in range(len(Ruleswenben)):
            if shuru == str(p):
                shuru = Ruleswenben[p]
    guize = RulseReader(shuru)
    print("\n\n成功读取规则!\n\n")
    for m in range(len(guize)):
        print(guize[m]+"\n")
    print("规则读取完毕，开始执行!>>>>>>>\n\n\n")
    guize.append(shuru)
    return guize


