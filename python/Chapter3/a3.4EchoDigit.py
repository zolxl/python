#a3.4EchoDigit.py
digit=input("请输入一个自然数：")
echoDigit=digit[::-1]
if eval(digit)==eval(echoDigit):
    print("{}是回文数".format(digit))
else:
    print("{}不是回文数".format(digit))
