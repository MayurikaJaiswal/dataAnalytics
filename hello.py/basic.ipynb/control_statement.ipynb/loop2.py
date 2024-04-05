#no. of steps unknown bit condition known
from turtle import*
speed ('fastest')
n=0
while n<=200:
    fd(100 + n)
    rt(60)
    write(n,font=('Calibari',16))
    n += 2

hideturtle()
mainloop()