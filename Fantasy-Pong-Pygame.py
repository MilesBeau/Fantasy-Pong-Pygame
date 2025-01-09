import pygame
import sys

pygame.init()

# window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Pygame Pong")

# clock
clock = pygame.time.Clock()

# colours
white = (255, 255, 255)
black = (0, 0, 0)
grey = (191, 191, 191)

# ball 
ball = pygame.Rect(screen_width/2 - 11.25, screen_height/2 - 17.5,35,35)
ball_speed_x = 7
ball_speed_y = 7

# paddle_A
paddle_A = pygame.Rect(screen_width - 130, screen_height/2 - 75,20,150)
paddle_A_speed = 0

# paddle_B
paddle_B = pygame.Rect(screen_width - 1180, screen_height/2 - 75,20,150)
paddle_B_speed = 0

# main-Game-Loop
KeepGameRunning = True
while KeepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            KeepGameRunning = False
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_A_speed=-5.5
            elif event.key == pygame.K_DOWN:
                paddle_A_speed =5.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_B_speed=-5.5
            elif event.key == pygame.K_s:
                paddle_B_speed =5.5
            
    
    # On-Screen-Objects
    screen.fill(black)       
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, paddle_A)
    pygame.draw.rect(screen, white, paddle_B)
    
    # Movements
    ball.x += ball_speed_x 
    ball.y += ball_speed_y
    paddle_A.y += paddle_A_speed
    paddle_B.y += paddle_B_speed
    
    # Border-Checking
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if paddle_A.top <= 0 or paddle_A.bottom >= screen_height:
        paddle_A_speed = 0
    if paddle_B.top <= 0 or paddle_B.bottom >= screen_height:
        paddle_B_speed = 0
   
    pygame.display.update()
    clock.tick(60)

            
