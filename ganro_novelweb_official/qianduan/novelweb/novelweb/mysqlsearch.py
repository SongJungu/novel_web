#!/usr/bin/python3
 
import pymysql



db = pymysql.connect("localhost","root","gykjganluo520","novelweb" )

 
def  test(what_search):
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