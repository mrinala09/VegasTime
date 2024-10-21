import pygame as pg 

pg.init()
screen = pg.display.set_mode((640,480))
BG_COLOR = pg.Color('white')
rect1 = pg.Rect(190,60,250,375)



memory_images = []
for filename in ['Spade.png', 'Diamond.png', 'Heart.png', 'Club.png']:
    new_image = pg.image.load( filename )
    memory_images.append( new_image )




# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BG_COLOR)
    color = (0,0,0)

    pg.draw.rect(screen, color,  rect1, 3)


# example edit to accomodate ur code, this was a test
# image_count = len( memory_images )  # should be 16 for a 4x4 grid
# random_locations = random.sample( range( image_count ), image_count )


# for i in range( 16 ):
#     x, y = grid_locations[ i ]
#     image = memory_images[ random_locations[ i ] ]
#     screen.blit( image, ( x, y ) )
    

    if suitChoice == 'club': 
        




        
    elif suitChoice == 'diamond':

    elif suitChoice == 'spade':
    
    elif suitChoice == 'heart':
    
    else:
     break 





    # then if user number = x, then print number of dots in the center of the card



    
    pg.display.flip()



# pg.quit()

