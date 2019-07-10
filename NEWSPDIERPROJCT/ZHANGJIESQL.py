#!/usr/bin/python3
 
import pymysql

def zhangjiesqlWriter(sql_mim,sql_zhanghao,sql_IP,zhangjiename,sql_biaoname):

    db = pymysql.connect(sql_IP,sql_zhanghao,sql_mim,"novel_zhenwen" )

 

    cursor = db.cursor()
 

    sql ="INSERT INTO "+sql_biaoname+"(novel_zhangjie_name) VALUES ("+"'"+zhangjiename+"'"+");"
    try:

        cursor.execute(sql)
 
        db.commit()
    except:

        db.rollback()
    db.close()