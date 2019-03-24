#a3.2DayDayUP.py
dayUP=1
for i in range(365):
    if i % 7 in [4,5,6,0]:
        dayUP= dayUP*(1+0.01)
    else:
        dayUP=dayUP
print("一年后你的能力值为：{:>50}".format(dayUP))
