# filename: validator.py
# -*- coding: utf-8 -*-

from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo

class Validator():
    '''Класс для проверки данных, введённых пользователем'''
    def __init__(self, data:dict={}):
        '''
        Конструктор класса.
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
        self.weight_field = 0                                                   #Ширина поля
        self.height_field = 0                                                   #Высота поля
        self.cords_robo_x = 0                                                   #Координата x положениея робота
        self.cords_robo_y = 0                                                   #Координата y положениея робота
        self.position_robo = ""                                                 #Ориентация робота в пространстве
        self.obstacles_list=[]                                                  #Список препятствий
        if data:
            self.weight_field = data["width_field"]                             #Заполняем переменные переданными значениями
            self.height_field = data["height_field"]                                                      
            self.cords_robo_x = data["cords_robo_x"]                                                      
            self.cords_robo_y = data["cords_robo_y"]                                                      
            self.position_robo = data["orientation"]                                                    
            self.obstacles_list=data["obstacles"]

    def check(self, show_mass:bool=False):
        '''
        Метод выполняет проверку данных, переданных объекту Validator.
        :param show_mass: флаг разрешения выдавать сообщения massegebox
        :type show_mass: bool
        '''
        print("Проверка запущена")
        if self.weight_field < 1:                                               #Проверка ширины поля
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Некорректно задана ширина поля!")    
            return False                                                
        if self.height_field < 1:                                               #Проверка высоты поля
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Некорректно задана высота поля!")
            return False
        if self.cords_robo_x >=self.weight_field:                               #Проверка координаты х робота на выход за пределы поля
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Координата х положения робота "
                               "выходит за переделы поля!")
            return False
        if self.cords_robo_x < 0:                                               #Проверка координаты х робота на отрицательное число
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Координата х положения робота "
                               "отрицательное число!")
            return False
        if self.cords_robo_y >=self.height_field:                               #Проверка координаты у робота на выход за пределы поля
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Координата y положения робота "
                               "выходит за переделы поля!")
            return False
        if self.cords_robo_y < 0:                                               #Проверка координаты у робота на отрицательное число
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Координата y положения робота "
                               "отрицательное число!")
            return False
        orientation = ("n", "s", "e", "w")
        if  self.position_robo not in orientation:                              #Проверка на корректность значений ориентации в пространстве
            lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Ориентация робота в пространстве "
                               "не соответствует допустимым значениям!")
            return False
        for item in  self.obstacles_list:                                       #Проверка на корректность данных в списке препятствий
            if item[0] >= self.weight_field:
                lambda: show_mass, showinfo(title = "Ошибка ввода", 
                                   message = "Координата х препятствия "
                                   "[{},{}] выходит за пределы поля!"
                                   .format(item[0],item[1]))
                return False
            if item[0] < 0:
                lambda: show_mass, showinfo(title = "Ошибка ввода", 
                                   message = "Координата х препятствия "
                                   "[{},{}] отрицательное число!"
                                   .format(item[0],item[1]))
                return False            
            if item[1] >= self.height_field:
                lambda: show_mass, showinfo(title = "Ошибка ввода", 
                                   message = "Координата y препятствия "
                                   "[{},{}] выходит за пределы поля!"
                                   .format(item[0],item[1]))
                return False
            if item[1] < 0:
                lambda: show_mass, showinfo(title = "Ошибка ввода", 
                                   message = "Координата y препятствия "
                                   "[{},{}] отрицательное число!"
                                   .format(item[0],item[1]))
                return False            
            if item[0]==self.cords_robo_x and item[1]==self.cords_robo_y:
                lambda: show_mass, showinfo(title = "Ошибка ввода", 
                               message = "Положение препятствия [{},{}] "
                               "совпадает с положением робота!"
                               .format(item[0],item[1]))
                return False  
        return True

    def check_and_show_massage(self):
        '''
        Метод выполняет проверку данных, переданных объекту Validator и
        выводит сообщения по результатам проверки с помощью объектов massegebox.
        '''
        return self.check(True)       

    def get(self) -> dict: 
        '''
        Метод возвращает данные, ранее переданные объекту Validator.
        :return: словарь с данными конфигурации
        :rtype: dict, формата
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
        result = {"width_field":self.weight_field, 
                  "height_field":self.height_field, 
                  "cords_robo_x":self.cords_robo_x, 
                  "cords_robo_y":self.cords_robo_y, 
                  "orientation":self.position_robo, 
                  "obstacles":self.obstacles_list}
        return result

    def set(self, data: dict):
        '''
        Метод передачи объекту валидатор данных для проверки.
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
        if data:
            self.weight_field = data["width_field"]                             #Заполняем переменные переданными значениями
            self.height_field = data["height_field"]                                                      
            self.cords_robo_x = data["cords_robo_x"]                                                      
            self.cords_robo_y = data["cords_robo_y"]                                                      
            self.position_robo = data["orientation"]                                                    
            self.obstacles_list=data["obstacles"]
