#importando os modulos 
from turtle import Screen, Turtle
from snake import Snake
import time 

#inicia o objeto tela
screen = Screen()
#define o tamanho da tela e cor com o bgcolor
screen.setup(width=600, height=600)
screen.bgcolor("black")
#Define o nome da janela
screen.title("My Snake Game")

"""deixa a tela preta para efeito de animação dos corpinhos da cobra, sem ele é mostrado o intervalod
de cada 'andar' da cobra"""
screen.tracer(0)

#instancia o objeto
snake = Snake()

#validação para checar no while e continuar rodando 
game_is_on = True
while game_is_on:
    #retorna a imagem com a execucao do codigo for (comando tracer da linha16)
    screen.update()
    #atrasa 1s a visualizacao de cada body andar na tela, dando efeito de estarem um atras do outro
    time.sleep(0.1)

    snake.move()


#evento para sair da tela do jogo ao clicar
screen.exitonclick()
