#MoneyConvert.py
MonStr = input("请输入需转换人民币或者美元的数量")
if MonStr[-1] in ['D','d']:
    R = eval(MonStr[0:-1])*6
    print("转换后的人民币为{:.2f}R".format(R))
elif MonStr[-1] in ['R','r']:
    D = eval(MonStr[0:-1])/6
    print("转换后的美元为{:.2f}D".format(D))
else:
    print("输入格式有误")
    
