import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('game name')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
big_font = pygame.font.Font('Pixeltype.ttf', 100)
game_active = True


sky_surface = pygame.Surface((800,400))
sky_surface.fill('white')

ground_surface = pygame.Surface((800,5))
ground_surface.fill('black')

score_surface = test_font.render('blob runner', True, 'black')
score_rect = score_surface.get_rect(center = (400, 50))

blob_surface = pygame.image.load('bob.png').convert_alpha()
blob_rect = blob_surface.get_rect(midbottom = (700, 300 ))

dead_surface = big_font.render('YOU DIED SUCKER', True, 'Black')
dead_rect = dead_surface.get_rect(midbottom = (400, 200))

player_surface = pygame.image.load('blob.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
                

    if game_active:  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
    

        screen.blit(score_surface,score_rect)

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
    


    pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(60)  