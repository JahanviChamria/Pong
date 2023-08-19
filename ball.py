from turtle import Turtle, Screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove=10
        self.ymove=10
        self.ms=0.1

    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx, newy)

    def bouncey(self):
        self.ymove*=-1
        self.ms*=0.9

    def bouncex(self):
        self.xmove*=-1
        self.ms*= 0.9

    def restart(self):
        self.goto(0,0)
        self.ms=0.1
        self.xmove *= -1