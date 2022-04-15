from turtle import width


class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        
        # Configurações dos alienígenas
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10   # controla a velocidade com que a frota desce na tela sempre que um alienígena alcançar as bordas
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        #self.fleet_direction = 1
        
        
        # Configuração da espaçonave
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        
        # Configurações dos projéteis
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 201, 0, 37
        self.bullets_allowed = 3
        
        
        
        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        
        
        # A taxa com que os pontos para cada alienígena aumentam
        self.score_skale = 1.5
        
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam ao decorrer do jogo."""    
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.9
        
        # fleet_direction igual a 1 representa a direita; -1 a esquerda
        self.fleet_direction = 1
        
        
        # Pontuação
        self.alien_points = 50
        
        
    def increase_speed(self):
        """Aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_skale)
        # print(self.alien_points)