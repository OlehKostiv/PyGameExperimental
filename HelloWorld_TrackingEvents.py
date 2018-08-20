# pylint: disable=E1101
import pygame
pygame.init()

gameDisplayXY = (500, 500)
pygame.display.set_mode( gameDisplayXY )
pygame.display.set_caption( 'Hello, world!' )
gameClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print( event )

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
    gameClock.tick( 30 )