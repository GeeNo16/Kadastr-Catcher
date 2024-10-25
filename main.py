from tkinter import *
import func
from func import need_dir


def get_dir():
    global show_dir
    show_dir.delete(0, END)
    show_dir.insert(0, need_dir())


def final_button_f():
    directory = show_dir.get()
    mode = mode_var.get()
    decision = type_var.get()
    func.base(directory, mode, decision)


window = Tk()
window.title('Kadastr catcher')
head = PhotoImage(file='Head.png')
window.iconphoto(False, head)
background = PhotoImage(file='Background.png')
background_label = Label(window, image=background)
background_label.place(x=0, y=300, relwidth=1, relheight=1)
height = 900
width = 650
window.geometry(f'{height}x{width}+900+400')
window.resizable(False, False)


mode_var = IntVar()
type_var = IntVar()

greeting = Label(window, text='Kadastr catcher для PDF и XML', font=('times', 40, 'bold'), foreground='#2c5630')
greeting.pack(padx=10)

settings_label = Label(window, text='Настройки', font=('times', 30, ''), foreground='#2c5630')
settings_label.pack(anchor='n')

type_label = Label(window, text='1) Выберите тип обрабатываемых файлов', font=('times', 20, ''))
type_label.place(x=226, y=120)
type0 = Radiobutton(window, text='PDF', variable=type_var, value=0, font=('', 13, ''), fg='#2c5630')
type1 = Radiobutton(window, text='XML', variable=type_var, value=1, font=('', 13, ''), fg='#2c5630')
type2 = Radiobutton(window, text='PDF и XML', variable=type_var, value=2, font=('', 13, ''), fg='#2c5630')
type2.place(x=260, y=152)
type0.place(x=260, y=182)
type1.place(x=260, y=212)


ch_dir_label = Label(window, text='2) Выберите любой файл в папке для обработки', font=('times', 20, ''))
ch_dir_label.place(x=226, y=240)

ch_dir = Button(window, text='Выбрать...', borderwidth=3, command=get_dir, fg='#2c5630')
ch_dir.place(x=257, y=277)

show_dir = Entry(window, width=50)
show_dir.place(x=257, y=310)

modes_label = Label(window, text='3) Выберите формат имени файлов', font=('times', 20, ''))
modes_label.place(x=226, y=332)
mode0 = Radiobutton(window, text='XX_XX_XXXXXXX_XXX', variable=mode_var, value=0, font=('', 13, ''), fg='#2c5630')
mode1 = Radiobutton(window, text='XX,XX,XXXXXXX,XXX', variable=mode_var, value=1, font=('', 13, ''), fg='#2c5630')
mode2 = Radiobutton(window, text='XX;XX;XXXXXXX;XXX', variable=mode_var, value=2, font=('', 13, ''), fg='#2c5630')
mode0.place(x=260, y=370)
mode1.place(x=260, y=400)
mode2.place(x=260, y=430)

final_label = Label(window, text='4) Запустите программу', font=('times', 20, ''))
final_label.place(x=226, y=460)

final_button = Button(window, text='Запустить', borderwidth=3, command=final_button_f, fg='#2c5630')
final_button.place(x=257, y=497)


window.mainloop()
