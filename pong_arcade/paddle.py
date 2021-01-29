from turtle import Turtle

INICIO_POSITIONS = [(0, 20), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle:

    
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.head = self.paddles[0]

    def create_paddle(self):
        #cria 3 objetos snake com forma de quadrado para compor o centro da tela
        for position in INICIO_POSITIONS:
            self.add_segment(position)        

    def add_segment(self, position):
        new_body = Turtle(shape = "square")
        new_body.color("white") 
        new_body.penup()
        new_body.goto(position)
        self.paddles.append(new_body)
    
    def move(self):
        # start inicio do range, até onde roda, step de quanto em quanto roda
        for body_num in range(len(self.paddles) -1 , 0, -1):
            """O range recebe o tamanho dos corpos. Esse trecho de codigo faz com que a posicao anterior
            assuma a posicao a frente, para efeito de andar com o corpinho da cobra. o goto() leva todo o conjunto para
            a proxima coordenada x, y"""
            new_x = self.paddles[body_num - 1].xcor()
            new_y = self.paddles[body_num - 1].ycor()
            self.paddles[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)   
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)