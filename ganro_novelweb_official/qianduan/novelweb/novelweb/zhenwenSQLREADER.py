#!/usr/bin/python3
 
import pymysql


 
def  test(what_search,sqlname):
    db = pymysql.connect("localhost","root","gykjganluo520",sqlname)
    cursor = db.cursor()
    array = [] 
    sql = what_search
    try:
        db.ping(reconnect=True)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            print(str(fname))
            array.append(fname)
        db.commit()
        print(array)
    except:

        db.rollback()
    db.close()
    return array