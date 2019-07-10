#!/usr/bin/python3
 
import pymysql
def novelindexconnter(novelname,novelbianhao,novelleixin,novelupdate,novelwriter,noveljianjie,novelimgname,yuanurl,rulsname,sql_mima,sql_zhanghao,sql_ip):
     

    db = pymysql.connect(sql_ip,sql_zhanghao,sql_mima,"novelweb")
 

    cursor = db.cursor()
 

    sql = "INSERT INTO novel_index(novel_name,novel_bianhao,novel_leixin,novel_updatetime,novel_writer,novel_jianjie,novel_imgname,noveldianji,yuanURL,RULS_NAME) VALUES ("+"'"+novelname+"'"+","+"'"+novelbianhao+"'"+","+"'"+novelleixin+"'"+","+"'"+novelupdate+"'"+","+"'"+novelwriter+"'"+","+"'"+noveljianjie+"'"+","+"'"+novelimgname+"'"+",0"+",'"+yuanurl+"'"+","+"'"+rulsname+"'"+");"
    try:
 
        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()

    db.close()
    zhencon = pymysql.connect(sql_ip,sql_zhanghao,sql_mima,"novel_zhenwen")
    zcu = zhencon.cursor()
    zhenbiao ='''
    create table '''+novelbianhao+'''(
        novel_zhangjie_name varchar(100) not null,
        id int(100) auto_increment,
        PRIMARY KEY  (`id`)
    )
    '''
    try:
 
        zcu.execute(zhenbiao)

        zhencon.commit()
    except:

        zhencon.rollback()
    zhencon.close()
