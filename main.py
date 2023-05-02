import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f'{current_time}',False,'black')
    score_rect = score_surface.get_rect(center = (400,50))
   
    if current_time >= 20000:
        screen.blit(ultrabeast_mode, ultrabeast_rect)
        blob_rect.x -=17
    
    elif current_time >= 10000:
        screen.blit(beast_mode, beast_rect)
        blob_rect.x -=10
    screen.blit(score_surface, score_rect)

    

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('game name')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
big_font = pygame.font.Font('Pixeltype.ttf', 100)
game_active = True
start_time = 0

sky_surface = pygame.Surface((800,400))
sky_surface.fill('white')

ground_surface = pygame.Surface((800,5))
ground_surface.fill('black')

ultrabeast_mode = test_font.render('ULTRA BEAST MODE', True, 'Purple')
ultrabeast_rect = ultrabeast_mode.get_rect(midbottom = (400, 100))

blob_surface = pygame.image.load('bob.png').convert_alpha()
blob_rect = blob_surface.get_rect(midbottom = (700, 300 ))

dead_surface = big_font.render('YOU DIED SUCKER', True, 'Black')
dead_rect = dead_surface.get_rect(midbottom = (400, 200))

beast_mode = test_font.render('BEAST MODE', True, 'Red')
beast_rect = beast_mode.get_rect(midbottom = (400, 100))

instruction_surface = test_font.render('(press space to try again)',True, 'black')
instruction_rect = instruction_surface.get_rect(midbottom = (400,300))

player_surface = pygame.image.load('blob.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                game_active = True
                blob_rect.left = 800
                start_time = pygame.time.get_ticks()
            
    if game_active:  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
    
        display_score()
        #screen.blit(score_surface,score_rect)

        screen.blit(blob_surface, blob_rect)
        blob_rect.x -=4
        if blob_rect.right <= 0: blob_rect.left = 800

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        

        screen.blit(player_surface, player_rect)

        if blob_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('White')
        screen.blit(dead_surface, dead_rect)
        screen.blit(instruction_surface, instruction_rect)
        
    


    pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(60)  