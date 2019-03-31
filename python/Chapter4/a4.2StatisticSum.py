#a4.2StatisticsSum.py
a = input("请输入字符串")
d=f=g=e=0
for i in a:
    if i.isalpha():
        f = f+1
    elif i.isdigit():
        d = d+1
    elif i == " ":
        g = g+1
    else:
        e = e+1
print("中英文字符数{} 空格数{}  数字{}  其他{}".format(f,g,d,e))
