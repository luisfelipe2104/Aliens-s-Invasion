from pygame import init
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """Uma classe para mostrar informações sobre pontuação."""
    
    def __init__(self, obj_settings, screen, stats):
        """Inicializa os atributos de pontuação."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.obj_settings = obj_settings
        self.stats = stats
        
        
        # Configurações de fonte para as informações de pontuação
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        
        # Prepara a imagem da pontuação inicial
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
        
        
    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = f'Score: {rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, (0, 0, 0))
        
        
        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        
        
    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        # Desenha as espaçonaves
        self.ships.draw(self.screen)
        
        
        
    def prep_high_score(self):
        """Transforma a pontuação máxima em uma imagem renderizada"""
        high_score = int(round(self.stats.high_score, -1))    # -1 arredonda para mútiplos de 10
        high_score_str = f'High score: {high_score:,}'
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, (0, 0, 0))
        
        
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
        
        
    def prep_level(self):
        """Transforma o nível em uma imagem renderizada."""
        self.level_image = self.font.render(str(self.stats.level), True, 
                                            self.text_color, (0, 0, 0))
        
        
        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
        
    def prep_ships(self):
        """Mostra quantas espaçonaves ainda restam."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.obj_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)