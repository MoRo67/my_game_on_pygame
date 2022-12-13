import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        #Загрузка изображения пришельца и присвоение rect
        self.image = pygame.image.load('images/evil.png')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 60

        self.x = float(self.rect.x)





