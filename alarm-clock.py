import turtle
import time
import winsound as ws
import sys

wn =turtle.Screen()
wn.title("Digital Clock")
wn.bgcolor("white")
wn.setup(width=300, height=200)
wn.tracer(0)

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()

Time = time.strftime("%H:%M:%S")

print("")
print(f"Current time is {Time} .")
Alarm = input("Enter Alarm time : ")
print("")

print(f"Alarm set for {Alarm} .")
yes_no = str(input("Do you want to set this alarm ? [y/n] : ")).lower()
print("")

def draw_clock():
    pen1.pencolor("gray")
    pen1.pensize(5)
    x = pen1.xcor = -75
    y = pen1.ycor = 45
    pen1.goto(x,y)
    pen1.pendown()
    for i in range(2):
        pen1.forward(150)
        pen1.right(90)
        pen1.forward(50)
        pen1.right(90)
    pen1.penup()
    pen2.penup()
    pen2.goto(x-15, y+15)
    pen2.pencolor("black")
    pen2.pensize(25)
    pen2.pendown()
    for i in range(2):
        pen2.forward(180)
        pen2.right(90)
        pen2.forward(80)
        pen2.right(90)
    

def show_time():
    pen3.pencolor("red")
    pen3.goto(0,0)
    pen3.clear()
    pen3.write(f"{Time}", font=("arial", 25, "normal"), align="center")
    pen3.penup()
    pen3.goto(0,-32)
    pen3.pendown()
    pen3.write(d, font=("arial", 15, "normal"), align="center")

if yes_no == "n" or yes_no == "no":
    print("")
    print(f"Currently it is {Alarm} .")
    Alarm = input("Enter Alarm time : ")
    print("")
    print(f"Alarm set for {Alarm} .")
    yes_no = str(input("Do you want to set this alarm ? [y/n] : ")).lower()
    print("")

while yes_no == "y" or yes_no == "yes":
    while Time != Alarm:
        Time = time.strftime("%H:%M:%S")
        h =time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        d = time.strftime("%D")
        show_time()
        draw_clock()
        time.sleep(1)
        wn.update()
        if Time == Alarm:
            ws.PlaySound("Alarm-Fast-A1-www.fesliyanstudios.com", ws.SND_FILENAME)

wn.mainloop()

