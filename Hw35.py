import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("This is caption")
screen.fill((58,58,58))
ufo_imag=pygame.image.load("ufo.png")
screen.blit(ufo_imag,(200,200))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()