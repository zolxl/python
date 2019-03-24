#a2.3ColorfulPython.py
import turtle as t
t.setup(1300,550,20,20)
t.pu()
t.fd(-500)
t.pensize(25)
t.pd()
t.seth(-40)
for i in range(9):
    color = ['purple','red','grey','gold','darkgreen','blue','green']
    k = i % 7
    t.pencolor(color[k])
    t.circle(40,80)
    t.circle(-40,80)
'''t.seth(0)'''
t.pencolor('violet')
t.fd(20)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)

def DrawSnake(radius,angle,length):
    t.seth(-40)
    for i in range(length):
        color = ['purple','red','grey','gold','darkgreen','blue','green']
        k = i % 7
        t.pencolor(color[k])
        t.circle(radius,angle)
        t.circle(-radius,angle)
    t.circle(radius,angle/2)
    t.fd(radius)
    t.circle(-16,180)
    t.fd(radius*2/3)
t.up()
t.fd(950)
t.seth(-90)
t.fd(150)
t.down()
DrawSnake(40,80,5)
t.done()


