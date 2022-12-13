import pygame

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает начальную позицию"""
        self.screen = ai_game.screen
        self.settings_of_game = ai_game.settings_of_game
        self.screen_rect = ai_game.screen.get_rect()

        #Загружам изображение корабля
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        #Каждый новый корабль появлеяется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранения вещественной координаты центра корабля
        self.x = float(self.rect.x)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию коробля с учетом флага"""
        #Обновляется атрибут x, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings_of_game.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings_of_game.ship_speed

        #Обновление атрибута rect на основе self.x
        self.rect.x = self.x



    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

