guanjian = []
for x in open("guoluchi.txt",encoding="utf-8"):
    guanjian.append(x)
def guolu(data):
    for y in range(len(guanjian)):
        gg = guanjian[y]
        data = data.replace(gg,"")
    return data