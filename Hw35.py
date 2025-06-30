import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption(("This is caption"))
#in this line i need to upload a image but dont have a image to upload so it is showing error
screen.fill((58,58,58))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip
