import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, obj_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        super(Ship, self).__init__()
        
        self.screen = screen
        
        self.obj_settings = obj_settings
        
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        
        
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        
        self.moving_top = False
        self.moving_down = False
        
        
    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        
        # Atualiza o valor do centro da espaçonave, e não o do retãngulo
        if self.moving_right and self.rect.right < self.screen_rect.right:   # faz com que ele não passe as paredes do jogo 
            self.center += self.obj_settings.ship_speed_factor  # moves right
            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.obj_settings.ship_speed_factor 
            
        if self.moving_top and self.rect.top > 0:
            self.rect.bottom -= self.obj_settings.ship_speed_factor 
            
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.obj_settings.ship_speed_factor 
            
        
        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center
        #self.rect.bottom = self.bottom
        
        
    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)
        
        
        
    def center_ship(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.screen_rect.centerx
        
        
        
    def center_ship2(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    