#импорт всей библеотеки
#import time
#использование одного метода из всей библеотеки
#time.sleep(secs=0.00001)

#импортируем библеотеку для работы с окнами(интерфейсом) все библеотеки:    tkinter qyqt5 pyside6
# импорт всех функций, классов и переменных из библеотеки !Может вызвать коллизию имён!
#from tkinter import*

#импорт всей библеотеки с присовением псевдонима
from tkinter import as tk

#импорт отдельной функций из модуля(из нашего файла)
# №импортируем библеотеку для работы с окнами(интерфейсом)все библеотеки :tkinter pyqt5 pyside6


# импорт всей библиотеки
import time

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !
# from tkinter import *

# импорт всей библиотеки с присовением псевдонима
# import tkinter as tk


# импорт отдельной функции из модуля(из нашего файла)
# from .calc import calc_3


# импортируем библиотеку для работы с окнами(интерфейсом) все библиотеки: tkinter pyqt5 pyside6


# import tkinter
# import tkinter.ttk as ttk
# root = tkinter.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
from tkinter import ttk

# инициализация инстанса - создание объекта ткинтер
root = Tk()

# создание главного окна
frm = ttk.Frame(root, padding=100)
frm.grid()

# Мы пишем таймер


# часы
ttk.Label(frm, text="00").grid(column=0, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)

# минуты
ttk.Label(frm, text="00").grid(column=2, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)

# секунды
ttk.Label(frm, text="00").grid(column=4, row=0)



# ttk.Label(frm, text="Any").grid(column=0, row=1)
# ttk.Label(frm, text="Alex").grid(column=1, row=1)
# ttk.Label(frm, text="Ivan").grid(column=2, row=1)

# 0    1    2     3    4      5
# 1   Any    :   Alex  :     Ivan



# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


root.mainloop()