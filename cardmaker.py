
import pygame
pygame.init()



memory_images = []
for filename in ['Spade.png', 'Diamond.png', 'Heart.png', 'Club.png']:
    new_image = pygame.image.load( filename )
    memory_images.append( new_image )




# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    surface = pygame.display.set_mode([500, 500])

    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # Draw surf at the new coordinates
    pygame.display.flip()

    color = (255,0,0)
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))


    # spade is 1st, diamond is 2nd, heart is 3rd club is 4th 
    # if suitChoice == 'club': 




        
    # elif suitChoice == 'diamond':

    # elif suitChoice == 'spade':
    
    # elif suitChoice == 'heart':
    
    # else:
    #     break 





    # then if user number = x, then print number of dots in the center of the card



    
    pygame.display.flip()



# pygame.quit()

