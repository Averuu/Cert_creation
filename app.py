from tkinter import *
from random import randint

def change_bg():

    #r = str(int(str(randint(0, 255)), 16))[1:]
    #g = str(int(str(randint(0, 255)), 16))[1:]
    #b = str(int(str(randint(0, 255)), 16))[1:]
    #colour = "#" + r + g + b
    clr = [str(hex(randint(0, 2**8 - 1)))[2:] for i in range(3)]
    for i in range(len(clr)):
        if len(clr[i]) != 2:
            clr[i] = "0" + clr[i]
    colour = "#" + "".join(clr)
    root.config(bg=colour)


def move_button(event):

    btn_w = btn_exit.winfo_width()
    btn_h = btn_exit.winfo_height()

    max_x = window_w - btn_w
    max_y = window_h - btn_h

    new_x = randint(0, max_x)
    new_y = randint(0, max_y)

    btn_exit.place(x=new_x, y=new_y)

window_w = 400
window_h = 300

root = Tk()
root.title("Lil' app")
root.geometry(f"{window_w}x{window_h}")
root.config(bg="#23EAC9")


labelTex = "Ты любишь кабачки?????"
lbl = Label(root,
            text=labelTex,
            font=("comicsansms", 30))
lbl.config(bg="#F6C2E5")
lbl.pack(pady=50)
btn_stay = Button(
    text="Да!",
    command=change_bg,
    width=10,
    height=2
)
btn_stay.config(bg="#09FF2A")
btn_stay.place(x=100, y=150)
btn_exit = Button(
    root,
    text="Нет",
    width=10,
    height=2
)
btn_exit.config(bg="#EE1010")
btn_exit.place(x=222, y=150)
btn_exit.bind("<Enter>", move_button)

#НАКОНЕЦ РАБОТАЕТ
root.mainloop()
