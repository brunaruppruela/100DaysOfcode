from turtle import Turtle, Screen

dyeizo = Turtle()
screen = Screen()
dyeizo.shape("turtle")
dyeizo.color("blue", "white")

def move_forward():
    """funcao funcao para caminhar a frente"""
    dyeizo.forward(10)

def move_backward():
    """funcao funcao para caminhar atras"""
    dyeizo.backward(10)

def turn_left():
    """funcao funcao vira a tartatura para esquerda"""
    new_heading = dyeizo.heading() + 10
    dyeizo.setheading(new_heading)

def turn_right():
    """funcao funcao vira a tartatura para direita"""
    new_heading = dyeizo .heading() - 10
    dyeizo.setheading(new_heading)

# def funcao_rodar():
#     """funcao funcao para desenhar circulos rodando"""
#
#     dyeizo.forward(10)
#     dyeizo.circle(50, extent=12, steps=120)

def funcao_clear():

    """funcao para limpar o desenho e voltar com a tartaruga para o centro, usei o penup para quando voltar ao centro
    nao trazer o trajeto desenhado."""

    dyeizo.clear()
    dyeizo.penup()
    dyeizo.home()


#chama o metodo para escutar o evento em key, a fun executa a funcao de mover para frente ou qualquer outra
#funcao.
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=funcao_clear)



screen.exitonclick()