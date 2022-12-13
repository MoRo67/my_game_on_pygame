import pygame
import sys
from settings_of_game import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """"Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """"Инициализация игры и создание игровых ресурсов"""
        pygame.init()
        self.settings_of_game = Settings()

        self.screen = pygame.display.set_mode((self.settings_of_game.screen_width, self.settings_of_game.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.fleet()






    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.update()
            self._update_bullet()
            self._update_screen()


    def _check_events(self):
            """Обрабатывает нажатие клавиш и мыши"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)

    def _check_keydown(self, event):
            """Реагирует на нажатие клавиш"""
            if event.key == pygame.K_d:
                self.ship.moving_right = True
            elif event.key == pygame.K_a:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup(self, event):
            """Реагирует на отпускание клавиш"""
            if event.key == pygame.K_d:
                self.ship.moving_right = False
            elif event.key == pygame.K_a:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullet"""
        if len(self.bullet) < self.settings_of_game.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullet(self):
        """Уничтожает старые снаряды"""
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

    def fleet(self):
        """Создание флота врагов"""
        #Создание пришельцев
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings_of_game.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Создание первого ряда пришелцев
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


    def _update_screen(self):
            """Обновляет изображение на экране и отобрадает новый экран"""
            self.screen.fill(self.settings_of_game.bg_color)
            self.ship.blitme()
            for bullet in self.bullet.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)



            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземплятора и запуск игры
    ai = AlienInvasion()
    ai.run_game()



