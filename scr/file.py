# filename: file.py
# -*- coding: utf-8 -*-

import hashlib

from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo

class File():
    '''
    Класс для записи и чтения данных конфигурации из файла
    '''
    def __init__(self):
        '''
        Конструктор класса File
        '''
        self.data = {}                                                          #Словарь для хранения данных конфигурации
        self.status = False                                                     #Флаг для хранения результата операции
        self.lines = []                                                         #Список для построчного прочтения файла

    def get_config(self) -> dict:
        '''
        Метод возвращает данные конфигурации.
        :return: данные конфигурации
        :rtype: dict
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
        words = self.lines[2].split()                                           #Разбиение второй строки файла на слова
        field_width = int(words[0])                                             #Преобразование число ширины игрового поля
        field_height = int(words[1])                                            #Преобразование в число высоты игрового поля
        orientation = words[4]                                                  #Извлечение положения робота в пространстве
        position_x = int(words[2])                                              #Преобразование в число координаты x робота
        position_y = int(words[3])                                              #Преобразование в число координаты y робота
        words = self.lines[3].split()                                           #Разбиение третьей строки файла на слова
        temp=[]                                                                 #Временная переменная для формирования списка препятствий
        obstacles=[]                                                            #Список с координатами препятствий
        for i, item in enumerate(words):                                        #Преобразование строки в список координат препятствий
            value = int(item)
            temp.append(value) 
            if i%2 == 1:
                obstacles.append(temp[:])
                temp.clear()
        return {"width_field":field_width, 
                "height_field":field_height, 
                "cords_robo_x":position_x, 
                "cords_robo_y":position_y, 
                "orientation": orientation, 
                "obstacles":obstacles}                                          #Возврат данных прочитанной конфигурации
   
    def get_user(self) -> list:
        '''
        Метод возвращает данные пользователя (имя и хэш-сумму пароля).
        :return: данные пользователя
        :rtype: list, формата [user_name, hash_password].
        '''
        return [self.lines[0].strip(), self.lines[1].strip()]

    def read_config(self, file_path:str) -> bool:
        '''
        Метод считывает конфигурацию из файла
        :param file_path: путь к файлу конфигурации
        :type file_path: str
        :return: статус исполнения если успешно True, если нет - False
        :rtype: bool
        '''
        self.status = False
        try:
            with open (file_path, "r", encoding = "utf-8") as file_input:       #Открытие текстового файла для чтения
                self.lines  = file_input.readlines()                            #Построчное чтение файла
        except FileNotFoundError:                                               #Обработка исключения при открытии файла                                     
                showinfo(title = "Файл не найден", 
                         message = "Неверно указано имя пользователя.")         #Выдается соответствующее сообщение в диалоговом окне
                return self.status
        if not self.lines:
            showinfo(title = "Файл конфигурации", 
                     message = "Невозможно открыть файл конфигурации, "
                     "\nфайл пуст!")                                            #Выдается соответствующее сообщение в диалоговом окне
            return self.status                                                  #Если список строк пуст (файл пуст), выход из метода
        file_string = ""                                                        #Строка для хеширования содержимого файла
        for i in range(len(self.lines)-1):                                      #Помещение всех данных из файл в строку
            file_string += self.lines[i].strip()+"\n"
        file_hash = hashlib.md5(file_string.encode()).hexdigest()               #Хэширование содержимого файла алгоритмом MD-5
        if file_hash == self.lines[len(self.lines)-1].strip():                  #Проверка соответствия хэш-суммы файла на соответствие
            self.status = True
        else:
            showinfo(title = "Файл конфигурации", 
                     message = "Невозможно открыть файл конфигурации, "
                     "\nданные в файле повреждены! .")                          #Выдается соответствующее сообщение в диалоговом окне
        return self.status

    def seve_config(self, file_path:str, user:list, data:dict) -> bool:
        '''
        Метод сохраняет конфигурацию в файл.
        :param file_path: путь к файлу конфигурации
        :type file_path: str
        :param user: имя пользователя и хэш-пароля
        :type user: list, формата [user_name, hash_password]
        :param data: данные конфигурации
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
        :return: статус исполнения если успешно True, если нет - False 
        :rtype: bool
        '''
        file_string = ""                                                        #Строка для хеширования содержимого файла
        file_string = user[0]+"\n"+ user[1]+"\n"+str(data["width_field"])+" "\
                    +str(data["height_field"])+" "+str(data["cords_robo_x"])\
                    +" "+str(data["cords_robo_y"])+" "\
                    +str(data["orientation"])+"\n"                              #Помещение всех данных для записи в файл в строку
        for i, item in enumerate(data["obstacles"]):                            #Помещение в строку списка препятствий
            file_string += str(item[0])+" "+ str(item[1])
            if i < len(data["obstacles"])-1:
                            file_string +=" "
        file_string += "\n"
        file_hash = hashlib.md5(file_string.encode()).hexdigest()               #Хэширование содержимого файла алгоритмом MD-5
        file_string += file_hash                                                #Добавление хэш-суммы к данным для записи в файл
        try:
            with open (file_path, "w", encoding = "utf-8") as file_out:         #Открытие файла для записи
                file_out.write(file_string)                                     #Запист данных конфигурации в файл
        except FileNotFoundError:                                               #Обработка исключения при открытии файла                                     
            showinfo(title = "Ошибка записи в файл", 
                     message = "Не удалось выполнить запись в файл.")            #Выдается соответствующее сообщение в диалоговом окне
            return False
        return True
