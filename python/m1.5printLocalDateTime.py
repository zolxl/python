from datetime import datetime #引用datetime库
now = datetime.now() #获得当前日期和时间
print(now)
now.strftime("%x")   #输出其中的日期部分
now.strftime("%X")  #输出其中的时间部分
print("当前时间是:",end="")
print(now,end="")
print("!")
print("当前日期是:",end="")
print(now.strftime("%x"),end="")
print('当前时间是:',now.strftime("%X"))
