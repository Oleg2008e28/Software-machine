# filename: field.py
# -*- coding: utf-8 -*-

from tkinter import*

class Field(Canvas):
    '''Класс создания поля типа Canvas для визуализации перемещения'''
    def __init__(self, width_x: int, height_y: int , master=None, 
                 image=None, command=None, **config):
        """
        Конструктор класса игрового поля.
        :param width_x: ширина игрового поля
        :type width_x: int
        :param height_y: высота игрового поля
        :type height_y: int
        """
        super(Field, self).__init__(master=master, **config)
        self.field_width = width_x                                              #Ширина поля
        self.field_height = height_y                                            #Высота поля
        self.ITEM_SIZE = 50                                                     #Ширина одной клетки поля в пикселях
        self.obstacles=[]                                                       #Список координат препятствий
        self.config(bg="white")                                                 #Цвет поля белый
        self.config(width=self.ITEM_SIZE * width_x + 1)                         #Ширина одного сегмента поля в пикселях
        self.config(height=self.ITEM_SIZE * height_y + 1)                       #Высота одного сегмента поля в пикселях
        self.config(highlightthickness=0)                                       #Настройки рамки
        self.config(borderwidth=0)                                              #и отступа
        x = 0
        y = 0
        self.robo = self.create_polygon(self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE,
                                        self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                        self.ITEM_SIZE*x + self.ITEM_SIZE/2, 
                                        self.ITEM_SIZE*0.9 + y * self.ITEM_SIZE, 
                                        self.ITEM_SIZE*0.9 + x * self.ITEM_SIZE,
                                        self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                        self.ITEM_SIZE/2 + x * self.ITEM_SIZE,
                                        self.ITEM_SIZE*0.3 + y * self.ITEM_SIZE, 
                                        fill='green', outline = "black", 
                                        width = self.ITEM_SIZE*0.05 
                                        if self.ITEM_SIZE*0.05  > 1 else 1)     #Отрисовка фигуры робота
        self.itemconfig(self.robo, state='hidden')                              #Скрытие фигуры робота
        self.drow_greed()                                                       #Отрисовка сетки

    def change_robo(self, x: int, y: int, orientation: str):
        '''
        Метод выполняет отрисовку изменения состояния робота на поле.
        :param x: новая координата х робота
        :type x: int
        :param y: новая координата у робота
        :type y: int
        :param orientation: ориентация робота в пространстве
        :type orientation: str
        '''
        if orientation == "s":                                                  # Положение "s"
            self.coords(self.robo, self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE,     
                                   self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*x + self.ITEM_SIZE*0.5,       
                                   self.ITEM_SIZE*0.9 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.9 + x * self.ITEM_SIZE,     
                                   self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.5 + x * self.ITEM_SIZE,       
                                   self.ITEM_SIZE*0.3 + y * self.ITEM_SIZE)

        if orientation == "e":                                                  # Положение "e"
            self.coords(self.robo, self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE,
                                   self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE * 0.9 + x * self.ITEM_SIZE,
                                   self.ITEM_SIZE*0.5 + y * self.ITEM_SIZE,   
                                   self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.9 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.3 + x * self.ITEM_SIZE,
                                   self.ITEM_SIZE*y + self.ITEM_SIZE*0.5)
        if orientation == "n":                                                  # Положение "n"
            self.coords(self.robo, self.ITEM_SIZE*0.5 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.1 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE * 0.9 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE * 0.9 + y * self.ITEM_SIZE,   
                                   self.ITEM_SIZE*0.5 + x * self.ITEM_SIZE,   
                                   self.ITEM_SIZE*0.7 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*y + self.ITEM_SIZE * 0.9)
        if orientation == "w":                                                  # Положение "w"
            self.coords(self.robo, self.ITEM_SIZE*0.1 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.5 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE * 0.9 + x * self.ITEM_SIZE,
                                   self.ITEM_SIZE * 0.1 + y * self.ITEM_SIZE,   
                                   self.ITEM_SIZE*0.7 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.5 + y * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*0.9 + x * self.ITEM_SIZE, 
                                   self.ITEM_SIZE*y + self.ITEM_SIZE * 0.9)
 
    def drow_greed(self):
        '''Метод выполняет отрисовку сетки на поле'''
        for i in range(self.field_width + 1):                                   #Рисование вертикальных линий
            self.create_line(self.ITEM_SIZE*i, 0, self.ITEM_SIZE*i,\
                             self.ITEM_SIZE*self.field_height, fill = "grey")
        for i in range(self.field_height + 1):                                  #Рисование горизонтальных линий
            self.create_line(0, self.ITEM_SIZE*i, self.ITEM_SIZE*\
                             self.field_width, self.ITEM_SIZE*i, fill = "grey")

    def drow_obstacles(self, obstacles:list):
        '''
        Метод выполняет отрисовку препятствий на поле.
        :param obstacles: новая координата х робота
        :type obstacles: list, в формате [[x, y], [x, y]]
                         где х, у - координаты препятствия 
        '''
        for item in self.obstacles:                                             #Удаляем старые препятствия, если они есть
            for i in range(4):                                                  #Каждое препятствие - четыре полигона
                self.delete(item[i])                                            #Удаляем их все
        for item in obstacles:                                                  #Перебираем новый список препятствий
            x = item[0]                                                         #Берем координаты 
            y = item[1]
            poli_1 = self.create_polygon(self.ITEM_SIZE*x,
                                         self.ITEM_SIZE*y, 
                                         self.ITEM_SIZE*x,                        
                                         self.ITEM_SIZE + y * self.ITEM_SIZE , 
                                         self.ITEM_SIZE/2 + x * self.ITEM_SIZE,     
                                         self.ITEM_SIZE/2 + y * self.ITEM_SIZE, 
                                         fill='orange')                         #Отрисоввываем первый полигон
            poli_2 = self.create_polygon(self.ITEM_SIZE*x,                    
                                         self.ITEM_SIZE*y, 
                                         self.ITEM_SIZE + self.ITEM_SIZE*x,       
                                         self.ITEM_SIZE*y, 
                                         self.ITEM_SIZE/2 + self.ITEM_SIZE*x,     
                                         self.ITEM_SIZE/2 + self.ITEM_SIZE*y, 
                                         fill='red')                            #Отрисоввываем второй полигон
            poli_3 = self.create_polygon(self.ITEM_SIZE*x,
                                         self.ITEM_SIZE + y * self.ITEM_SIZE, 
                                         self.ITEM_SIZE + x * self.ITEM_SIZE,       
                                         self.ITEM_SIZE + y * self.ITEM_SIZE,
                                         self.ITEM_SIZE/2 + x * self.ITEM_SIZE,     
                                         self.ITEM_SIZE/2 + y * self.ITEM_SIZE, 
                                         fill='red')                            #Отрисоввываем третий полигон
            poli_4 = self.create_polygon(self.ITEM_SIZE + x * self.ITEM_SIZE, 
                                         self.ITEM_SIZE*y,
                                         self.ITEM_SIZE + x * self.ITEM_SIZE, 
                                         self.ITEM_SIZE + y * self.ITEM_SIZE,
                                         self.ITEM_SIZE/2 + x * self.ITEM_SIZE, 
                                         self.ITEM_SIZE/2 + y * self.ITEM_SIZE, 
                                         fill='orange')                         #Отрисоввываем четвертый полигон
            self.obstacles.append((poli_1, poli_2, poli_3, poli_4))             #Сохраняем ссылки в список

    def set_height(self, height_x: int):
        '''
        Метод устанавливает ширину поля.
        :param height_x: Высота игрового поля
        :type height_x: int 
        '''       
        self.field_height = height_x                                            #Сохранение значения в переменной класса
        self.config(height=self.ITEM_SIZE * height_x + 1)                       #Изменение высоты холста
        self.drow_greed()                                                       #Отрисовка сетки

    def set_robo_hidden(self): 
        '''Метод скрывает робота на поле'''
        self.itemconfig(self.robo, state='hidden')

    def set_robo_normal(self):
        '''Метод устанавливает видимость робота на поле'''
        self.itemconfig(self.robo, state='normal')

    def set_width(self, width_x: int):
        '''
        Метод устанавливает ширину поля.
        :param width_x: Ширина игрового поля
        :type width_x: int 
        ''' 
        self.field_width = width_x                                              #Сохранение значения в переменной класса
        self.config(width=self.ITEM_SIZE * width_x + 1)                         #Изменение ширины холста
        self.drow_greed()                                                       #Отрисовка сетки
