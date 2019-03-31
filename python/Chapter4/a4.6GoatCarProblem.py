#4.6GoatCarProblem.py
import random as r
times = pow(10, eval(input("请输入数字")))
win1=win2=0
for i in range(times):
    man = r.randint(1,3)
    car = r.randint(1,3)
    if man == car:
        win1 += 1
    else:
        win2 +=1
change=win2/times
nochange = win1/times
print("{}次实验中".format(times))
print("更换选择赢的概率为：{:.2%}".format(change))
print("不换选择赢的概率为：{:.2%}".format(nochange))
