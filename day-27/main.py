from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


#construindo o objeto tela
window =  Tk()

#Definindo o titulo da janela
window.title("Miles to Kilometer")
window.config(padx=20, pady=20)
#Definindo o tamanho minino para tela, caso não seja definido, abrira pequeno

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)


kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)


button2 = Button(text="Calculate", command=calculate)
button2.grid(column=1, row=2)





#metodo que mantem a tela ativa enquanto o programa roda.
window.mainloop()