from scoreboard import Scoreboard

from button import Button

from game_stats import GameStats

from alien import Alien

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

import sys

import pygame

def run_game():
    # Inicializa o jogo e cria um objeto na tela
    pygame.init()
    obj_settings = Settings() 
    screen = pygame.display.set_mode((obj_settings.screen_width, obj_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    background = pygame.image.load('images/background2.jpg')
    
    
    # Cria o botão Play
    play_button = Button(obj_settings, screen, "Press P or Space")
    
    
    # Cria uma instãncia para armazenar dados estatísticos do jogo e cria painel de pontuação
    stats = GameStats(obj_settings)
    sb = Scoreboard(obj_settings, screen, stats)
    
    
    # Cria uma espaçonave (importando ela do arquivo ship)
    ship = Ship(obj_settings, screen)
    
    
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    
    
    # Cria um grupo de alienígenas
    aliens = Group()
    
    
    # Cria a frota de alienígena
    gf.create_fleet(obj_settings, screen, ship, aliens)
    
    
    # Define cor de fundo
    bg_color = (230, 230, 230)
    
    
    #Cria um alienígena
    alien = Alien(obj_settings, screen)
    
    
    # Inicia o laço principal do jogo
    while True:
        
        # Observa eventos de teclado e mouse
        gf.check_events(obj_settings, screen, stats, play_button, ship, aliens, bullets, sb)
        
        
        if stats.game_active:
            ship.update()
        
            bullets.update()
        
            gf.update_bullets(obj_settings, screen, stats, sb, ship, aliens, bullets)
        
            gf.update_aliens(obj_settings, screen, stats, sb, ship, aliens, bullets)
                
        gf.update_screen(obj_settings, screen, stats, sb, ship, aliens, bullets, play_button, background)
        
               
        
run_game()