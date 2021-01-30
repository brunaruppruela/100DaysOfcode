from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#criando o objeto e definindo tamanho da janela, cor e nome
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Arcade")
screen.tracer(0)

#iniciando os objetos das pás esq e dir
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


#capturando os eventos do teclado para movimentar a pá, lembrando que passar função por parametro não é necessario os ()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


#evento para sair da tela do jogo ao clicar
screen.exitonclick()