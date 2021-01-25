from turtle import Screen, Turtle
import time 

#inicia o objeto tela
screen = Screen()

#define o tamanho da tela e cor com o bgcolor
screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("My Snake Game")

#deixa a tela preta para efeito de animação dos corpinhos
screen.tracer(0)

inicio_positions = [(0, 0), (-20, 0), (-40, 0)]

all_bodys = []

#cria 3 objetos snake com forma de quadrado para compor o centro da tela
for position in inicio_positions:
    new_body = Turtle(shape = "square")
    new_body.color("white")
    new_body.penup()
    new_body.goto(position)
    all_bodys.append(new_body)


game_is_on = True
while game_is_on:
    #retorna a imagem após executar o loop for
    screen.update()
    #atrasa 1s de cada body
    time.sleep(0.1)

    # start inicio do range, até onde roda, step de quanto em quanto roda
    for body_num in range(len(all_bodys) -1 , 0, -1):
        new_x = all_bodys[body_num - 1].xcor()
        new_y = all_bodys[body_num - 1].ycor()
        all_bodys[body_num].goto(new_x, new_y)
    all_bodys[0].foward(20)   
    



screen.exitonclick()
