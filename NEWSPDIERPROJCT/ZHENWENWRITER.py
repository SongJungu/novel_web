import os
def Writer(zhenwen,zhangjiename,novelname):
    lujin = os.getcwd()+"\\zhenwen\\"+novelname+"\\"+zhangjiename+".txt"
    a = open(lujin,"w",encoding="utf-8")
    a.write(zhangjiename + "\n\n")
    a.write(zhenwen)
    a.close()
