import pygame
pygame.init()
window=pygame.display.set_mode((640,480))
caption=pygame.display.set_caption("Game Screen")
window.fill((0,0,0))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(window,(255,255,0) , pygame.Rect(60,60,30,30))
    font=pygame.font.Font(None , 30)
    text=font.render("This is Text" , True , (255,255,255))
    pygame.display.flip()