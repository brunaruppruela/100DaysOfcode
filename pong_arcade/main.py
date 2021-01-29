from turtle import Turtle, Screen
#from paddle import Paddle

#criando o objeto e definindo tamanho da janela, cor e nome
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade")

#criando o objeto do tipo Screen para herdar as caracteristicas e ações de tela no jogo
screen = Screen()

#criando o objeto paddle do lado direito com caracteristicas da classe turtle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
#tamanho da pá
paddle.shapesize(5, 1)
paddle.penup()
#alinhamento a direita
paddle.goto(350, 0)

def go_up():
    """Função para movimentar a pá na coordenada Y, ou seja pra cima, ela anda de 20 em 20 quadros"""
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    """Função para movimentar a pá na coordenada Y negativa, ou seja pra baixo, ela anda de 20 em 20 quadros"""
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


#capturando os eventos do teclado para movimentar a pá, lembrando que passar função por parametro não é necessario os ()
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")



#evento para sair da tela do jogo ao clicar
screen.exitonclick()