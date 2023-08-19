from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

rpaddle=Paddle((350, 0))
lpaddle=Paddle((-350, 0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(key="Up", fun=rpaddle.up)
screen.onkey(key="Down", fun=rpaddle.down)
screen.onkey(key="w", fun=lpaddle.up)
screen.onkey(key="s", fun=lpaddle.down)

game=True
while game:
    time.sleep(ball.ms)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()

    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320:
        ball.bouncex()

    if ball.xcor()>380:
        time.sleep(0.3)
        ball.restart()
        score.l+=1
        score.clear()
        score.update()


    if ball.xcor()<-380:
        time.sleep(0.3)
        ball.restart()
        score.r+=1
        score.clear()
        score.update()



screen.exitonclick()