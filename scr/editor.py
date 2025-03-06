# filename: editor.py
# -*- coding: utf-8 -*-

from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog

from validator import Validator

class Editor(Toplevel):
    '''Класс окна редактора конфигураций конечного автомата.'''

    def __init__(self, parent, Title_Name: str, data: dict={}):
        super().__init__(parent)
        '''
        Конструктор объекта окна редактора конфигураций конечного автомата.
        :param Title_Name: заголовок окна
        :type Title_Name: str
        :param data: словарь, содержащий параметры конфигурации
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
        self.weight_field = 0                                                      #Ширина поля
        self.height_field = 0                                                      #Высота поля
        self.cords_robo_x = 0                                                      #Координата x положения робота
        self.cords_robo_y = 0                                                      #Координата y положения робота
        self.orientation = ""                                                    #Ориентация робота в пространстве
        self.obstacles_list=[]                                                     #Список препятствий
        self.result={}
        self.resizable(False, False)                                               #Запрет на изменение размеров пользователем
        self.title(Title_Name)                                                     #Установка заголовка окна
        self.entry_obstacle_x = StringVar()
        self.entry_obstacle_y = StringVar()
        self.entry_size_width = StringVar()
        self.entry_size_height = StringVar()
        self.entry_cords_robo_x = StringVar()
        self.entry_cords_robo_y = StringVar()
        self.combobox_ORIENTATIONS_RU = StringVar()
        
        label_size_field = Label(self, text="Размер поля (ширина х высота):")
        label_size_field.grid(row=0, column=0, sticky="w", padx=[30,0], pady=10)
        label_width_field = Label(self, text="Ширина = ")
        label_width_field.grid(row=0, column=1, sticky="w", padx=[0,0], pady=10)
        entry_size_width = Entry(self, textvariable=self.entry_size_width)
        entry_size_width.grid(row=0, column=2, sticky=W+E, padx=[0,30], pady=10)
        label_height_field = Label(self, text="Высота = ")
        label_height_field.grid(row=1, column=1, sticky="w", padx=[0,0], 
                                pady=10)
        entry_size_height = Entry(self,textvariable=self.entry_size_height)
        entry_size_height.grid(row=1, column=2, sticky=W+E, padx=[0,30], 
                               pady=10)
        label_cords_robo = Label(self, text="Исходные координаты робота:")
        label_cords_robo.grid(row=2, column=0, sticky="w", padx=[30,0], 
                              pady=10)
        label_cords_robo_x = Label(self,text = "x = ")
        label_cords_robo_x.grid(row=2, column=1, sticky="w")
        entry_cords_robo_x = Entry(self,textvariable=self.entry_cords_robo_x)
        entry_cords_robo_x.grid(row=2, column=2, sticky=W+E, padx=[0,30], 
                                pady=10)
        label_cords_robo_y = Label(self,text="y = ")
        label_cords_robo_y.grid(row=3, column=1, sticky="w")
        entry_cords_robo_y = Entry(self,textvariable=self.entry_cords_robo_y)
        entry_cords_robo_y.grid(row=3, column=2, sticky=W+E, padx=[0,30], 
                                pady=10)
        label_orientation = Label(self,text="Исходные положение робота:")
        label_orientation.grid(row=4, column=0, sticky="w", padx=[30,0], 
                                 pady=10)
        ORIENTATIONS_RU = ("Север", "Юг", "Восток", "Запад")
        combobox_ORIENTATIONS_RU = ttk.Combobox(self, values=ORIENTATIONS_RU, 
                                    state="readonly", 
                                    textvariable=self.combobox_ORIENTATIONS_RU)
        combobox_ORIENTATIONS_RU.grid(row=4, column=2, sticky=W, padx=[0,30], 
                                      pady=10)
        label_cords_obstacle = Label(self,text="Координаты препятствия:    ")
        label_cords_obstacle.grid(row=5, column=0, sticky="w", padx=[30,0], 
                                  pady=10)
        label_cords_obstacle_x = Label(self,text="x = ")
        label_cords_obstacle_x.grid(row=5, column=1, sticky="w")
        entry_cords_obstacle_x = Entry(self, textvariable=self.entry_obstacle_x)
        entry_cords_obstacle_x.grid(row=5, column=2, sticky=W+E, padx=[0,30], 
                                    pady=10)
        label_cords_obstacle_y = Label(self,text="y = ")
        label_cords_obstacle_y.grid(row=6, column=1, sticky="w")
        entry_cords_obstacle_y = Entry(self, textvariable=self.entry_obstacle_y)
        entry_cords_obstacle_y.grid(row=6, column=2, sticky=W+E, padx=[0,30], 
                                    pady=10)
        label_list_obstacles = Label(self,text="Список препятствий:")
        label_list_obstacles.grid(row=7, column=0, sticky="w", padx=[30,0], 
                                  pady=10)
        self.listbox_obstacles = Listbox(self)
        self.listbox_obstacles.grid(row=8, column=0, sticky=S+N+W+E, rowspan=2, 
                                    columnspan=2, padx=[30,0])
        scrollbar = ttk.Scrollbar(self, orient="vertical", 
                                  command=self.listbox_obstacles.yview)
        scrollbar.grid(row=8, rowspan=2, column=1, sticky=E+N+S)
        self.listbox_obstacles["yscrollcommand"]=scrollbar.set
        button_del  = Button(self, text = "Удалить", command = self.but_delete)
        button_del.grid(row=9, column=2, sticky=W+E, padx=[30,30], pady=10)
        button_add  = Button(self, text="Добавить", command=self.but_add)
        button_add.grid(row=8, column=2, sticky=W+E, padx=[30,30], pady=10)
        button_save  = Button(self, text="Сохранить", command=self.but_save)
        button_save.grid(row=11, column=0, sticky=W+E, columnspan=2, 
                         padx=[30,0], pady=10)
        width_screen = self.winfo_screenwidth()                                 #Ширина экрана
        height_screen = self.winfo_screenheight()                               #Высота экрана
        self.update()                                                           #Вычисление параметров создаваемого окна
        width_win = self.winfo_width()                                          #Запрос ширины окна
        height_win = self.winfo_height()                                        #Запрос высоты окна
        x = width_screen//2 - width_win//2                                      #Координата x левого верхнего угла окна
        y = height_screen//2 - height_win//2                                    #Координата y левого верхнего угла окна
        self.geometry('+{}+{}'.format(x, y))                                    #Размещение окна по центру экрана
        self.focus_set()                                                        #Передать фокус окну
        if data:                                                                #Если словарь входных данных не пустой
            self.weight_field = data["width_field"]                             #Заполняем переменные переданными значениями
            self.height_field = data["height_field"]                                                      
            self.cords_robo_x = data["cords_robo_x"]                                                      
            self.cords_robo_y = data["cords_robo_y"]                                                      
            self.orientation = data["orientation"]                                                    
            self.obstacles_list = data["obstacles"]
            entry_size_width.insert(0, str(self.weight_field))                  #Заполняем поля ввода на форме
            entry_size_height.insert(0, str(self.height_field))
            entry_cords_robo_x.insert(0, str(self.cords_robo_x))
            entry_cords_robo_y.insert(0, str(self.cords_robo_y))
            if self.orientation == "n":
                combobox_ORIENTATIONS_RU.set(ORIENTATIONS_RU[0])
            elif self.orientation == "s":
                combobox_ORIENTATIONS_RU.set(ORIENTATIONS_RU[1])
            elif self.orientation == "e":
                combobox_ORIENTATIONS_RU.set(ORIENTATIONS_RU[2])
            elif self.orientation == "w":
                combobox_ORIENTATIONS_RU.set(ORIENTATIONS_RU[3])
            self.creat_list_box(self.obstacles_list, self.listbox_obstacles)

    def but_delete(self):
        '''
        Метод удаляет препятствие из списка препятствий 
        '''
        if len(self.obstacles_list) > 0:
            s = self.listbox_obstacles.curselection()                           #Получение выделенного препятствия из списка listbox
            for i in s:
                self.obstacles_list.pop(i)                                      #Удаление выбранных записей из списка препятствий 
            self.creat_list_box(self.obstacles_list, self.listbox_obstacles)    #Обновление содержимого списка listbox

    def but_add(self):
        '''
        Метод формирует список препятствий для отображения в виджете формы.
        :param in_list: список координат препятствий
        :type in_list: list, в формате [x: int, y:int]
                       где x, y - координаты препятствия;
        :param out_list_box: список препятствий
        :type out_list_box: list, в формате "Препятствие [x:y]"
                       где x, y - координаты препятствия;
        '''  
        try:
            x = int(self.entry_obstacle_x.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                message = 'Некорректные данные в поле '
                          '"Координата x препятствия"!', parent=self)
            return
        try:
            y = int(self.entry_obstacle_y.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                message = 'Некорректные данные в поле '
                          '"Координата y препятствия"!', parent=self)
            return
        if [x, y] not in self.obstacles_list:
            if x >= 0 and y >= 0:
                self.obstacles_list.append([x, y])
                self.creat_list_box(self.obstacles_list, self.listbox_obstacles)
            else:
                showinfo(title = "Ошибка ввода", 
                         message = "Для координат препятствия введено "
                                   "\nотридцательное значение!", parent=self)
        else:
            showinfo(title = "Ошибка ввода", 
                     message = "Препятствие с заданными координатами "
                               "\nуже существует!", parent=self)

    def but_save(self):
        try:
            self.weight_field = int(self.entry_size_width.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                     message = 'Некорректные данные в поле "Ширина поля"!', \
                     parent=self)
            return
        try:
            self.height_field = int(self.entry_size_height.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                     message = 'Некорректные данные в поле "Высота поля"!', \
                     parent=self)
            return
        try:
            self.cords_robo_x = int(self.entry_cords_robo_x.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                message = 'Некорректные данные в поле "Координата х робота"!', \
                parent=self)
            return
        try:
            self.cords_robo_y = int(self.entry_cords_robo_y.get())
        except ValueError:
            showinfo(title = "Ошибка ввода", 
                message = 'Некорректные данные в поле "Координата y робота"!', \
                parent=self)
            return
        if self.combobox_ORIENTATIONS_RU.get() == "Север":
            self.orientation = "n"
        elif self.combobox_ORIENTATIONS_RU.get() == "Юг":
            self.orientation = "s"
        elif self.combobox_ORIENTATIONS_RU.get() == "Восток":
            self.orientation = "e"
        elif self.combobox_ORIENTATIONS_RU.get() == "Запад":
            self.orientation = "w"
        result = {"width_field":self.weight_field, 
                  "height_field":self.height_field, 
                  "cords_robo_x":self.cords_robo_x, 
                  "cords_robo_y":self.cords_robo_y, 
                  "orientation":self.orientation, 
                  "obstacles":self.obstacles_list}
        valodator = Validator(result)
        if valodator.check_and_show_massage():
            self.result = result
            self.destroy()  

    def creat_list_box(self, in_list: list, out_list_box: list):
        '''
        Метод формирует список препятствий для отображения в виджете формы.
        :param in_list: список координат препятствий
        :type in_list: list, в формате [x: int, y:int]
                       где x, y - координаты препятствия;
        :param out_list_box: список препятствий
        :type out_list_box: list, в формате "Препятствие [x:y]"
                       где x, y - координаты препятствия;
        '''
        size = out_list_box.size()
        out_list_box.delete(0, size)
        for item in in_list:
            s = "Препятствие [" + str(item[0]) + ":" + str(item[1]) +"]"
            out_list_box.insert(END, s)

    def get_data(self) -> dict:
        '''
        Метод запроса данных конфигурации.
        :return: Словарь, содержащий данные конфигурации.
        :type data: dict {"width_field": int, "height_field": int,
                          "cords_robo_x": int, "cords_robo_y": int,
                          "orientation": str, "obstacles": list}
                          где "width_field" - ширина поля;
                              "height_field" - высота поля;
                              "cords_robo_x" - текущая координата х робота;
                              "cords_robo_y" - текущая координата y робота;
                              "orientation" - ориентация робота в пространстве;
                              "obstacles" - список координат препятствий, в 
                                            формате [x, y]. 
        '''        
        self.grab_set()                                                         #Захват пользовательского ввода окном верхнего уровня
        self.wait_window()                                                      #Ожидание закрытия окна ввода имени пользователя и пароля
        return self.result                                                      #Возвращение словаря с данными пользователя
