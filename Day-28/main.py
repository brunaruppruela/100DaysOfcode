# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec =SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(works_sessions):
            marks += "✔"
        label_check.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# o parametro highlightthinckeness preenche os espacos em branco ao redor da imagem
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# usando o Photoimage para ler o arquivo foto e armazenar na variavel, assim pode ser lido pelo metodo create_image
tomato_img = PhotoImage(file="./Day-28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



"""criando os labels e botoes: parametro fg preenche a fonte escolhida e o bg o backgroud do label, 
deixando da mesma cor do fundo da tela, no caso, amarelo"""
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

botao_start = Button(text="Start", highlightthickness=0, command=start_timer)
botao_start.grid(column=0, row=2)

botao_reset = Button(text="Reset", highlightthickness=0, command=reset_time)
botao_reset.grid(column=2, row=2)

label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
label_check.grid(column=1, row=3)

window.mainloop()
