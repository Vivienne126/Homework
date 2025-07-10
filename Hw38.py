import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
screen.fill((255,255,255))
pygame.display.set_caption("The sprites change colour when you prees a key")

class sprite(pygame.sprite.Sprite):
    def __init__(self,colour,position):
        
        self.image=pygame.Surface((50,50))
        self.image.fill(colour)
        self.colour=colour
        self.position=position
    def change_colour(self,new_colour):
        self.colour=new_colour
        self.image.fill(new_colour)
sprite1=sprite((255,0,255) , (600,300))#colour and xany y cordinates
sprite2=sprite((255,255,0), (600,600))
all_sprites=pygame.sprite.Group(sprite1,sprite2)
done=False
while not done:
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                sprite1.change_colour((255,255,0))
            elif event.key==pygame.K_1:
                sprite2.change_colour((125,125,125))
    all_sprites.draw(screen)

pygame.display.flip()

