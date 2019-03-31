#a4.3MaxCommonModeandMinCommon.py
x,y = int(input("请输入整数：")),int(input("请输出整数b"))
temp = 1
z = min(x,y)
for i in range(1,z+1):
    if x % i == 0 and y % i == 0:
        temp = i
print("zuidagongyueshu:{}".format(temp))
print("最小公倍数%d"%(x*y/temp))
            
