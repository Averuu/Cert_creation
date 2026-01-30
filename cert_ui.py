"""."""
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import ttk, scrolledtext
import smtplib
from email.message import EmailMessage

PATH = 'nameless.png'
global_name_coords = (421, 263)
DATE_COORDS = (150, 445)

WIDTH_DICT = {
    'й': 14,
    'ц': 14,
    'у': 13,
    'к': 12,
    'е': 14,
    'н': 14,
    'г': 10,
    'ш': 19,
    'щ': 19,
    'з': 10,
    'х': 12,
    'ъ': 14,
    'ф': 18,
    'ы': 17,
    'в': 11,
    'а': 13,
    'п': 14,
    'р': 13,
    'о': 13,
    'л': 13,
    'д': 14,
    'ж': 18,
    'э': 12,
    'я': 13,
    'ч': 13,
    'с': 13,
    'м': 16,
    'и': 13,
    'т': 12,
    'ь': 12,
    'б': 13,
    'ю': 17,
    'ё': 14,
    'Й': 16,
    'Ц': 17,
    'У': 14,
    'К': 15,
    'Е': 13,
    'Н': 16,
    'Г': 12,
    'Ш': 22,
    'Щ': 22,
    'З': 13,
    'Х': 14,
    'Ъ': 17,
    'Ф': 20,
    'Ы': 21,
    'В': 14,
    'А': 17,
    'П': 16,
    'Р': 14,
    'О': 16,
    'Л': 16,
    'Д': 17,
    'Ж': 22,
    'Э': 15,
    'Я': 14,
    'Ч': 15,
    'С': 16,
    'М': 19,
    'И': 15,
    'Т': 14,
    'Ь': 14,
    'Б': 15,
    'Ю': 22,
    'Ё': 13,
    ' ': 8,
    '-': 10
}
MONTHS_DICT = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}

theCert = None


class Certicate():
    """Автосоздание сертификатов."""

    global global_name_coords

    def __init__(self, path='', names=[], dates=[],
                 name_coords=global_name_coords,
                 date_coords=(), colour=(0, 0, 0),
                 emails=[],
                 font_name='Montserrat-Bold.ttf',
                 font_date='Montserrat-Medium.ttf', size=20):
        """."""
        self.path = path
        self.names = names
        self.dates = dates
        self.name_coords = name_coords
        self.date_coords = date_coords
        self.colour = colour
        self.font_date = font_date
        self.font_name = font_name
        self.size = size
        self.emails = emails

    def create_one(self, name, date):
        """Создание  одного сертификата."""
        img = Image.open(self.path)
        draw = ImageDraw.Draw(img)
        font_name = ImageFont.truetype(self.font_name, self.size)
        font_date = ImageFont.truetype(self.font_date, 12)

        global global_name_coords
        global WIDTH_DICT
        name_coords = list(global_name_coords)
        name_set = list(set(list(name)))
        width = 0
        for j in name_set:
            width += name.count(j) * WIDTH_DICT[j]
        name_coords[0] -= int(width / 2)

        date = date.split('.')
        date1 = date[0].strip()
        date2 = MONTHS_DICT[date[1]]
        date = f'{date1} {date2} {date[2].strip()} г.'

        draw.text(name_coords, name,
                  fill=self.colour, font=font_name)
        draw.text(self.date_coords, date,
                  fill=self.colour, font=font_date)
        # remake to mond medium 12
        img.save(f'Автобаза. Сертификат. {name}.pdf')

    def create_certs(self):
        """Создание всех сертификатов."""
        for i in range(len(self.names)):
            self.create_one(self.names[i], self.dates[i])

    def create_demo(self):
        """демо создание."""
        self.create_one("Иванов Иван Иванович", "01.12.2025")

    def get_info(self):
        return [self.names, self.emails]


class Message:
    """Отправка email."""
    def __init__(self, email, password):
        """."""
        self.email = email
        self.password = password
        self.msg = EmailMessage()

    def create_message(self, to_list, subject_text='',
                       content='', att_list=[], filename='name'):
        """Формировка сообщения."""
        self.msg['Subject'] = subject_text  # тема
        self.msg["From"] = self.email  # от кого
        self.msg["To"] = ', '.join(to_list)  # кому
        self.msg.set_content(content)
        if att_list:
            if not isinstance(att_list, list):
                att_list = [att_list]
            for i in att_list:
                self.msg.add_attachment(i, maintype='document',
                                        subtype='pdf',
                                        filename=filename)

    def send_message(self):
        """."""
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        # шифровка
        smtpobj.starttls()
        # login (emailer_app password)
        smtpobj.login(self.email, self.password)
        smtpobj.send_message(self.msg)
        self.msg = EmailMessage()

    def send_certs(self, cert, subject, text):
        names, emails = cert.get_info()[0], cert.get_info()[1]
        if len(names) != len(emails):
            raise ValueError
        for i in range(len(names)):
            with open(f'Автобаза. Сертификат. {names[i]}.pdf', "rb") as c:
                att = c.read()
                filename = f'Автобаза. Сертификат. {names[i]}.pdf'
                # , maintype='document', subtype='pdf', filename=filename
                self.create_message([emails[i]], subject_text=subject,
                                    content=text, att_list=att,
                                    filename=filename)
                self.send_message()


def send_all():
    global theCert
    msg = Message('', '')
    msg.send_certs(theCert, subject='Тестим сноооваааа', text='lololoоаоао')


def my_process_function(array):
    """Обработка входных данных."""
    global theCert
    names = []
    dates = []
    emails = []
    for i in range(1, len(array), 2):
        things = array[i]
        things = things.replace(':', '_')
        things = things.split('\t')
        dates.append(things[0].split(' ')[0])
        names.append(things[1])
        emails.append(things[2])

    theCert = Certicate(PATH, names=names, dates=dates,
                        date_coords=DATE_COORDS, emails=emails)
    theCert.create_certs()
    print(theCert.emails)
    send_all()

    return None


class SimpleArrayGUI:
    """."""

    def __init__(self, root, process_function=None):
        """."""
        self.root = root
        self.process_function = process_function
        self.root.title("Создание сертификатов")
        self.root.geometry("500x400")

        self.setup_ui()

    def setup_ui(self):
        """."""
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = ttk.Label(main_frame,
                                text="Введите имена и фамилии (всё с новой строки)",
                                font=("Arial", 12))
        title_label.pack(pady=(0, 10))

        # Область ввода текста
        self.text_area = scrolledtext.ScrolledText(main_frame, height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=(0, 10))
        
        # Кнопка вставки из буфера обмена
        paste_btn = ttk.Button(button_frame, text="Вставить из буфера",
                               command=self.paste_from_clipboard)
        paste_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Кнопка обработки
        process_btn = ttk.Button(button_frame, text="Создать сертификаты",
                                      command=self.get_array_data)
        process_btn.pack(side=tk.LEFT)

        send_btn = ttk.Button(button_frame, text="Отправить сертификаты",
                                      command=self.get_array_data)
        process_btn.pack(side=tk.LEFT)

        # Метка для вывода количества строк
        self.count_label = ttk.Label(main_frame, text="")
        self.count_label.pack()

    def paste_from_clipboard(self):
        """Вставляет текст из буфера обмена в текстовое поле."""
        try:
            # Получаем текст из буфера обмена
            clipboard_text = self.root.clipboard_get()
            
            # Вставляем в текущую позицию курсора
            self.text_area.insert(tk.INSERT, clipboard_text)
            
            # Прокручиваем до конца
            self.text_area.see(tk.END)
            
        except tk.TclError:
            # Если буфер обмена пуст или недоступен
            self.count_label.config(text="Буфер обмена пуст")
        except Exception as e:
            self.count_label.config(text=f"Ошибка: {str(e)}")

    def get_array(self):
        """Возвращает массив строк из текстового поля."""
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            return []

        # Разделяем на строки, убираем пустые и лишние пробелы
        lines = text.split('\n')
        array = [line.strip() for line in lines if line.strip()]
        return array

    def get_array_data(self):
        """Нажатие кнопки - получает массив и передаёт в функцию обработки."""
        array = self.get_array()
        print('ARRAY: ', array)

        # Обновляем метку с количеством строк
        count = len(array)
        self.count_label.config(text=f"Загружено строк: {count}")

        # Если передана функция обработки, вызываем её
        if self.process_function:
            try:
                result = self.process_function(array)
                # После обработки обновляем статус
                self.count_label.config(text=f"Создано {len(array)//2 if len(array)%2==0 else 'ошибка'} сертификатов")
            except Exception as e:
                self.count_label.config(text=f"Ошибка обработки: {e}")
                print(f"Ошибка обработки: {e}")
        
        my_process_function(array)


# Пример использования
# Пример использования
def main():
    """."""
    root = tk.Tk()

    # Пример функции обработки - просто возвращает массив обратно


    # Создаём GUI
    app = SimpleArrayGUI(root)

    # Чтобы получить массив из другого места программы:
    # array = app.get_array()

    root.mainloop()


if __name__ == "__main__":
    main()
