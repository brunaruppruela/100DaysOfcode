from turtle import Turtle

class Ball(Turtle):
    #criando o objeto paddle do lado direito com caracteristicas da classe turtle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def colision_top():
        