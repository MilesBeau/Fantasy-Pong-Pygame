import pygame
import sys

pygame.init()

# Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Pygame Pong")

# Colours
white = (255, 255, 255)
black = (234, 212, 252)
grey = (191, 191, 191)

# ball 
ball = pygame.Rect(screen_width/2 - 11.25, screen_height/2 - 17.5,35,35)

# Paddle_A
paddle_A = pygame.Rect(screen_width - 130, screen_height/2 - 75,20,150)

# Paddle_B
paddle_B = pygame.Rect(screen_width - 1180, screen_height/2 - 75,20,150)

# Score Board



# Main Game Loop
KeepGameRunning = True
while KeepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            KeepGameRunning = False 
           
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, paddle_A)
    pygame.draw.rect(screen, white, paddle_B)
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
            
