#a4.5GuessNumberV3.py
from random import *
N = 0
guess_number= randint(0,9)
while True:
    try:
        temp = int(input("请输入一个整数:"))
    except:
        print("请正确输入一个整数")
        N = N+1
        #temp = int(input("请输入另一个整数"))
    finally:
        if temp == guess_number:
            N = N+1
            print("恭喜你，猜了{}次，你猜对了".format(N))
            break
        elif temp > guess_number:
            print("遗憾，猜大了")
            N = N + 1
        elif temp < guess_number:
            print("cai xiao le")
            N = N + 1
