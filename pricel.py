import pygame

pygame.init()

done = False

while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.KEYDOWN:
            if i.button == 3:
                if i.pos == duck.pos:
                    duck
                    pygame.display.update()
                elif i.pos == duck_rev.pos:
                duck_rev
            pygame.display.update()
    pygame.time.delay(20)