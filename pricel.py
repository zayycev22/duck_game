import os
import pygame
import random
import time
from pygame import *
import threading

import move

pygame.init()
pic1 = "Images/scope.png"


class Pricel:

    def __init__(self, pos):
        self.image = pygame.image.load(os.path.join(pic1))
        self.image = transform.scale(self.image, (40, 40))
        self.x = pos[0]
        self.y = pos[1]

    def update(self):
        pos = pygame.mouse.get_pos()
        # self.x += 10
        # self.y += 10
        self.x = pos[0] - 20
        self.y = pos[1] - 20

#    def shot(self, a):
#        pos = pygame.mouse.get_pos()
#        img = pygame.image.load(os.path.join("Images/shot.png"))
#        if a > 0:
#            a -= 1
#            screen.blit
#    def handle_mouse_move(self,pos):
# if self.bounds.collidepoint(pos)
