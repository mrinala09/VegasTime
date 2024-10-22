import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
BG_COLOR = pg.Color('white')

# Card rectangle
rect1 = pg.Rect(190, 60, 250, 375)

# Load images of suits into memory
memory_images = []
for filename in ['Spade.png', 'Diamond.png', 'Heart.png', 'Club.png']:
    new_image = pg.image.load(filename)
    memory_images.append(new_image)

# Function to resize images (if needed) to fit the card corners
def scale(image, width, height):
    return pg.transform.scale(image, (width, height))

corner_size = (40, 40)
memory_images = [scale(img, *corner_size) for img in memory_images]

# Run until the user asks to quit
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill background
    screen.fill(BG_COLOR)

    # Draw the card rectangle outline
    color = (0, 0, 0)  # Black
    pg.draw.rect(screen, color, rect1, 3)

    top_left = (rect1.left, rect1.top)
    top_right = (rect1.right - corner_size[0], rect1.top)
    bottom_left = (rect1.left, rect1.bottom - corner_size[1])
    bottom_right = (rect1.right - corner_size[0], rect1.bottom - corner_size[1])

    if suitChoice == 'club':
        
        screen.blit(memory_images[0], top_left)
        screen.blit(memory_images[0], top_right)
        screen.blit(memory_images[0], bottom_left)
        screen.blit(memory_images[0], bottom_right)
        
    elif suitChoice == 'diamond':

        screen.blit(memory_images[1], top_left)
        screen.blit(memory_images[1], top_right)
        screen.blit(memory_images[1], bottom_left)
        screen.blit(memory_images[1], bottom_right)

    elif suitChoice == 'spade':
       
        screen.blit(memory_images[2], top_left)
        screen.blit(memory_images[2], top_right)
        screen.blit(memory_images[2], bottom_left)
        screen.blit(memory_images[2], bottom_right)
    
    elif suitChoice == 'heart':
        screen.blit(memory_images[3], top_left)
        screen.blit(memory_images[3], top_right)
        screen.blit(memory_images[3], bottom_left)
        screen.blit(memory_images[3], bottom_right)
    

    pg.display.flip()

pg.quit()
