from turtle import Turtle

#constantes sao declaradas em python, em maiusculo
INICIO_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    
    def __init__(self):
        self.all_bodys = []
        self.create_snake()

    def create_snake(self):
        #cria 3 objetos snake com forma de quadrado para compor o centro da tela
        for position in INICIO_POSITIONS:
            new_body = Turtle(shape = "square")
            new_body.color("white") 
            new_body.penup()
            new_body.goto(position)
            self.all_bodys.append(new_body)


    
    def move(self):
        # start inicio do range, até onde roda, step de quanto em quanto roda
        for body_num in range(len(self.all_bodys) -1 , 0, -1):
            """O range recebe o tamanho dos corpos. Esse trecho de codigo faz com que a posicao anterior
            assuma a posicao a frente, para efeito de andar com o corpinho da cobra. o goto() leva todo o conjunto para
            a proxima coordenada x, y"""
            new_x = self.all_bodys[body_num - 1].xcor()
            new_y = self.all_bodys[body_num - 1].ycor()
            self.all_bodys[body_num].goto(new_x, new_y)
        self.all_bodys[0].forward(MOVE_DISTANCE)   
    