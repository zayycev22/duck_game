import os
import pygame
import random
import time
from pygame import *
import threading


import move
pygame.init()
pic1="Images/scope.png"

class Pricel:

    def __init__(self, pos):

        self.image = pygame.image.load(os.path.join(pic1))
        self.image = transform.scale(self.image, (20, 20))
        self.x=pos[0]
        self.y=pos[1]

    def update(self):
        #pos = pygame.mouse.get_pos()
        self.x += 1
        self.y += 1
        #self.x = pos[0]
        #self.y = pos[1]
#    def handle_mouse_move(self,pos):
        #if self.bounds.collidepoint(pos)


