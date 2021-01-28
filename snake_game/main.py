#importando os modulos 
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard  = Scoreboard()

#capturar teclas do teclado para movimentar o corpinho
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#validação para checar no while e continuar rodando 
game_is_on = True
while game_is_on:
    #retorna a imagem com a execucao do codigo for (comando tracer da linha16)
    screen.update()
    #atrasa 1s a visualizacao de cada body andar na tela, dando efeito de estarem um atras do outro
    time.sleep(0.1)
    snake.move()

    #detectar as colisoes com comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detectar colisao com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.all_bodys[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


#evento para sair da tela do jogo ao clicar
screen.exitonclick()
