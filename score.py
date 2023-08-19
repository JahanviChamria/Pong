from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r=0
        self.l=0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r, align="center", font=('Courier', 80, 'normal'))
