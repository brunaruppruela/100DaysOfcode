from turtle import Turtle

class Paddle(Turtle):
    #criando o objeto paddle do lado direito com caracteristicas da classe turtle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        #tamanho da pá
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        #alinhamento a direita
        self.goto(position)


    def go_up(self):
        """Função para movimentar a pá na coordenada Y, ou seja pra cima, ela anda de 20 em 20 quadros"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Função para movimentar a pá na coordenada Y negativa, ou seja pra baixo, ela anda de 20 em 20 quadros"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        