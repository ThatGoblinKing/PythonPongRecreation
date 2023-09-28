#Pygames
import pygame
import threading
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")

#Paddle Positions
p1x = 20
p2x = 660
p1y = 200
p2y = 200
playerSpeed = 5

#Ball Positions
bx = 350
by = 250
#Ball Velocity
bVx = 5
bVy = 5
ballDirX = 1
ballDirY = 1
#Ball misc
bColor = (255, 255, 255)
ballIncrease = 0.25


#Scores
p1Score = 0
p2Score = 0

#Misc
doExit = False
clock = pygame.time.Clock()

while not doExit:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True #exits game loop
            
    #Game Logic
    #Controls
    keys = pygame.key.get_pressed()

    #P1
    if keys[pygame.K_w] and p1y > 0:
        p1y-=playerSpeed
    if keys[pygame.K_s] and p1y + 100 < 500:
        p1y+=playerSpeed
    
    #P2
    if keys[pygame.K_UP] and p2y > 0:
        p2y-=playerSpeed
    if keys[pygame.K_DOWN] and p2y + 100 < 500:
        p2y+=playerSpeed
    else:
        bx += bVx * ballDirX
        by += bVy * ballDirY

    #Ball bounce
    if bx < 0:
        ballDirX *= -1
        p2Score += 1
        bColor = (255, 255, 255)

    if bx + 20 > 700:
        ballDirX *= -1
        p1Score += 1
        bColor = (255, 255, 255)

    if by < 0 or by + 20 > 500:
        ballDirY *= -1
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bx = p1x + 20
        ballDirX *= -1
        bVx += ballIncrease
        bColor = (55, 250, 188)
    if bx > p2x - 20 and by + 20 > p2y and by < p2y + 100:
        bx = p2x - 20
        ballDirX *= -1
        bVx += ballIncrease
        bColor = (250, 184, 97)
        
    playerSpeed = bVx



    #Render Section
    screen.fill((0,0,0))
    img = pygame.image.load('BG.png')
    rect = img.get_rect()
    rect.center = 349, 249
    screen.blit(img, rect)

    #Paddles
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100))
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100))
    
    #Ball
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20))
    pygame.draw.rect(screen, (bColor), (bx, by, 20, 20), 3)
    
    #Score

    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))
    img = pygame.image.load('BG.png')
    pygame.display.flip()

pygame.quit() #Quits game