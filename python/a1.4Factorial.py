#计算1+2！+3！+...+10!的结果
sum,tmp = 0,1
n = input("正整数N：")
for i in range(1,int(n)):
    tmp*=i
    sum+=tmp
print("运算结果是：{}".format(sum))
