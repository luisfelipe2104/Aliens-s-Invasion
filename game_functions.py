import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep


def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação máxima"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def fire_bullet(obj_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < obj_settings.bullets_allowed:
        new_bullet = Bullet(obj_settings, screen, ship)
        bullets.add(new_bullet)
        
        # Tocando o som de tiro laser
        shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        pygame.mixer.Sound.set_volume(shoot_sound, 0.1)
        shoot_sound.play()


def check_keydown_events(event, obj_settings, screen, ship, bullets, aliens, stats, sb):
    """Responde a pressionamento de tecla"""
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:          # Move a espaçonave para a direita
        ship.moving_right = True
                
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.moving_left = True
                
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.moving_top = True
                
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.moving_down = True
        
        
    elif event.key == pygame.K_SPACE:
        fire_bullet(obj_settings, screen, ship, bullets)
        start_gameP(obj_settings, screen, stats, ship, aliens, bullets, sb)
        
        
    elif event.key == pygame.K_p:
        start_gameP(obj_settings, screen, stats, ship, aliens, bullets, sb)
        
        
    elif event.key == pygame.K_9:
        sys.exit()
        
        
def check_keyup_events(event, ship):
    """Responde a solturas de teclas"""
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:          
        ship.moving_right = False
            
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.moving_left = False
                
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.moving_top = False
                
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.moving_down = False
    
        

def check_events(obj_settings, screen, stats, play_button, ship, aliens, bullets, sb):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, obj_settings, screen, ship, bullets, aliens, stats, sb)
                
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(obj_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)


def start_gameP(obj_settings, screen, stats, ship, aliens, bullets, sb):
  
    if not stats.game_active:
        # Reinicia as configurações do jogo
        obj_settings.initialize_dynamic_settings()
        
        
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        
        
        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True
        
        
        # Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        
        
        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(obj_settings, screen, ship, aliens)
        ship.center_ship2()
        
        


def check_play_button(obj_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reinicia as configurações do jogo
        obj_settings.initialize_dynamic_settings()
        
        
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        
        
        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True
        
        
        # Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        
        
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        
        
        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(obj_settings, screen, ship, aliens)
        ship.center_ship2()
        
        

            
def update_screen(obj_settings, screen, stats, sb, ship, aliens, bullets, play_button, background):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(obj_settings.bg_color)
    screen.blit(background, (0, 0))
    
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
        
    ship.blitme()
    aliens.draw(screen)
    
    
    sb.show_score()
    
    
    # Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()
    
    
    # Deixa a tela mais recente visível
    pygame.display.flip()
    
    
    
def update_bullets(obj_settings, screen, stats, sb, ship, aliens, bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()
        
    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
    check_bullet_alien_collisions(obj_settings, screen, stats, sb, ship, aliens, bullets)
    
    
    
def check_bullet_alien_collisions(obj_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # identifica a colisão entre os membros de dois grupos
    
    
    if collisions:
        for aliens in collisions.values():
            stats.score += obj_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # Destrói os projéteis existentes, aumenta a velocidade do jogo e cria uma nova frota
        bullets.empty()
        obj_settings.increase_speed()
        
        
        # Aumenta o nível
        stats.level +=1
        sb.prep_level()
        
        
        create_fleet(obj_settings, screen, ship, aliens)
        ship.center_ship2()
    
    
    
def get_number_aliens_x(obj_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha"""
    
    available_space_x = obj_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    return number_aliens_x


def get_number_rows(obj_settings, ship_height, alien_height):
    """Determine o número de linhas com alienígenas que cabem na tela."""
    available_space_y = (obj_settings.screen_height - (3 * alien_height) - ship_height)
    
    number_rows = int(available_space_y / (2 * alien_height))
    
    return number_rows



def create_alien(obj_settings, screen, aliens, alien_number, row_number):
    # Cria um alienígena e o posiciona na linha
    alien = Alien(obj_settings, screen)
    alien_width = alien.rect.width
    
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    


    
def create_fleet(obj_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(obj_settings, screen)
    number_aliens_x = get_number_aliens_x(obj_settings, alien.rect.width)
    
    
    number_rows = get_number_rows(obj_settings, ship.rect.height, alien.rect.height)
    
    # Cria a frota de Alienígenas
    # Usamos o código de criar uma unica linha e o repetimos pelo número de vezes de number_rows
    for row_number in range(number_rows):
        
        for alien_number in range(number_aliens_x):
            create_alien(obj_settings, screen, aliens, alien_number, row_number)
            
            
            
def check_fleet_edges(obj_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(obj_settings, aliens)
            break
        
        
        
def change_fleet_direction(obj_settings, aliens):
    """Faz toda a frota desce e muda a sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += obj_settings.fleet_drop_speed
    obj_settings.fleet_direction *= -1
    
            
            
def ship_hit(obj_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
    
    if stats.ships_left > 0:
        # Decrementa ship_left
        stats.ships_left -= 1
        
        # Atualiza o painel de pontuações
        sb.prep_ships()
        
    
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
    
        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(obj_settings, screen, ship, aliens)
        ship.center_ship2()
        
    
    
        # Faz uma pausa
        sleep(0.5)
        
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    
    
def check_aliens_bottom(obj_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(obj_settings, screen, stats, sb, ship, aliens, bullets)
            break
        

            
            
def update_aliens(obj_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica se a frota está em uma das bordas
    e então atualiza as posições de todos alienígenas da frota."""
    
    check_fleet_edges(obj_settings, aliens)
    
    aliens.update()
    
    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_bottom(obj_settings, screen, stats, sb, ship, aliens, bullets)
    
    
    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
       # print("Oh shit!!!")
       ship_hit(obj_settings, screen, stats, sb, ship, aliens, bullets)
        