# filename: password.py
# -*- coding: utf-8 -*-

import hashlib

from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog

class UserPassword(Toplevel):
    '''Класс окна запроса имени пользователя и пароля'''
    def __init__(self, parent, Title_Name: str, Button_Name: str):
        '''
        Конструктор окна запроса имени пользователя и пароля.
        :param Title_Name: Заголовок окна
        :type Title_Name: str
        :param Button_Name: Надпись на кнопке
        :type Title_Name: str
        '''
        super().__init__(parent)
        self.name = StringVar()                                                 #Переменная для считывания имени пользователя
        self.password = StringVar()                                             #Переменная для считывания пароля
        self.title_name = Title_Name                                            #Переменная для заголовка окна
        self.button_name= Button_Name                                           #Переменная для хранения названия кнопки
        self.user=[]                                                            #Список для хранения имени пользователя и хэш-суммы пароля
        self.resizable(False, False)                                            #Запрет на изменение размеров пользователем
        self.title(self.title_name)                                             #Установка заголовка окна
        label_action = Label(self, text = "Введите имя пользователя и пароль:") #Создание виджета надписи
        label_action.grid(row = 0, column = 0, sticky = "w", padx = [30,10], 
                          pady = [10,10])                                       #Размещение виджета по сетке
        label_name = Label(self, text = "Имя пользователя:")                    #Создание виджета надписи
        label_name.grid(row = 1, column = 0, sticky = "w", padx = [30,10], 
                        pady = [5,5])                                           #Размещение виджета по сетке
        entry_name = Entry(self, textvariable=self.name)                        #Создание виджета поле ввода
        entry_name.grid(row = 1, column = 1, sticky =  W+E, padx = [0,30], 
                        pady = [5,5])                                           #Размещение виджета по сетке
        label_password = Label(self, text = "Пароль:")                          #Создание виджета надписи
        label_password.grid(row = 2, column = 0, sticky = "w", padx = [30,10], 
                            pady = [5,5])                                       #Размещение виджета по сетке
        entry_password = Entry(self, textvariable=self.password)                #Создание виджета поле ввода
        entry_password.grid(row = 2, column = 1, sticky = W+E, padx = [0,30], 
                            pady = [5,5])                                       #Размещение виджета по сетке
        button_action = Button(self, text = self.button_name, 
                               command = self.button_action_press)              #Создание виджета поле ввода
        button_action.grid(row = 3, column = 1, sticky = W+E, padx = [0,30], 
                           pady = [5,10])                                       #Размещение виджета по сетке
        self.bind("<Return>", self.button_action_press)                         #Связывание события нажатия кнопки Enter и обработчика кнопки
        width_screen = self.winfo_screenwidth()                                 #Ширина экрана
        height_screen = self.winfo_screenheight()                               #Высота экрана
        self.update()                                                           #Вычисление параметров создаваемого окна
        width_win = self.winfo_width()                                          #Запрос ширины окна
        height_win = self.winfo_height()                                        #Запрос высоты окна
        x = width_screen//2 - width_win//2                                      #Координата x левого верхнего угла окна
        y = height_screen//2 - height_win//2                                    #Координата y левого верхнего угла окна
        self.geometry('+{}+{}'.format(x, y))                                    #Размещение окна по центру экрана
        entry_name.focus_set()                                                  #Передача фокуса ввода первому полю ввода на форме
    
    def button_action_press(self, *args):
        '''Метод обработки нажатия кнопки на форме'''
        name = self.name.get()                                                  #Копирование имени пользователя из поля ввода
        password = self.password.get()                                          #Копирование пароля пользователя из поля ввода
        if name == "":                                                          #Проверка на наличие введенного имени
            showinfo(title = "Ошибка ввода данных", 
                     message = "Не введено имя пользователя")                   #Сообщение об ошибке ввода имени пользователя
        elif password == "":                                                    #Проверка на наличие введенного пароля
            showinfo(title = "Ошибка ввода данных", 
                     message = "Не введен пароль")                              #Сообщение об ошибке ввода пароля
        else:
            password_hash = hashlib.md5(password.encode()).hexdigest()          #Хэширование пароля алгоритмом MD-5
            self.user.append(name)
            self.user.append(password_hash)
            self.destroy()                                                      #Закрытие окна ввода пароля    

    def get_data(self) -> list:
        '''Метод запроса данных имени пользователя и хэш-суммы пароля
           :return: список, содержащий имя пользователя и хэш-сумму пароля
           :rtype: list в формате [имя_пользователя: str, хэш-сумма_пароля: str].
        '''
        self.grab_set()                                                         #Захват пользовательского ввода окном верхнего уровня
        self.wait_window()                                                      #Ожидание закрытия окна ввода имени пользователя и пароля
        return self.user                                                        #Возвращение кортежа с данными пользователя
