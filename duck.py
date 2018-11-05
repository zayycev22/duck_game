# -*- coding: utf-8 -*-
import os
import pygame
import random
import time
from pygame import *
import threading
import move
pygame.init()  # инициализация
display = pygame.display.set_mode((800, 500))  # создание окна
background="Images/field.png"
image_path2="Images/duck.png"
teacher="Images/duck_rev.png"
popal="Images/magic.png"

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image2 = pygame.image.load(os.path.join("Images", "field.png"))
image2 = transform.scale(image2,(800,500))
text = pygame.image.load(os.path.join(popal))
text = transform.scale(text,(800,500))









ducks=[]
ducks2=[]
for i in range(0, 5, 1):
    ducks.append(move.Duck((0, random.randint(10, 450))))
#for i in range(0, 5, 1):
 #   ducks2.append(Duck((0, random.randint(750, 450))))
duck=move.Duck((0,100))
duck_rev=move.Duck((0,450))
z = 210
time = 90
FPS = 30
clock = pygame.time.Clock()
pygame.mixer.init()
sound=pygame.mixer.Sound('music/mus.ogg')
sound.play(-1)
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
           # screen.blit(ducks2[i].image, (ducks[i].x, ducks[i].y))
    screen.blit(duck.image, (duck.x, duck.y))
    screen.blit(duck_rev.image3,(duck_rev.x,duck_rev.y))# отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()
    clock.tick(FPS)
