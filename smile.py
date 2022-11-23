from turtle import *

def eye():
    begin_fill()
    color("white")
    circle(25)
    end_fill()

def pupil():
    begin_fill()
    color("black")
    left(180)
    circle(10)
    end_fill()



speed(0)
begin_fill()

color("yellow")

circle(100)

end_fill()

color("white")
penup()
left(90)
forward(100)
left(90)
forward(50)

left(180)
pendown()
begin_fill()
color("white")
circle(25)
end_fill()

penup()
forward(100)
pendown()
eye()

penup()
left(180)
forward(50)
left(90)
forward(55)
left(90)
pendown()
begin_fill()
color("black")
circle(30)
end_fill()

left(90)
forward(50)
penup()
left(90)
forward(50)
pendown()
begin_fill()
color("black")
left(180)
circle(10)
end_fill()

penup()
forward(100)
left(180)
pendown()
pupil()



done()