#a2.1Tempconvert.py 输入"234.f"
TempStr = eval(input(" 请输入温度:"))
#TempStr = eval(TempStr)
TempStr = str(TempStr)
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32) / 1.8
    print("温度转换为摄氏度为:{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = eval(TempStr[0:-1]) *1.8 +32
    print("温度转换华氏度为：{:.2f}F".format(F))
else:
    print("输入温度格式有误")
