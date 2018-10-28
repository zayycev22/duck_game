import os
import pygame
import random
import time
from pygame import *
import threading
import duck

pygame.init()


class Pricel:

    def __init__(self, pos):

        self.image = pygame.image.load(os.path.join("Images", "pr.png"))
        self.image = transform.scale(self.image, (20, 20))


done = False
while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.KEYDOWN:
            if i.button == 3:
                if i.pos == duck.pos:
                    duck.delete()
                    pygame.display.update()
                elif i.pos == duck_rev.pos:
                    duck_rev.delete()
                    pygame.display.update()
    pygame.time.delay(20)
