# filename: main.py
# -*- coding: utf-8 -*-

from tkinter import*                                                            #Внешние библиотеки
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog

from password import *                                                          #Локальные модули
from field import Field
from engine import Engine
from engine import InvalidEngineValue
from editor import Editor
from file import File
from information import InfoWin 

class MainWin(Tk):
    '''Главный класс программы'''
    def __init__(self):
        super().__init__()
        '''
        Конструктор главного класса.
        Создает главное окно и выполняет основные
        логические функции приложения.
        '''
        self.robot = Engine()                                                   #Создание объекта движка
        self.file_config = File()                                               #Создание объекта для работы с файлом
        self.field = Field(5,5)                                                 #Установка начального размена поля
        self.field.pack(side=LEFT, padx=10, pady=10)                            #Размещение поля на форме с учетом отступов
        self.orientation=""                                                     #Переменная для хранения ориентации робота в пространстве
        self.position = [0, 0]                                                  #Координаты начального расположения робота
        self.title('Програмный автомат "Робот"')                                #Заголовок главного окна
        self.resizable(False, False)                                            #Запрет изменения размеров главного окна пользователем
        main_menu = Menu()                                                      #Создание меню формы
        file_menu = Menu(tearoff = 0)                                           #Запрет штрихового разделителя в меню файл
        info_menu = Menu(tearoff = 0)                                           #Запрет штрихового разделителя в меню справка
        file_menu.add_command(label = "Открыть конфигурацию", 
                              command = self.open_config)                       #Добавление пункта в меню файл "Открыть конфигурацию"
        file_menu.add_command(label = "Создать конфигурацию",
                              command = self.create_config)                     #Добавление пункта в меню файл "Создать конфигурацию"
        file_menu.add_command(label = "Редактировать конфигурацию",
                              command = self.edit_config)                       #Добавление пункта в меню файл "Редактировать конфигурацию                       
        info_menu.add_command(label = "О прграмме", command = self.get_info)
        file_menu.add_separator()                                               #Вставка разделителя
        file_menu.add_command(label = "Выйти", command = self.destroy)          #Добавление пункта в меню файл "Выйти"
        main_menu.add_cascade(label = "Файл", menu = file_menu)                 #Добавление меню "Файл"
        main_menu.add_cascade(label = "Справка", menu = info_menu)              #Добавление меню "Справка"
        self.config(menu = main_menu)                                           #Сборка меню и размещение на форме
        frame_control = LabelFrame(text="Управление", padx=20)                  #Фрейм для размещения кнопок управления
        frame_control.pack(padx=10)
        btn_forward = Button(master=frame_control, text = "Сделать шаг вперед", 
                             command=self.forward)                              #Кнопка "Сделать шаг вперед"
        btn_forward.pack(fill=X, pady=10, side=TOP)
        btn_turn_left = Button(master=frame_control, text="Повернуть налево", 
                               command=self.turn_left)                          #Кнопка "Повернуть влево"
        btn_turn_left.pack(pady=10, side=LEFT, padx=[0,10], ipadx=5)
        btn_turn_right = Button(master=frame_control, text="Повернуть направо", 
                                command=self.turn_right)                        #Кнопка "Повернуть вправо"
        btn_turn_right.pack(pady=10, side=RIGHT, padx=[10,0], ipadx=5)
        frame_st = LabelFrame(text="Состояние", padx=20)                        #Фрейм для отображения состояния автомата
        frame_st.pack(fill=X,padx=10)
        self.label_position = Label(master=frame_st, text = "Координаты: \tx = "
                                    +str(self.robot.get_position_x())+"\ty = "+
                                    str(self.robot.get_position_y()))           #Надпись для отображения координаты х
        self.label_position.pack( anchor=W, pady=10, side=TOP)
        self.label_orientation = Label(master=frame_st, text = "Направление: \t"
                                       +self.orientation_convert_ru(self.robot.\
                                       get_orientation()))                      #Надпись для отображения координаты у
        self.label_orientation.pack( anchor=W, pady=10, side=TOP)
        width_screen = self.winfo_screenwidth()                                 #Ширина экрана
        height_screen = self.winfo_screenheight()                               #Высота экрана
        self.update()                                                           #Вычисление параметров создаваемого окна
        width_win = self.winfo_width()                                          #Запрос ширины окна
        height_win = self.winfo_height()                                        #Запрос высоты окна
        x = width_screen//2 - width_win//2                                      #Координата x левого верхнего угла окна
        y = height_screen//2 - height_win//2                                    #Координата y левого верхнего угла окна
        self.geometry('+{}+{}'.format(x, y))                                    #Размещение окна по центру экрана

    def create_config(self):
        '''Метод создания файла конфигурации'''
        pass_win = UserPassword(self, "Создание конфигурации", "Создать")       #Вызов окна запроса имени пользователя и пароля
        user = pass_win.get_data()                                              #Запрос данных у окна запроса имени пользователя и пароля
        if not user:                                                            #Если окно запроса имени пользователя и пароля вернуло пустой список
            return                                                              #Процесс создания конфигурации завершается
        editer = Editor(self, "Создание конфигурации")                          #Создание объекта для работы с данными конфигурации
        data = editer.get_data()                                                #Запрос данных у окна объекта для работы с данными конфигурации
        if not data:                                                            #Если получен пустой словарь (окно было закрыто крестиком), 
            return                                                              #процесс создания конфигурации заканчивается.
        types = (("Файл конфигурации","*.conf"),)                               #Кортеж отображаемых типов файлов
        file_path = filedialog.asksaveasfilename(
            title = "Сохранение конфигурации", 
            initialdir = "./", 
            defaultextension = ".conf", 
            initialfile = user[0]+".conf", 
            filetypes = types)                                                  #Вызов файлового диалога для сохранения файла 
        if not file_path:                                                     #Если получен пустой путь (окно было закрыто крестиком),
            return                                                              #процесс сохранения конфигурации отменяется.
        if self.file_config.seve_config(file_path, user, data):                 #Сохранение конфигурации в файл
            self.open_config(data)                                              #Открытие созданной конфигурации

    def edit_config(self):
        '''Метод редактирования файла конфигурации'''
        types = (("Файл конфигурации","*.conf"),)                               #Кортеж отображаемых типов файлов
        file_path = filedialog.askopenfilename(
                                title = "Редактирование конфигурации", 
                                initialdir = "./", filetypes = types)           #Вызов файлового диалога для открытия файла 
        if not file_path:                                                       #Проверка, был ли выбран файл конфигурации
            return
        pass_win = UserPassword(self, "Открытие конфигурации", "Открыть")       #Вызов окна запроса имени пользователя и пароля
        user_pass = pass_win.get_data()                                         #Запрос данных у окна запроса имени пользователя и пароля
        if not user_pass:                                                       #Если окно запроса имени пользователя и пароля вернуло пустой список
            return                                                              #Процесс создания конфигурации завершается
        if  self.file_config.read_config(file_path):                            #Чтение конфигурации из файла
            user = self.file_config.get_user()                                  #Получение данных пользователя от окна запроса 
            if user_pass[0]==user[0] and user_pass[1]==user[1]:                 #Если данные пользователя соответствуют данным конфигурации
                data = self.file_config.get_config()                            #Читаем данные конфигурации
            else:
                showinfo(title = "Отказ в доступе", 
                         message = "Неверное имя пользователя или пароль.")     #Выдается соответствующее сообщение в диалоговом окне
                return
        else:
                return  
        editer = Editor(self, "Редактирование конфигурации", data)              #Создание объекта для работы с данными конфигурации
        data = editer.get_data()
        if not data:                                                            #Если получен пустой словарь (окно было закрыто крестиком), 
            return                                                              #процесс создания конфигурации заканчивается.
        if self.file_config.seve_config(file_path, user, data):                 #Сохранение конфигурации в файл
            self.open_config(data)                                              #Открытие созданной конфигурации 
    def get_info(self):
        info = InfoWin(self)

    def forward(self):
        '''
        Метод обрабатывает нажатие кнопки "Вперед".
        Изменяет положение робота на поле при его движении вперед,
        а также отображает координаты положения робота.
        '''
        self.robot.make_move("forward")                                         #Выполнение команды "Вперед"
        position_x = self.robot.get_position_x()                                #Получение текущей координаты х робота
        position_y = self.robot.get_position_y()                                #Получение текущей координаты У робота
        orientation = self.robot.get_orientation()                              #Получение текущей ориентации робота
        self.field.change_robo(position_x, position_y, orientation)             #Изменение состояния робота на поле
        self.label_position["text"] = "Координаты: \tx = "+str(position_x)+ \
                                      "\ty = "+str(position_y)                  #Отображение текущих координат робота 

    def open_config(self, data: dict={}):
        '''
        Метод открытия файла конфигурации и запуска основной программы.
        :param data: словарь с данными конфигурации
        :type data: dict
                    {"width_field": int, "height_field": int,
                     "cords_robo_x": int, "cords_robo_y": int,
                     "orientation": str, "obstacles": list}
                     где "width_field" - ширина поля;
                         "height_field" - высота поля;
                         "cords_robo_x" - текущая координата х робота;
                         "cords_robo_y" - текущая координата y робота;
                         "orientation" - ориентация робота в пространстве;
                         "obstacles" - список координат препятствий, в формате
                                       [x, y].
        '''
        if not data:
            types = (("Файл конфигурации","*.conf"),)                           #Кортеж отображаемых типов файлов
            file_path=filedialog.askopenfilename(title="Открытие конфигурации", 
                      initialdir = "./", filetypes = types)                     #Вызов файлового диалога для открытия файла 
            if not file_path:                                                 #Проверка, был ли выбран файл конфигурации
                return
            pass_win = UserPassword(self, "Открытие конфигурации", "Открыть")   #Вызов окна запроса имени пользователя и пароля
            user_pass = pass_win.get_data()                                     #Запрос данных у класса окна
            if not user_pass:
                return
            if  self.file_config.read_config(file_path):                        #Чтение конфигурации из файла
                user = self.file_config.get_user()                              #Получение данных пользователя от окна запроса 
                if user_pass[0]==user[0] and user_pass[1]==user[1]:             #Если данные пользователя соответствуют данным конфигурации
                    data = self.file_config.get_config()                        #Читаем данные конфигурации
                else:
                    showinfo(title = "Отказ в доступе", 
                             message = "Неверное имя пользователя или пароль.") #Выдается соответствующее сообщение в диалоговом окне
                    return
            else:
                    return                                                     
        self.robot.set_field_width(data["width_field"])                         #Передача движку ширины поля
        self.robot.set_field_height(data["height_field"])                       #Передача движку высоты поля
        self.robot.set_position_x(data["cords_robo_x"])                         #Передача движку x координаты робота 
        self.robot.set_position_y(data["cords_robo_y"])                         #Передача движку y координаты робота 
        self.robot.set_orientation(data["orientation"])                         #Передача движку ориентации робота в пространстве
        self.robot.set_obstacles(data["obstacles"])                             #Передача движку массива препятствий
        self.robot.set_activ_flag()                                             #Разрешение работы движка (активизирует выполнение команд) 
        self.field.set_width(data["width_field"])                               #Передача ширины поля графическому объекту отображения
        self.field.set_height(data["height_field"])                             #Передача высоты поля графическому объекту отображения
        self.field.drow_obstacles(data["obstacles"])                            #Передача списка препятствий графическому объекту отображения
        self.field.change_robo(data["cords_robo_x"],data["cords_robo_y"],       
             data["orientation"])                                               #Отрисовка робота в текущей позиции
        self.field.set_robo_normal()                                            #Устанавливает видимость робота на поле
        self.label_position["text"] = "Координаты: \tx = "+ \
             str(data["cords_robo_x"])+"\ty = "+str(data["cords_robo_y"])       #Отображение координат робота в области состояния
        self.label_orientation["text"] = "Направление: \t"+ \
             self.orientation_convert_ru(self.robot.get_orientation())          #Отображение ориентации робота в области состояния

    def orientation_convert_ru(self, orientation: str) -> str:
        '''
        Метод выполняет конвертацию названия направления в русское.
        :param orientation: сторона света "n", "s", "e", "w".
        :type orientation: str
        :return: сторона света в русской аннотации "Север", "Юг", "Восток", "Запад"
        :rtype: str
        '''
        if orientation == "n":
            return "Север"
        if orientation == "s":
            return "Юг"
        if orientation == "w":
            return "Запад"
        if orientation == "e":
            return "Восток"  
        return "" 

    def turn_left(self):
        '''
        Метод обрабатывает нажатие кнопки "Повернуть влево".
        Выполняет поворот робота влево и изменяет отображаемую 
        ориентацию робота в пространстве.
        '''
        self.robot.make_move("left")                                            #Выполнение команды "Повернуть влево"
        self.label_orientation["text"] = "Направление: \t"+ \
             self.orientation_convert_ru(self.robot.get_orientation())          #Преобразование текущей ориентации робота в русское
        self.field.change_robo(self.robot.get_position_x(), 
             self.robot.get_position_y(), self.robot.get_orientation())         #Изменение состояния робота на поле

    def turn_right(self):
        '''
        Метод обрабатывает нажатие кнопки "Повернуть вправо".
        Выполняет поворот робота вправо и изменяет отображаемую 
        ориентацию робота в пространстве.
        '''
        self.robot.make_move("right")                                           #Выполнение команды "Повернуть вправо"
        self.label_orientation["text"] = "Направление: \t"+ \
             self.orientation_convert_ru(self.robot.get_orientation())          #Преобразование текущей ориентации робота в русское
        self.field.change_robo(self.robot.get_position_x(), 
             self.robot.get_position_y(), self.robot.get_orientation())         #Изменение состояния робота на поле


if __name__ == "__main__":                                                      #Начало основной программы
    app = MainWin()                                                             #Создание объекта главного класса программы
    app.mainloop()                                                              #Запуск бесконечного цикла обслуживания окна
