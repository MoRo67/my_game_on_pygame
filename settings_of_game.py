class Settings():
    """"Класс для хранения настроек игры"""
    def __init__(self):
        """"Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        #Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3


        #Настройки корабля
        self.ship_speed = 1.5


