from turtle import Turtle, Screen
from paddle import Paddle

#criando o objeto e definindo tamanho da janela, color e nome
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade")

screen = Screen()

paddle = Paddle()


#evento para sair da tela do jogo ao clicar
screen.exitonclick()