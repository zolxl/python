#a3.1CalculateWeight.py
weight=eval(input("请输入你现在的体重(KG)"))
N=eval(input("请输入计算几年后的体重"))
for i in range(N):
    weight+=0.5
print("N年后你的体重为：{:.2f}".format(weight))
moonWeight=weight * 0.165
print("N年后月亮上的体重为：{}".format(moonWeight))
