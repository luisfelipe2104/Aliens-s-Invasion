class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    
    
    def __init__(self, obj_settings):
        """Inicializa os dados estatísticos."""
        self.obj_settings = obj_settings
        self.reset_stats()
        
        # Inicia a Invasão Alienígena em um estado inativo
        self.game_active = False
        
        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0
        
        
        
    def reset_stats(self):
        """Inicializanos os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.obj_settings.ship_limit
        self.score = 0
        self.level = 1
                