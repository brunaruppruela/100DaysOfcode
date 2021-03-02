#Código para criar uma Corrida de Tartatugas!
from turtle import Turtle, Screen
import random
from tkinter import messagebox

is_race_on = False
screen = Screen()

"""usar o metodo setup para alterar o tamanho da tela, pois é necessario para o jogo"""
screen.setup(width=500, height=400)
"""usar o textinput semelhante ao input padrão. Da um titulo a janela e recebe num campo o dado, atraves do prompt"""
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ['A', 'B', 'C', 'D', 'E', 'F']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


#passei o parametro shape para que a classe iniciasse o objeto
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.write(names[turtle_index], True, align="center")
    all_turtles.append(new_turtle)
    

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                #para o loop caso a escolha do usuario chegue junto com qualquer outra tartaruga
                is_race_on = False
            else:
                messagebox.showinfo(title="Oops", message=f"You've lost! The {winning_color} turtle is the winner!")
                #print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()