# filename: information.py
# -*- coding: utf-8 -*-

from tkinter import* 

class InfoWin(Toplevel):
    '''Класс окна справки'''
    def __init__(self, parent):
        super().__init__(parent)
        INFO = "     Данная программа представляет собой имитацию работы \n"\
            "конечного автомата, моделирующего процесс перемещения робота \n"\
            "по игровому полю. Для робота задаются команды: «повернуть \n"\
            "налево», «повернуть направо», «сделать шаг вперед». После \n"\
            "получения команды автомат отображает значение координаты \n"\
            "игрового поля, которого достигает робот после выполнения \n"\
            "команды, либо выдает сообщение, если невозможно выполнить \n"\
            "данную команду (робот встретил на своем пути препятствие или \n"\
            "достиг края игрового поля)." \
            "\nПрограмма может запускаться в трех режимах работы: \n"\
            "     - режим, моделирующий работу конечного автомата; \n"\
            "     - режим создания конфигурации автомата; \n"\
            "     - режим редактирования ранее созданной конфигурации. \n"\
            "     Данные конфигураций автомата защищены паролем, при \n"\
            "создании конфигурации следует задать имя пользователя и \n"\
            "пароль, а при открытии конфигурации необходимо ввести ранее \n"\
            "заданные имя пользователя и пароль.\n\n"\
            "Задание для летней практики \n"\
            "Выполнил студент группы 22-ВМв Хаченков О.И. \n"\
            "НГТУ им. Алексеева 2024 год."                                      #Текст справки
        self.resizable(False, False)                                            #Запрет на изменение размеров пользователем
        self.title("Справка")                                                   #Установка заголовка окна
        label_action = Label(self, justify=LEFT , text = INFO)                  #Создание виджета надписи
        label_action.pack(side=TOP, padx=10, pady=10)                           #Размещение виджета по сетке
        button_1 = Button(self, text = "Закрыть", command = self.destroy)       #Создание виджета поле ввода
        button_1.pack(side=RIGHT, padx=10, pady=10)                             #Размещение виджета по сетке
        width_screen = self.winfo_screenwidth()                                 #Ширина экрана
        height_screen = self.winfo_screenheight()                               #Высота экрана
        self.update()                                                           #Вычисление параметров создаваемого окна
        width_win = self.winfo_width()                                          #Запрос ширины окна
        height_win = self.winfo_height()                                        #Запрос высоты окна
        x = width_screen//2 - width_win//2                                      #Координата x левого верхнего угла окна
        y = height_screen//2 - height_win//2                                    #Координата y левого верхнего угла окна
        self.geometry('+{}+{}'.format(x, y))                                    #Размещение окна по центру экрана
        self.focus_set()                                                        #Передача фокуса окну 
        self.grab_set()                                                         #Захват пользовательского ввода окном верхнего уровня
        self.wait_window()                                                      #Ожидание закрытия окна