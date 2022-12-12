from turtle import Turtle,Screen 

from random import randint , choice as rand_choice

colors = ["blue", "red", "green", "orange", "black"]

class MyTurtle(Turtle):
    def random_shape(self, x, w):
        self.penup()
      

        self.color(rand_choice(colors))
        self.penup()
        self.setposition(randint(-200,200), randint(-200,200))
        self.pendown()

        self.circle(randint(10 , 50), steps=randint(4,10))
        self.right (randint(0,180))
        self.end_fill()


    def __init__(self):
        super().__init__()
        self.random_shape(0,0)
        self.onclick(self.random_shape)


    

x = MyTurtle()

w = MyTurtle()

x.forward(50)

w.backward(50)

screen = Screen()

screen.mainloop()
