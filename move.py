import pygame
import random
import os
from pygame import *
import threading

background="Images/field.png"
image_path2="Images/duck.png"
teacher="Images/duck_rev.png"
popal="Images/magic.png"

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image2 = pygame.image.load(os.path.join("Images", "field.png"))
image2 = transform.scale(image2,(800,500))
text = pygame.image.load(os.path.join(popal))
text = transform.scale(text,(800,500))

class Duck:
    def __init__(self, pos):

        self.image = pygame.image.load(os.path.join("Images", "duck.png"))
        self.image = transform.scale(self.image, (80, 70))

        self.image3 = pygame.image.load(os.path.join(teacher))
        self.image3 = transform.scale(self.image3, (100, 90))

        self.text=pygame.image.load(os.path.join(popal))
        self.x = pos[0]
        self.y = pos[1]
        self.direction="right"
        self.direction1="up"
    def update(self, speed = 4):

        if self.direction=="right":
            self.x+=speed
            if self.x>=745:
                self.direction="left"


        if self.direction =="left":
            self.x-= speed
            if self.x<=15:
                self.direction="right"

        if self.direction1=="up":
            self.y+=25
            if self.y>=475:
                self.direction1="down"

        if self.direction1=="down":
            self.y-=25
            if self.y<=75:
                self.direction1="up"



    def update2(self):
        if self.direction=="right":
            self.x+=4.5
            self.y-=2
            if self.x >= 745:
                self.direction="left"

        if self.direction =="left":
            self.x-=4.5
            self.y+=2
            if self.x<=15:
                self.direction="right"