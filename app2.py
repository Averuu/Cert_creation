from tkinter import *

WIN_W = 400
WIN_H = 500


class MainVisual:
    """Шаблон окна."""

    def __init__(self, width, height):
        """Init."""
        self.root = Tk()
        self.root.title("Создание сертификатов без СМС и регистрации")
        self.root.geometry(f"{width}x{height}")
        self.root.config(bg="#68F825")

        self.text_label = Label(
            self.root,
            text="Вставь сюда строки вместе с ID-шниками",
            font=("comicsansms", 30)
        )
        self.text_label.pack()

        self.btn_paste()
    
    