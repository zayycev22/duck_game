# -*- coding: utf-8 -*-
import os
import pygame
import random
import time
from pygame import *
import threading

pygame.init()  # инициализация
display = pygame.display.set_mode((800, 500))  # создание окна
background="Images/field.png"
image_path2="Images/duck.png"
teacher="Images/duck_re.png"
popal="Images/garry.png"

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
    def update(self, speed = 4):

        if self.direction=="right":
            self.x+=speed
            if self.x>=745:
                self.direction="left"
                self.y+=25

        if self.direction =="left":
            self.x-= speed
            if self.x<=15:
                self.direction="right"
                self.y += 25

    def update2(self):
        if self.direction=="right":
            duck_rev.x+=4.5
            duck_rev.y-=2
            if self.x >= 745:
                self.direction="left"

        if self.direction =="left":
            self.x-=4.5
            self.y+=2
            if self.x<=15:
                self.direction="right"







ducks=[]
for i in range(0, 5, 1):
    ducks.append(Duck((0, random.randint(10, 450))))
duck=Duck((0,100))
duck_rev=Duck((0,450))
z = 210
time = 90
FPS = 30
clock = pygame.time.Clock()
check=False
done=False
while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
    z -= 1

    if z <= 0:
        check=True
        while time >= 0:
            time -= 1
            screen.blit(text,(0,0))
            pygame.display.flip()
            clock.tick(FPS)



    duck.update()
    duck_rev.update2()
    if check==True:
        for i in range(0, 5):
            ducks[i].update(random.randint(2, 15))

    screen.fill((0, 100, 100))
    screen.blit(image2,(0, 0))
    if check==True:
        for i in range(0, 5):
            screen.blit(ducks[i].image, (ducks[i].x, ducks[i].y))
    screen.blit(duck.image, (duck.x, duck.y))
    screen.blit(duck_rev.image3,(duck_rev.x,duck_rev.y))# отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()
    clock.tick(FPS)
