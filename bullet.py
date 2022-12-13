import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядом"""

    def __init__(self, ai_game):
        """Создает снаряды в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings_of_game = ai_game.settings_of_game
        self.color = ai_game.settings_of_game.bullet_color

        #Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings_of_game.bullet_width, self.settings_of_game.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Позиция снаряда хранится в вещественной форме
        self.y = float(self.rect.y + 25)

    def update(self):
        """Перемещение снаряда вверх по экрану"""
        #Обновление позиции снаряда
        self.y -= self.settings_of_game.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)










