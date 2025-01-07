import pygame
import sys

pygame.init()

# window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Pygame Pong")

# colours
white = (255, 255, 255)
black = (234, 212, 252)
grey = (191, 191, 191)

# ball 
ball = pygame.Rect(screen_width/2 - 11.25, screen_height/2 - 17.5,35,35)

ball_speed_x = 1
ball_speed_y = 1

# paddle_A
paddle_A = pygame.Rect(screen_width - 130, screen_height/2 - 75,20,150)

# paddle_B
paddle_B = pygame.Rect(screen_width - 1180, screen_height/2 - 75,20,150)

# Score Board



# Main-Game-Loop
KeepGameRunning = True
while KeepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            KeepGameRunning = False 
    
    # On-Screen-Objects
    screen.fill(grey)       
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, paddle_A)
    pygame.draw.rect(screen, white, paddle_B)
    
    # Movements
    ball.x += ball_speed_x 
    ball.y += ball_speed_y
    
    # Border-Checking
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
            
