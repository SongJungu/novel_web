import os
import urllib.request
def IMG_DOWNLOAD(URL,bianhao):
    img_path = os.getcwd()+"\\NOVEL_IMG"+"\\"+bianhao+".jpg"
    urllib.request.urlretrieve(URL,img_path)