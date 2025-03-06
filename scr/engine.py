# filename: engine.py
# -*- coding: utf-8 -*-


from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo

class Engine():
    '''Класс имитирующий работу программного автомата'''
    def __init__(self, width_x: int=1, heigth_y: int=1, position_x: int=0, 
                 position_y: int=0, orientation: str="n", obstacles: list=[]):   
        '''
        Конструктор объекта движка для управления перемещением робота.
        :param width_x: ширина игрового поля
        :type width_x: int
        :param heigth_y: высота игрового поля
        :type heigth_y: int
        :param position_x: текущая координата х робота
        :type position_x: int        
        :param position_y: текущая координата у робота
        :type position_y: int 
        :param orientation: ориентация робота в пространстве
        :type orientation: str ("e", "s", "w", "n")
        :param obstacles: список препятствий
        :type obstacles: list, формата [[x: int, y: int], [x: int ,y: int]]
                         где х, у - координаты препятствия
        '''
        self.ORIENTATION = ("e", "s", "w", "n")                                 #Перечень допустимых команд для ориентации в пространстве     
        if width_x < 1:                                                         #Проверка значения переданного аргумента width_x
            raise InvalidEngineValue("Ошибка! Аргумент width_x конструктора "
                                     "класса Engine меньше 1")                  #Генерация исключения
        if heigth_y < 1:                                                        #Проверка значения переданного аргумента heigth_y
            raise InvalidEngineValue("Ошибка! Аргумент heigth_y конструктора "
                                     "класса Engine меньше 1")                  #Генерация исключения
        self.width_x = width_x                                                  #Ширина поля
        self.heigth_y = heigth_y                                                #Высота поля
        if position_x < 0:                                                      #Проверка значения переданного аргумента position_x
            raise InvalidEngineValue("Ошибка! Аргумент position_x конструктора "
                                     "set_position_x класса Engine меньше 0")   #Генерация исключения
        if position_x >= self.width_x:  
            raise InvalidEngineValue("Ошибка! Аргумент position_x конструктора "
                                     "set_position_x класса Engine больше "
                                     "или равен width_x")                       #Генерация исключения
        if position_y < 0:                                                      #Проверка значения переданного аргумента position_y
            raise InvalidEngineValue("Ошибка! Аргумент position_y конструктора "
                                     "set_position_y класса Engine меньше 0")   #Генерация исключения
        if position_y >= self.heigth_y:  
            raise InvalidEngineValue("Ошибка! Аргумент position_y конструктора "
                                     "set_position_y класса Engine больше "
                                     "или равен width_y")                       #Генерация исключения
        self.position_x = position_x                                            #Текущая координата x робота
        self.position_y = position_y                                            #Текущая координата y робота
        if orientation not in self.ORIENTATION:                                 #Проверка значения переданного аргумента orientation
            raise InvalidEngineValue("Ошибка! Неверный аргумент orientation "
                                     "конструктора класса Engine")              #Генерация исключения
        self.orientation = orientation                                          #Ориентация в пространстве
        for item in obstacles:                                                  #Проверка типа переданного аргумента obstacles
            if len(item) != 2:
                raise InvalidEngineValue("Ошибка! Неверный формат аргумента "
                                         "obstacles конструктора "
                                         "класса Engine")                       #Генерация исключения
            if type(item[0]) != int or type(item[1]) != int:
                raise InvalidEngineValue("Ошибка! Задано не int значение в "
                                         "качестве координат препятствия "
                                         "метода конструктора класса Engine")   #Генерация исключения
            if item[0] < 0 or item[1] < 0:
                raise InvalidEngineValue("Ошибка! Задано отрицательное "
                                         "значение в качестве координат "
                                         "препятствия конструктора "
                                         "класса Engine")                       #Генерация исключения
            if item[0] >= self.width_x or item[1] >= self.heigth_y:
                raise InvalidEngineValue("Ошибка! Положение препятствия "
                                         "конструктора класса Engine "
                                         "выходит за границы игрового поля ")   #Генерация исключения
        self.obstacles = obstacles                                              #Список координат препятствий                                           
        self.COMMANDS = ("left", "right", "forward")                            #Перечень допустимых команд для робота
        self.activ_flag = False                                                 #Флаг определяет активен ли движок или нет

    def get_cords(self) -> tuple:
        '''
        Метод возвращает текущие координаты робота.
        :return: текущие координаты робота
        :rtype: tuple (x, y)
                где x,y - координаты робота
        '''
        return (self.position_x, self.position_y)    

    def get_field_height(self) -> int:
        '''
        Метод возвращает высоту поля.
        :return: высота игрового поля 
        :rtype: int
        '''
        return self.heigth_y

    def get_field_width(self) -> int:
        '''
        Метод возвращает ширину поля.
        :return: ширина игрового поля 
        :rtype: int
        '''
        return self.width_x

    def get_obstacles(self) -> list:
        '''
        Метод возвращает массив координат препятствий.
        :return: список препятствий 
        :rtype: list, формата [[x: int, y: int], [x: int, y: int]]
                где х, у - координаты препятствий
        '''
        return self.obstacles

    def get_orientation(self) -> str:
        '''
        Метод возвращает ориентацию робота в пространстве.
        :return: ориентация робота в пространстве 
        :rtype: str ("e", "s", "w", "n")
        '''
        return self.orientation

    def get_position_x(self) -> int:
        '''
        Метод возвращает текущую координату х робота.
        :return: текущая координата х 
        :rtype: int
        '''
        return self.position_x

    def get_position_y(self) -> int:
        '''
        Метод возвращает текущую координату y робота.
        :return: текущая координата y 
        :rtype: int
        '''
        return self.position_y    

    def make_move(self, command: str):
        '''
        Метод, выполняющий изменение состояния робота.
        :param command: команда, отдаваемая автомату
        :type command: srt ("left", "right", "forward")
        '''
        if self.activ_flag:                                                     #Проверка разрешения работы движка
            if command not in self.COMMANDS:                                    #Проверка переданной команды
                print("Ошибка! Неверная команда для класса Engine.")            #Сообщение об ошибке
                exit()                                                          #Завершение приложения
            if command == "left":                                               #Обработка команды "Повернуть на лево"
                if self.orientation == "e":
                    self.orientation = "n"
                elif self.orientation == "n":
                    self.orientation = "w"
                elif self.orientation == "w":
                    self.orientation = "s"
                elif self.orientation == "s":
                    self.orientation = "e"
            if command == "right":                                              #Обработка команды "Повернуть на право"
                if self.orientation == "e":
                    self.orientation = "s"
                elif self.orientation == "s":
                    self.orientation = "w"
                elif self.orientation == "w":
                    self.orientation = "n"
                elif self.orientation == "n":
                    self.orientation = "e"
            if command == "forward":                                            #Обработка команды "Сделать шаг вперед"
                if self.orientation == "e":                                     #Если ориентация робота "e"->Восток 
                    if self.position_x + 1 >= self.width_x:                     #Проверка на взаимодействие с правым краем поля
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в правый край поля!")       #Сообщение уперся в правый край поля
                    elif [self.position_x + 1, self.position_y] \
                          in self.obstacles:                                    #Проверка на взаимодействие с препятствием справа
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в препятствие справа!")     #Сообщение уперся в препятствие справа
                    else:
                        self.position_x += 1                                    #Сместить текущее положение вправо

                elif self.orientation == "s":                                   #Если ориентация робота "s"->Юг 
                    if self.position_y + 1 >= self.heigth_y:                    #Проверка на взаимодействие с нижним краем поля
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в нижний край поля!")       #Сообщение уперся в нижний край поля
                    elif [self.position_x, self.position_y + 1] \
                          in self.obstacles:                                    #Проверка на взаимодействие с препятствием снизу
                          showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в препятствие снизу!")      #Сообщение уперся в препятствие снизу
                    else:
                        self.position_y += 1                                    #Сместить текущее положение вниз

                elif self.orientation == "w":                                   #Если ориентация робота "w"->Запад 
                    if self.position_x - 1 < 0:
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в левый край поля!")        #Сообщение уперся в левый край поля
                    elif [self.position_x - 1, self.position_y] \
                          in self.obstacles:
                          showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в препятствие слева!")      #Сообщение уперся в препятствие слева
                    else:
                        self.position_x -= 1                                    #Сместить текущее положение влево
                
                elif self.orientation == "n":                                   #Если ориентация робота "n"->Север
                    if self.position_y - 1 < 0: 
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в верхний край поля!")      #Сообщение уперся в верхний край поля
                    elif [self.position_x, self.position_y - 1] \
                          in self.obstacles:
                        showinfo(title = "Взаимодействие с объектом", 
                            message = "Робот уперся в препятствие сверху!")     #Сообщение уперся в препятствие сверху
                    else:
                        self.position_y -= 1                                    #Сместить текущее положение вверх

    def set_activ_flag(self):
        '''
        Метод разрешает работу движка.
        '''
        self.activ_flag = True

    def set_field_height(self, heigth_y: int):
        '''
        Метод устанавливает высоту поля.
        :param heigth_y: ширина игрового поля
        :type heigth_y: int
        '''
        if heigth_y < 1:                                                        #Проверка значения переданного аргумента heigth_y
            raise InvalidEngineValue("Ошибка! Аргумент heigth_y метода "
                                     "set_field_height класса Engine меньше 1") #Генерация исключения
        self.heigth_y = heigth_y 

    def set_field_width(self, width_x: int):
        '''
        Метод устанавливает ширину поля.
        :param width_x: ширина игрового поля
        :type width_x: int
        '''
        if width_x < 1:                                                         #Проверка значения переданного аргумента width_x
            raise InvalidEngineValue("Ошибка! Аргумент width_x метода "
                                     "set_field_width класса Engine меньше 1")  #Генерация исключения
        self.width_x = width_x

    def set_obstacles(self, obstacles: list):
        '''
        Метод устанавливает препятствия.
        :param obstacles: список препятствий 
        :type obstacles: list, ормата [[x: int, y: int], [x: int, y: int]]
                         где х, у - координаты препятствий
        '''
        for item in obstacles:                                                  #Проверка типа переданного аргумента obstacles
            if len(item) != 2:
                raise InvalidEngineValue("Ошибка! Неверный формат аргумента "
                                         "obstacles метода set_obstacles "
                                         "класса Engine")                       #Генерация исключения
            if type(item[0]) != int or type(item[1]) != int:
                raise InvalidEngineValue("Ошибка! Задано не int значение в "
                                         "качестве координат препятствия "
                                         "метода set_obstacles класса Engine")  #Генерация исключения
            if item[0] < 0 or item[1] < 0:
                raise InvalidEngineValue("Ошибка! Задано отрицательное "
                                         "значение в качестве координат "
                                         "препятствия метода set_obstacles "
                                         "класса Engine")                       #Генерация исключения
            if item[0] >= self.width_x or item[1] >= self.heigth_y:
                raise InvalidEngineValue("Ошибка! Положение препятствия "
                                         "метода set_obstacles класса Engine "
                                         "выходит за границы игрового поля ")   #Генерация исключения
        self.obstacles = obstacles

    def set_orientation(self, orientation: str):
        '''
        Метод устанавливает ориентацию робота в пространстве.
        :param orientation: ширина игрового поля
        :type orientation: str
        '''
        if orientation not in self.ORIENTATION:                                 #Проверка значения переданного аргумента orientation
            raise InvalidEngineValue("Ошибка! Неверный аргумент orientation "
                                     "метода set_orientation класса Engine")    #Генерация исключения
        self.orientation = orientation

    def set_position_x(self, position_x: int):
        '''
        Метод устанавливает координату х положения робота.
        :param position_x: ширина игрового поля
        :type position_x: int
        '''
        if position_x < 0:                                                      #Проверка значения переданного аргумента position_x
            raise InvalidEngineValue("Ошибка! Аргумент position_x метода "
                                     "set_position_x класса Engine меньше 0")   #Генерация исключения
        if position_x >= self.width_x:  
            raise InvalidEngineValue("Ошибка! Аргумент position_x метода "
                                     "set_position_x класса Engine больше "
                                     "или равен width_x")                       #Генерация исключения
        self.position_x = position_x

    def set_position_y(self, position_y: int):
        '''
        Метод устанавливает координату у положения робота.
        :param position_у: ширина игрового поля
        :type position_у: int
        '''
        if position_y < 0:                                                      #Проверка значения переданного аргумента position_y
            raise InvalidEngineValue("Ошибка! Аргумент position_y метода "
                                     "set_position_y класса Engine меньше 0")   #Генерация исключения
        if position_y >= self.heigth_y:  
            raise InvalidEngineValue("Ошибка! Аргумент position_y метода "
                                     "set_position_y класса Engine больше "
                                     "или равен width_y")                       #Генерация исключения
        self.position_y = position_y

    def set_unactiv_flag(self):
        '''
        Метод останавливает работу движка.
        '''
        self.activ_flag = False


class InvalidEngineValue(ValueError):
    '''Класс исключений для обработки некорректных данных'''
    def __init__(self, message):
        super().__init__(message)
        self.msgfmt = message
