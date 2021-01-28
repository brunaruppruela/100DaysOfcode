from turtle import Turtle

#constantes sao declaradas em python, em maiusculo
INICIO_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    
    def __init__(self):
        self.all_bodys = []
        self.create_snake()
        self.head = self.all_bodys[0]

    def create_snake(self):
        #cria 3 objetos snake com forma de quadrado para compor o centro da tela
        for position in INICIO_POSITIONS:
            self.add_segment(position)        

    def add_segment(self, position):
        new_body = Turtle(shape = "square")
        new_body.color("white") 
        new_body.penup()
        new_body.goto(position)
        self.all_bodys.append(new_body)
    
    def extend(self):
        self.add_segment(self.all_bodys[-1].position())

    def move(self):
        # start inicio do range, até onde roda, step de quanto em quanto roda
        for body_num in range(len(self.all_bodys) -1 , 0, -1):
            """O range recebe o tamanho dos corpos. Esse trecho de codigo faz com que a posicao anterior
            assuma a posicao a frente, para efeito de andar com o corpinho da cobra. o goto() leva todo o conjunto para
            a proxima coordenada x, y"""
            new_x = self.all_bodys[body_num - 1].xcor()
            new_y = self.all_bodys[body_num - 1].ycor()
            self.all_bodys[body_num].goto(new_x, new_y)
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
