import sqlconnter
import time
bianhao = "GANRO"+str(time.time())+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
bianhao =bianhao.replace(".","")
update = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
sqlconnter.novelindexconnter("小说名",bianhao,"玄幻",update,"宋毕罗","这是数据库测试","这是图片名","http://nadnawo","ganro")