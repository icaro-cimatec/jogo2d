import pygame

from bullet import Bullet
from ship import Ship
from settings import Settings

class BulletManager:
    """REsponsável apenas por criar, atualizar e desenhar os projetéis"""
    
    def __init__(self, screen: pygame.Surface, settings: Settings, ship: Ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def _fire_bullets(self) -> None:
        """Dispara um projétil se o limete de projetéis ainda não tiver sido alcançado"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self, aliens) -> None:
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos"""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collision(aliens)

    def _remove_offscreen_bullets(self) -> None:
        """Remove os projetéis que desaparecem da tela"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collision(self, aliens) -> None:
        """Verifica colisões entre projéteis e alienígenas"""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)
