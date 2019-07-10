from django.shortcuts import render
import time
import os
import novelweb.zhenwenSQLREADER
import novelweb.mysqlsearch
def firstdate(request):
#    novelname =[]
 #   imgname = []
#    zhuantiao =[]

 #   BIANHAO  = novelweb.mysqlsearch.test("select distinct novel_bianhao from novel_index;")

#    for y in BIANHAO:
 #       zhuantiao.append("/novel_xinxi?bianhao="+y)
 #       novelname.append(novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+y+'";')[0])
  #      imgname.append(novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+y+'";')[0])
    context  = {}
    try:
        active_imgname = novelweb.mysqlsearch.test("select distinct active_imgname from active;")
        acitve_novelname =  novelweb.mysqlsearch.test("select distinct active_novelname from active;")
    except:
        pass
    try :
        acitve_novelname1 =acitve_novelname[0]
        acitve_imgpath1 = "/static/web_img/"+active_imgname[0]
        acitve_novelBIANHAO1 = novelweb.mysqlsearch.test('select novel_bianhao from novel_index where novel_name="'+acitve_novelname[0]+'";')[0]
        ACTIVE_novelget_URL1 = "/novel_xinxi?bianhao="+acitve_novelBIANHAO1
    except :
        acitve_novelname1 ="#"
        acitve_imgpath1 = "/static/web_img/not_active.png"
        ACTIVE_novelget_URL1 = "#"
    context['acitve_novelname1'] = acitve_novelname1
    context['active_img1'] = acitve_imgpath1
    context['active_getURL1'] = ACTIVE_novelget_URL1
############################
    try :
        acitve_novelname2 = acitve_novelname[1]
        acitve_imgpath2 = "/static/web_img/"+active_imgname[1]
        acitve_novelBIANHAO2 = novelweb.mysqlsearch.test('select novel_bianhao from novel_index where novel_name="'+acitve_novelname[1]+'";')[0]
        ACTIVE_novelget_URL2 = "/novel_xinxi?bianhao="+acitve_novelBIANHAO2
    except :
        acitve_novelname2 = "#"
        acitve_imgpath2 = "/static/web_img/not_active.png"
        ACTIVE_novelget_URL2 = "#"
    context['acitve_novelname2'] = acitve_novelname2
    context['active_img2'] = acitve_imgpath2
    context['active_getURL2'] = ACTIVE_novelget_URL2

###########################
    try :
        acitve_novelname3 = acitve_novelname[2]
        acitve_imgpath3 = "/static/web_img/"+active_imgname[2]
        acitve_novelBIANHAO3 = novelweb.mysqlsearch.test('select novel_bianhao from novel_index where novel_name="'+acitve_novelname[2]+'";')[0]
        ACTIVE_novelget_URL3 = "/novel_xinxi?bianhao="+acitve_novelBIANHAO3
    except :
        acitve_novelname3 = "#"
        acitve_imgpath3 = "/static/web_img/not_active.png"
        ACTIVE_novelget_URL3 = "#"
    context['acitve_novelname3'] = acitve_novelname3
    context['active_img3'] = acitve_imgpath3
    context['active_getURL3'] = ACTIVE_novelget_URL3

##########################
    try :
        acitve_novelname4 = acitve_novelname[3]
        acitve_imgpath4 = "/static/web_img/"+active_imgname[3]
        acitve_novelBIANHAO4 = novelweb.mysqlsearch.test('select novel_bianhao from novel_index where novel_name="'+acitve_novelname[3]+'";')[0]
        ACTIVE_novelget_URL4 = "/novel_xinxi?bianhao="+acitve_novelBIANHAO4
    except :
        acitve_novelname4 = "#"
        acitve_imgpath4 = "/static/web_img/not_active.png"
        ACTIVE_novelget_URL4 = "#"
    context['acitve_novelname4'] = acitve_novelname4
    context['active_img4'] = acitve_imgpath4
    context['active_getURL4'] = ACTIVE_novelget_URL4

    ###########
    try:
        bianjihao  = novelweb.mysqlsearch.test("select distinct bianhao from lijian;")
    except:
        pass
    try:
        bianji_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+bianjihao[0]+'";')[0]
        bianji_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+bianjihao[0]+'";')[0]
        bianji_jianjie1 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+bianjihao[0]+'";')[0]
        bianji_url1 = "/novel_xinxi?bianhao="+bianjihao[0]
        bianji_leixin1 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+bianjihao[0]+'";')[0]
    except:
        bianji_name1 = "待写入..."
        bianji_img1 = "/static/web_img/notbook.png"
        bianji_jianjie1 = "待写入..."
        bianji_leixin1 = "待写入..."
        bianji_url1 = "#"
    context['bianji_nameTJ1'] =bianji_name1
    context['bianji_imgTJ1'] = bianji_img1
    context['bianji_jianjieTJ1'] = bianji_jianjie1
    context['bianji_leixinTJ1'] = bianji_leixin1
    context['bianji_urlTJ1'] = bianji_url1

    try:
        bianji_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+bianjihao[1]+'";')[0]
        bianji_img2 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+bianjihao[1]+'";')[0]
        bianji_jianjie2 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+bianjihao[1]+'";')[0]
        bianji_url2 = "/novel_xinxi?bianhao="+bianjihao[1]
        bianji_leixin2 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+bianjihao[1]+'";')[0]
    except:
        bianji_name2 = "待写入..."
        bianji_img2 = "/static/web_img/notbook.png"
        bianji_jianjie2 = "待写入..."
        bianji_leixin2 = "待写入..."
        bianji_url2 = "#"
    context['bianji_nameTJ2'] =bianji_name2
    context['bianji_imgTJ2'] = bianji_img2
    context['bianji_jianjieTJ2'] = bianji_jianjie2
    context['bianji_leixinTJ2'] = bianji_leixin2
    context['bianji_urlTJ2'] = bianji_url2

    try:
        bianji_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+bianjihao[2]+'";')[0]
        bianji_img3 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+bianjihao[2]+'";')[0]
        bianji_jianjie3 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+bianjihao[2]+'";')[0]
        bianji_url3 = "/novel_xinxi?bianhao="+bianjihao[2]
        bianji_leixin3 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+bianjihao[2]+'";')[0]
    except:
        bianji_name3 = "待写入..."
        bianji_img3 = "/static/web_img/notbook.png"
        bianji_jianjie3 = "待写入..."
        bianji_leixin3 = "待写入..."
        bianji_url3 = "#"
    context['bianji_nameTJ3'] =bianji_name3
    context['bianji_imgTJ3'] = bianji_img3
    context['bianji_jianjieTJ3'] = bianji_jianjie3
    context['bianji_leixinTJ3'] = bianji_leixin3
    context['bianji_urlTJ3'] = bianji_url3
##########################

    try :
        boy_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from boylike;")
    except:
        pass
    try:
        boy_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[0]+'";')[0]
        boy_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[0]+'";')[0]
        boy_url1 = "/novel_xinxi?bianhao="+boy_bianhao[0]
    except:
        boy_name1 = "待写入..."
        boy_img1 = "/static/web_img/notbook.png"
        boy_url1 =  "#"
    context['boy_name1'] = boy_name1
    context['boy_img1'] = boy_img1
    context['boy_url1'] = boy_url1


    try:
        boy_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[1]+'";')[0]
        boy_img2 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[1]+'";')[0]
        boy_url2 = "/novel_xinxi?bianhao="+boy_bianhao[1]
    except:
        boy_name2 = "待写入..."
        boy_img2 = "/static/web_img/notbook.png"
        boy_url2 =  "#"
    context['boy_name2'] = boy_name2
    context['boy_img2'] = boy_img2
    context['boy_url2'] = boy_url2



    try:
        boy_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[2]+'";')[0]
        boy_img3 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[2]+'";')[0]
        boy_url3 = "/novel_xinxi?bianhao="+boy_bianhao[2]
    except:
        boy_name3 = "待写入..."
        boy_img3 = "/static/web_img/notbook.png"
        boy_url3 =  "#"
    context['boy_name3'] = boy_name3
    context['boy_img3'] = boy_img3
    context['boy_url3'] = boy_url3



    try:
        boy_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[3]+'";')[0]
        boy_img4 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[3]+'";')[0]
        boy_url4 = "/novel_xinxi?bianhao="+boy_bianhao[3]
    except:
        boy_name4 = "待写入..."
        boy_img4 = "/static/web_img/notbook.png"
        boy_url4 =  "#"
    context['boy_name4'] = boy_name4
    context['boy_img4'] = boy_img4
    context['boy_url4'] = boy_url4



    try:
        boy_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[4]+'";')[0]
        boy_img5 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[4]+'";')[0]
        boy_url5 = "/novel_xinxi?bianhao="+boy_bianhao[4]
    except:
        boy_name5 = "待写入..."
        boy_img5 = "/static/web_img/notbook.png"
        boy_url5 =  "#"
    context['boy_name5'] = boy_name5
    context['boy_img5'] = boy_img5
    context['boy_url5'] = boy_url5



    try:
        boy_name6 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+boy_bianhao[5]+'";')[0]
        boy_img6 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+boy_bianhao[5]+'";')[0]
        boy_url6 = "/novel_xinxi?bianhao="+boy_bianhao[5]
    except:
        boy_name6 = "待写入..."
        boy_img6 = "/static/web_img/notbook.png"
        boy_url6 =  "#"
    context['boy_name6'] = boy_name6
    context['boy_img6'] = boy_img6
    context['boy_url6'] = boy_url6



#############
    try :
        girl_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from girllike;")
    except:
        pass

    try:
        girl_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[0]+'";')[0]
        girl_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[0]+'";')[0]
        girl_url1 = "/novel_xinxi?bianhao="+girl_bianhao[0]
    except:
        girl_name1 = "待写入..."
        girl_img1 = "/static/web_img/notbook.png"
        girl_url1 =  "#"
    context['girl_name1'] = girl_name1
    context['girl_img1'] = girl_img1
    context['girl_url1'] = girl_url1



    try:
        girl_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[1]+'";')[0]
        girl_img2 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[1]+'";')[0]
        girl_url2 = "/novel_xinxi?bianhao="+girl_bianhao[1]
    except:
        girl_name2 = "待写入..."
        girl_img2 = "/static/web_img/notbook.png"
        girl_url2 =  "#"
    context['girl_name2'] = girl_name2
    context['girl_img2'] = girl_img2
    context['girl_url2'] = girl_url2



    try:
        girl_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[2]+'";')[0]
        girl_img3 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[2]+'";')[0]
        girl_url3 = "/novel_xinxi?bianhao="+girl_bianhao[2]
    except:
        girl_name3 = "待写入..."
        girl_img3 = "/static/web_img/notbook.png"
        girl_url3 =  "#"
    context['girl_name3'] = girl_name3
    context['girl_img3'] = girl_img3
    context['girl_url3'] = girl_url3



    try:
        girl_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[3]+'";')[0]
        girl_img4 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[3]+'";')[0]
        girl_url4 = "/novel_xinxi?bianhao="+girl_bianhao[3]
    except:
        girl_name4 = "待写入..."
        girl_img4 = "/static/web_img/notbook.png"
        girl_url4 =  "#"
    context['girl_name4'] = girl_name4
    context['girl_img4'] = girl_img4
    context['girl_url4'] = girl_url4



    try:
        girl_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[4]+'";')[0]
        girl_img5 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[4]+'";')[0]
        girl_url5 = "/novel_xinxi?bianhao="+girl_bianhao[4]
    except:
        girl_name5 = "待写入..."
        girl_img5 = "/static/web_img/notbook.png"
        girl_url5 =  "#"
    context['girl_name5'] = girl_name5
    context['girl_img5'] = girl_img5
    context['girl_url5'] = girl_url5



    try:
        girl_name6 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+girl_bianhao[5]+'";')[0]
        girl_img6 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+girl_bianhao[5]+'";')[0]
        girl_url6 = "/novel_xinxi?bianhao="+girl_bianhao[5]
    except:
        girl_name6 = "待写入..."
        girl_img6 = "/static/web_img/notbook.png"
        girl_url6 =  "#"
    context['girl_name6'] = girl_name6
    context['girl_img6'] = girl_img6
    context['girl_url6'] = girl_url6


################################
    try :
        newbookTJ_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from newbookTJ;")
    except:
        pass
    try:
        newbookTJ_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[0]+'";')[0]
        newbookTJ_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[0]+'";')[0]
        newbookTJ_url1 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[0]
    except:
        newbookTJ_name1 = "待写入..."
        newbookTJ_img1 = "/static/web_img/notbook.png"
        newbookTJ_url1 =  "#"
    context['newbookTJ_name1'] = newbookTJ_name1
    context['newbookTJ_img1'] = newbookTJ_img1
    context['newbookTJ_url1'] = newbookTJ_url1



    try:
        newbookTJ_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[1]+'";')[0]
        newbookTJ_img2 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[1]+'";')[0]
        newbookTJ_url2 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[1]
    except:
        newbookTJ_name2 = "待写入..."
        newbookTJ_img2 = "/static/web_img/notbook.png"
        newbookTJ_url2 =  "#"
    context['newbookTJ_name2'] = newbookTJ_name2
    context['newbookTJ_img2'] = newbookTJ_img2
    context['newbookTJ_url2'] = newbookTJ_url2



    try:
        newbookTJ_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[2]+'";')[0]
        newbookTJ_img3 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[2]+'";')[0]
        newbookTJ_url3 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[2]
    except:
        newbookTJ_name3 = "待写入..."
        newbookTJ_img3 = "/static/web_img/notbook.png"
        newbookTJ_url3 =  "#"
    context['newbookTJ_name3'] = newbookTJ_name3
    context['newbookTJ_img3'] = newbookTJ_img3
    context['newbookTJ_url3'] = newbookTJ_url3



    try:
        newbookTJ_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[3]+'";')[0]
        newbookTJ_img4 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[3]+'";')[0]
        newbookTJ_url4 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[3]
    except:
        newbookTJ_name4 = "待写入..."
        newbookTJ_img4 = "/static/web_img/notbook.png"
        newbookTJ_url4 =  "#"
    context['newbookTJ_name4'] = newbookTJ_name4
    context['newbookTJ_img4'] = newbookTJ_img4
    context['newbookTJ_url4'] = newbookTJ_url4



    try:
        newbookTJ_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[4]+'";')[0]
        newbookTJ_img5 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[4]+'";')[0]
        newbookTJ_url5 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[4]
    except:
        newbookTJ_name5 = "待写入..."
        newbookTJ_img5 = "/static/web_img/notbook.png"
        newbookTJ_url5 =  "#"
    context['newbookTJ_name5'] = newbookTJ_name5
    context['newbookTJ_img5'] = newbookTJ_img5
    context['newbookTJ_url5'] = newbookTJ_url5



    try:
        newbookTJ_name6 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+newbookTJ_bianhao[5]+'";')[0]
        newbookTJ_img6 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+newbookTJ_bianhao[5]+'";')[0]
        newbookTJ_url6 = "/novel_xinxi?bianhao="+newbookTJ_bianhao[5]
    except:
        newbookTJ_name6 = "待写入..."
        newbookTJ_img6 = "/static/web_img/notbook.png"
        newbookTJ_url6 =  "#"
    context['newbookTJ_name6'] = newbookTJ_name6
    context['newbookTJ_img6'] = newbookTJ_img6
    context['newbookTJ_url6'] = newbookTJ_url6

#########################

    try :
        wanbenTJ_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from wanbenTJ;")
    except:
        pass
    try:
        wanbenTJ_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+wanbenTJ_bianhao[0]+'";')[0]
        wanbenTJ_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+wanbenTJ_bianhao[0]+'";')[0]
        wanbenTJ_url1 = "/novel_xinxi?bianhao="+wanbenTJ_bianhao[0]
    except:
        wanbenTJ_name1 = "待写入..."
        wanbenTJ_img1 = "/static/web_img/notbook.png"
        wanbenTJ_url1 =  "#"
    context['wanbenTJ_name1'] = wanbenTJ_name1
    context['wanbenTJ_img1'] = wanbenTJ_img1
    context['wanbenTJ_url1'] = wanbenTJ_url1



    try:
        wanbenTJ_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+wanbenTJ_bianhao[1]+'";')[0]
        wanbenTJ_img2 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+wanbenTJ_bianhao[1]+'";')[0]
        wanbenTJ_url2 = "/novel_xinxi?bianhao="+wanbenTJ_bianhao[1]
    except:
        wanbenTJ_name2 = "待写入..."
        wanbenTJ_img2 = "/static/web_img/notbook.png"
        wanbenTJ_url2 =  "#"
    context['wanbenTJ_name2'] = wanbenTJ_name2
    context['wanbenTJ_img2'] = wanbenTJ_img2
    context['wanbenTJ_url2'] = wanbenTJ_url2



    try:
        wanbenTJ_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+wanbenTJ_bianhao[2]+'";')[0]
        wanbenTJ_img3 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+wanbenTJ_bianhao[2]+'";')[0]
        wanbenTJ_url3 = "/novel_xinxi?bianhao="+wanbenTJ_bianhao[2]
    except:
        wanbenTJ_name3 = "待写入..."
        wanbenTJ_img3 = "/static/web_img/notbook.png"
        wanbenTJ_url3 =  "#"
    context['wanbenTJ_name3'] = wanbenTJ_name3
    context['wanbenTJ_img3'] = wanbenTJ_img3
    context['wanbenTJ_url3'] = wanbenTJ_url3

########################################################

    try:
       xuanhuanTJ_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from xuanhuanTJ;")
    except:
        pass
    try:
        xuanhuanTJ_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[0]+'";')[0]
        xuanhuanTJ_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[0]+'";')[0]
        xuanhuanTJ_jianjie1 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[0]+'";')[0]
        xuanhuanTJ_url1 = "/novel_xinxi?bianhao="+xuanhuanTJ_bianhao[0]
        xuanhuanTJ_leixin1 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[0]+'";')[0]
    except:
        xuanhuanTJ_name1 = "待写入..."
        xuanhuanTJ_img1 = "/static/web_img/notbook.png"
        xuanhuanTJ_jianjie1 = "待写入..."
        xuanhuanTJ_leixin1 = "待写入..."
        xuanhuanTJ_url1 = "#"
    context['xuanhuanTJ_name1'] =xuanhuanTJ_name1
    context['xuanhuanTJ_img1'] = xuanhuanTJ_img1
    context['xuanhuanTJ_jianjie1'] = xuanhuanTJ_jianjie1
    context['xuanhuanTJ_leixin1'] = xuanhuanTJ_leixin1
    context['xuanhuanTJ_url1'] = xuanhuanTJ_url1

    try:
        xuanhuanTJ_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[1]+'";')[0]
        xuanhuanTJ_leixin2 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[1]+'";')[0]
        xuanhuanTJ_url2 = "/novel_xinxi?bianhao="+xuanhuanTJ_bianhao[1]
    except:
        xuanhuanTJ_name2 = "待写入..."
        xuanhuanTJ_leixin2 = "待写入..."
        xuanhuanTJ_url2 = "#"
    context['xuanhuanTJ_name2'] =xuanhuanTJ_name2
    context['xuanhuanTJ_leixin2'] = xuanhuanTJ_leixin2
    context['xuanhuanTJ_url2'] = xuanhuanTJ_url2

    try:
        xuanhuanTJ_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[2]+'";')[0]
        xuanhuanTJ_leixin3 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[2]+'";')[0]
        xuanhuanTJ_url3 = "/novel_xinxi?bianhao="+xuanhuanTJ_bianhao[2]
    except:
        xuanhuanTJ_name3 = "待写入..."
        xuanhuanTJ_leixin3 = "待写入..."
        xuanhuanTJ_url3 = "#"
    context['xuanhuanTJ_name3'] =xuanhuanTJ_name3
    context['xuanhuanTJ_leixin3'] = xuanhuanTJ_leixin3
    context['xuanhuanTJ_url3'] = xuanhuanTJ_url3
    try:
        xuanhuanTJ_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[3]+'";')[0]
        xuanhuanTJ_leixin4 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[3]+'";')[0]
        xuanhuanTJ_url4 = "/novel_xinxi?bianhao="+xuanhuanTJ_bianhao[3]
    except:
        xuanhuanTJ_name4 = "待写入..."
        xuanhuanTJ_leixin4 = "待写入..."
        xuanhuanTJ_url4 = "#"
    context['xuanhuanTJ_name4'] =xuanhuanTJ_name4
    context['xuanhuanTJ_leixin4'] = xuanhuanTJ_leixin4
    context['xuanhuanTJ_url4'] = xuanhuanTJ_url4

    try:
        xuanhuanTJ_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[4]+'";')[0]
        xuanhuanTJ_leixin5 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+xuanhuanTJ_bianhao[4]+'";')[0]
        xuanhuanTJ_url5 = "/novel_xinxi?bianhao="+xuanhuanTJ_bianhao[4]
    except:
        xuanhuanTJ_name5 = "待写入..."
        xuanhuanTJ_leixin5 = "待写入..."
        xuanhuanTJ_url5 = "#"
    context['xuanhuanTJ_name5'] =xuanhuanTJ_name5
    context['xuanhuanTJ_leixin5'] = xuanhuanTJ_leixin5
    context['xuanhuanTJ_url5'] = xuanhuanTJ_url5
####################################

    try:
       dushiTJ_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from dushiTJ;")
    except:
        pass
    try:
        dushiTJ_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+dushiTJ_bianhao[0]+'";')[0]
        dushiTJ_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+dushiTJ_bianhao[0]+'";')[0]
        dushiTJ_jianjie1 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+dushiTJ_bianhao[0]+'";')[0]
        dushiTJ_url1 = "/novel_xinxi?bianhao="+dushiTJ_bianhao[0]
        dushiTJ_leixin1 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+dushiTJ_bianhao[0]+'";')[0]
    except:
        dushiTJ_name1 = "待写入..."
        dushiTJ_img1 = "/static/web_img/notbook.png"
        dushiTJ_jianjie1 = "待写入..."
        dushiTJ_leixin1 = "待写入..."
        dushiTJ_url1 = "#"
    context['dushiTJ_name1'] =dushiTJ_name1
    context['dushiTJ_img1'] = dushiTJ_img1
    context['dushiTJ_jianjie1'] = dushiTJ_jianjie1
    context['dushiTJ_leixin1'] = dushiTJ_leixin1
    context['dushiTJ_url1'] = dushiTJ_url1

    try:
        dushiTJ_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+dushiTJ_bianhao[1]+'";')[0]
        dushiTJ_leixin2 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+dushiTJ_bianhao[1]+'";')[0]
        dushiTJ_url2 = "/novel_xinxi?bianhao="+dushiTJ_bianhao[1]
    except:
        dushiTJ_name2 = "待写入..."
        dushiTJ_leixin2 = "待写入..."
        dushiTJ_url2 = "#"
    context['dushiTJ_name2'] =dushiTJ_name2
    context['dushiTJ_leixin2'] = dushiTJ_leixin2
    context['dushiTJ_url2'] = dushiTJ_url2

    try:
        dushiTJ_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+dushiTJ_bianhao[2]+'";')[0]
        dushiTJ_leixin3 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+dushiTJ_bianhao[2]+'";')[0]
        dushiTJ_url3 = "/novel_xinxi?bianhao="+dushiTJ_bianhao[2]
    except:
        dushiTJ_name3 = "待写入..."
        dushiTJ_leixin3 = "待写入..."
        dushiTJ_url3 = "#"
    context['dushiTJ_name3'] =dushiTJ_name3
    context['dushiTJ_leixin3'] = dushiTJ_leixin3
    context['dushiTJ_url3'] = dushiTJ_url3
    try:
        dushiTJ_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+dushiTJ_bianhao[3]+'";')[0]
        dushiTJ_leixin4 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+dushiTJ_bianhao[3]+'";')[0]
        dushiTJ_url4 = "/novel_xinxi?bianhao="+dushiTJ_bianhao[3]
    except:
        dushiTJ_name4 = "待写入..."
        dushiTJ_leixin4 = "待写入..."
        dushiTJ_url4 = "#"
    context['dushiTJ_name4'] =dushiTJ_name4
    context['dushiTJ_leixin4'] = dushiTJ_leixin4
    context['dushiTJ_url4'] = dushiTJ_url4

    try:
        dushiTJ_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+dushiTJ_bianhao[4]+'";')[0]
        dushiTJ_leixin5 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+dushiTJ_bianhao[4]+'";')[0]
        dushiTJ_url5 = "/novel_xinxi?bianhao="+dushiTJ_bianhao[4]
    except:
        dushiTJ_name5 = "待写入..."
        dushiTJ_leixin5 = "待写入..."
        dushiTJ_url5 = "#"
    context['dushiTJ_name5'] =dushiTJ_name5
    context['dushiTJ_leixin5'] = dushiTJ_leixin5
    context['dushiTJ_url5'] = dushiTJ_url5

#########################################

    try:
       kehuanTJ_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from kehuanTJ;")
    except:
        pass
    try:
        kehuanTJ_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+kehuanTJ_bianhao[0]+'";')[0]
        kehuanTJ_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+kehuanTJ_bianhao[0]+'";')[0]
        kehuanTJ_jianjie1 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+kehuanTJ_bianhao[0]+'";')[0]
        kehuanTJ_url1 = "/novel_xinxi?bianhao="+kehuanTJ_bianhao[0]
        kehuanTJ_leixin1 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+kehuanTJ_bianhao[0]+'";')[0]
    except:
        kehuanTJ_name1 = "待写入..."
        kehuanTJ_img1 = "/static/web_img/notbook.png"
        kehuanTJ_jianjie1 = "待写入..."
        kehuanTJ_leixin1 = "待写入..."
        kehuanTJ_url1 = "#"
    context['kehuanTJ_name1'] =kehuanTJ_name1
    context['kehuanTJ_img1'] = kehuanTJ_img1
    context['kehuanTJ_jianjie1'] = kehuanTJ_jianjie1
    context['kehuanTJ_leixin1'] = kehuanTJ_leixin1
    context['kehuanTJ_url1'] = kehuanTJ_url1

    try:
        kehuanTJ_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+kehuanTJ_bianhao[1]+'";')[0]
        kehuanTJ_leixin2 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+kehuanTJ_bianhao[1]+'";')[0]
        kehuanTJ_url2 = "/novel_xinxi?bianhao="+kehuanTJ_bianhao[1]
    except:
        kehuanTJ_name2 = "待写入..."
        kehuanTJ_leixin2 = "待写入..."
        kehuanTJ_url2 = "#"
    context['kehuanTJ_name2'] =kehuanTJ_name2
    context['kehuanTJ_leixin2'] = kehuanTJ_leixin2
    context['kehuanTJ_url2'] = kehuanTJ_url2

    try:
        kehuanTJ_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+kehuanTJ_bianhao[2]+'";')[0]
        kehuanTJ_leixin3 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+kehuanTJ_bianhao[2]+'";')[0]
        kehuanTJ_url3 = "/novel_xinxi?bianhao="+kehuanTJ_bianhao[2]
    except:
        kehuanTJ_name3 = "待写入..."
        kehuanTJ_leixin3 = "待写入..."
        kehuanTJ_url3 = "#"
    context['kehuanTJ_name3'] =kehuanTJ_name3
    context['kehuanTJ_leixin3'] = kehuanTJ_leixin3
    context['kehuanTJ_url3'] = kehuanTJ_url3
    try:
        kehuanTJ_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+kehuanTJ_bianhao[3]+'";')[0]
        kehuanTJ_leixin4 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+kehuanTJ_bianhao[3]+'";')[0]
        kehuanTJ_url4 = "/novel_xinxi?bianhao="+kehuanTJ_bianhao[3]
    except:
        kehuanTJ_name4 = "待写入..."
        kehuanTJ_leixin4 = "待写入..."
        kehuanTJ_url4 = "#"
    context['kehuanTJ_name4'] =kehuanTJ_name4
    context['kehuanTJ_leixin4'] = kehuanTJ_leixin4
    context['kehuanTJ_url4'] = kehuanTJ_url4

    try:
        kehuanTJ_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+kehuanTJ_bianhao[4]+'";')[0]
        kehuanTJ_leixin5 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+kehuanTJ_bianhao[4]+'";')[0]
        kehuanTJ_url5 = "/novel_xinxi?bianhao="+kehuanTJ_bianhao[4]
    except:
        kehuanTJ_name5 = "待写入..."
        kehuanTJ_leixin5 = "待写入..."
        kehuanTJ_url5 = "#"
    context['kehuanTJ_name5'] =kehuanTJ_name5
    context['kehuanTJ_leixin5'] = kehuanTJ_leixin5
    context['kehuanTJ_url5'] = kehuanTJ_url5


###################################
    try:
       HOT_bianhao  = novelweb.mysqlsearch.test("select distinct bianhao from HOT;")
    except:
        pass
    try:
        HOT_name1 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+HOT_bianhao[0]+'";')[0]
        HOT_img1 = "/static/NOVEL_IMG/"+novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+HOT_bianhao[0]+'";')[0]
        HOT_jianjie1 = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+HOT_bianhao[0]+'";')[0]
        HOT_url1 = "/novel_xinxi?bianhao="+HOT_bianhao[0]
        HOT_leixin1 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+HOT_bianhao[0]+'";')[0]
    except:
        HOT_name1 = "待写入..."
        HOT_img1 = "/static/web_img/notbook.png"
        HOT_jianjie1 = "待写入..."
        HOT_leixin1 = "待写入..."
        HOT_url1 = "#"
    context['HOT_name1'] =HOT_name1
    context['HOT_img1'] = HOT_img1
    context['HOT_jianjie1'] = HOT_jianjie1
    context['HOT_leixin1'] = HOT_leixin1
    context['HOT_url1'] = HOT_url1

    try:
        HOT_name2 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+HOT_bianhao[1]+'";')[0]
        HOT_leixin2 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+HOT_bianhao[1]+'";')[0]
        HOT_url2 = "/novel_xinxi?bianhao="+HOT_bianhao[1]
    except:
        HOT_name2 = "待写入..."
        HOT_leixin2 = "待写入..."
        HOT_url2 = "#"
    context['HOT_name2'] =HOT_name2
    context['HOT_leixin2'] = HOT_leixin2
    context['HOT_url2'] = HOT_url2

    try:
        HOT_name3 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+HOT_bianhao[2]+'";')[0]
        HOT_leixin3 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+HOT_bianhao[2]+'";')[0]
        HOT_url3 = "/novel_xinxi?bianhao="+HOT_bianhao[2]
    except:
        HOT_name3 = "待写入..."
        HOT_leixin3 = "待写入..."
        HOT_url3 = "#"
    context['HOT_name3'] =HOT_name3
    context['HOT_leixin3'] = HOT_leixin3
    context['HOT_url3'] = HOT_url3
    try:
        HOT_name4 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+HOT_bianhao[3]+'";')[0]
        HOT_leixin4 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+HOT_bianhao[3]+'";')[0]
        HOT_url4 = "/novel_xinxi?bianhao="+HOT_bianhao[3]
    except:
        HOT_name4 = "待写入..."
        HOT_leixin4 = "待写入..."
        HOT_url4 = "#"
    context['HOT_name4'] =HOT_name4
    context['HOT_leixin4'] = HOT_leixin4
    context['HOT_url4'] = HOT_url4

    try:
        HOT_name5 = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+HOT_bianhao[4]+'";')[0]
        HOT_leixin5 = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+HOT_bianhao[4]+'";')[0]
        HOT_url5 = "/novel_xinxi?bianhao="+HOT_bianhao[4]
    except:
        HOT_name5 = "待写入..."
        HOT_leixin5 = "待写入..."
        HOT_url5 = "#"
    context['HOT_name5'] =HOT_name5
    context['HOT_leixin5'] = HOT_leixin5
    context['HOT_url5'] = HOT_url5



##########################################
    context['banquan'] = "宋君顾测试使用"
    context['ico_url'] = "/static/web_img/timg.jpg"
    context['inedx_web_title'] = "宋君顾小说网站"
 #   context['imgname_0'] = "/static/NOVEL_IMG/"+imgname[0]
 #   context['imgname_1'] = "/static/NOVEL_IMG/"+imgname[1]
#    context['novelname_1'] = novelname[0]
 #   context['novelname_2']= novelname[1]
 #   context['zhuan_1'] = zhuantiao[0]
    return render(request, 'index.html', context)
def TWO (request):
    request.encoding='utf-8'
    context  = {}
    if 'bianhao' in request.GET:
        bianhao = request.GET['bianhao']
        novelname = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+bianhao+'";')[0]
        imgname = novelweb.mysqlsearch.test('select novel_imgname from novel_index where novel_bianhao="'+bianhao+'";')[0]
        jianjie = novelweb.mysqlsearch.test('select novel_jianjie from novel_index where novel_bianhao="'+bianhao+'";')[0]
        update = novelweb.mysqlsearch.test('select novel_updatetime from novel_index where novel_bianhao="'+bianhao+'";')[0]
        writer = novelweb.mysqlsearch.test('select novel_writer from novel_index where novel_bianhao="'+bianhao+'";')[0]
        leixin = novelweb.mysqlsearch.test('select novel_leixin from novel_index where novel_bianhao="'+bianhao+'";')[0]
        zhangjiegetmaker = novelweb.zhenwenSQLREADER.test('select novel_zhangjie_name from '+bianhao+';',"novel_zhenwen")
        howlong = str(len(zhangjiegetmaker))
        lastname = novelweb.zhenwenSQLREADER.test('select novel_zhangjie_name from '+bianhao+' where id="'+howlong+'";',"novel_zhenwen")[0]
        context['lastname'] = lastname
        context['lasturl'] = "/READER?bianhao="+bianhao+"&&zhangjiename="+lastname
        zhangjielist = ""
        firstname = zhangjiegetmaker[0]
        context['firsturl'] = "/READER?bianhao="+bianhao+"&&zhangjiename="+firstname
        for y in zhangjiegetmaker:
            zhangjielist = zhangjielist+'<li><a href="/READER?bianhao='+bianhao+'&&zhangjiename='+y+'">'+y+'</a></li>'
        context['novelname'] = novelname
        context['zhangjie'] = zhangjielist
        context['novelimg'] = "/static/NOVEL_IMG/"+imgname
        context['jianjie'] = jianjie
        context['update'] = update
        context['writer'] = writer
        context['leixin'] = leixin
        context['title'] = novelname + "宋君顾小说网站无广告阅读"
    return render(request, 'xinxi.html', context)
def READER(request):
    context={}
    if 'bianhao' in request.GET:
        if'zhangjiename' in request.GET:
            zhenwen = ""
            bianhao = request.GET['bianhao']
            zhangjiename = request.GET['zhangjiename']
            novelname = novelweb.mysqlsearch.test('select novel_name from novel_index where novel_bianhao="'+bianhao+'";')[0]
            for  o in open(os.getcwd()+"\\novelweb\\static\\zhenwen\\"+novelname+"\\"+zhangjiename+".txt",encoding="utf-8"):
                zhenwen = zhenwen + o+"<br/>"
            bianhaox = novelweb.zhenwenSQLREADER.test('select id from '+bianhao+' where novel_zhangjie_name="'+zhangjiename+'";',"novel_zhenwen")[0]
            nextnumber = str(int(bianhaox)+1)
            shangnumber = str(int(bianhaox)-1)
            try:
                nextname = novelweb.zhenwenSQLREADER.test('select novel_zhangjie_name from '+bianhao+' where id="'+nextnumber+'";',"novel_zhenwen")[0]
                context['next'] = "/READER?bianhao="+bianhao+"&&zhangjiename="+nextname
                context['nexthave'] = "下一章"
            except:
                context['next'] = "#"
                context['nexthave'] = "没有下一章咯"
            try:
                shangname = novelweb.zhenwenSQLREADER.test('select novel_zhangjie_name from '+bianhao+' where id="'+shangnumber+'";',"novel_zhenwen")[0]
                context['shang']= "/READER?bianhao="+bianhao+"&&zhangjiename="+shangname
                context['shanghave'] = "上一章"
            except:
                context['shang'] = "#"
                context['shanghave'] = "没有上一章哦"
            context['zhenwen'] = zhenwen
            context['zhangjiename'] = zhangjiename
            context['name'] = novelname
            context['mulu'] = "/novel_xinxi?bianhao="+bianhao
    return render(request, 'READ.html', context)