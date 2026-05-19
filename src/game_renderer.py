import pygame
from ship import Ship

class GameRenderer:
    """Responsável apenas por desenhar os elementos do jogo na tela"""

    def __init__(self, screen: pygame.Surface, bg_color: tuple, ship: Ship, bullets: pygame.sprite.Group, aliens: pygame.sprite.Group) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha os projetéis na tela"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
