# -*- coding: utf-8 -*-
import os
import pygame
import random
import time
from pygame import *
import threading
import move
import pricel

pygame.init()  # инициализация
display = pygame.display.set_mode((800, 500))  # создание окна
background = "Images/field.png"
image_path2 = "Images/duck.png"
teacher = "Images/duck_rev.png"
popal = "Images/magic.png"
pic1 = "Images/scope.png"
vic = "Images/vic.png"
vs = "Images/vs.png"

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image2 = pygame.image.load(os.path.join("Images", "field.png"))
image2 = transform.scale(image2, (800, 500))
text = pygame.image.load(os.path.join(popal))
text = transform.scale(text, (800, 500))
vsriv = pygame.image.load(os.path.join(vs))
vsriv = transform.scale(vsriv, (50, 50))
vsriv1 = transform.scale(vsriv, (100, 100))
scope_img = pygame.image.load(os.path.join(pic1))
victory = pygame.image.load(os.path.join(vic))
victory = transform.scale(victory, (480, 270))
defeat = pygame.image.load(os.path.join("Images/def.png"))
defeat = transform.scale(defeat, (480, 270))
pric = pricel.Pricel(pygame.mouse.get_pos())
ducks = []

# ducks2 = []
for i in range(0, 5, 1):
    ducks.append(move.Duck((random.randint(0, 700), random.randint(0, 450))))

# for i in range(0, 5, 1):
#   ducks2.append(Duck((0, random.randint(750, 450))))

duck = move.Duck((0, 100))
duck_rev = move.Duck((750, 100))
z = 0
time = 10
FPS = 30
clock = pygame.time.Clock()
speed = 0.2
speed1 = 2
pygame.mixer.init()
exp = pygame.mixer.Sound("music/vsriv.wav")
sound1 = pygame.mixer.Sound("music/vic.ogx")
sound2 = pygame.mixer.Sound("music/Porazhenie.mp3")
shot = pygame.mixer.Sound("music/shot.wav")
sound = pygame.mixer.Sound('music/mus.ogg')
reload = pygame.mixer.Sound("music/reload.ogg")
sound.play(-1)
check = False
done = False
f = 1
# a = 1
# ammo = 5
points = 0
e3 = 21
e1 = 21
e2 = [21, 21, 21, 21, 21]
timer = 1000
pos = pygame.mouse.get_pos()
while not done:
    timer -= 1
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
        if f <= 0 and e.type == pygame.MOUSEBUTTONDOWN:
            shot.play(0)
            #            ammo -= 1
            f = 40
            # a = 40
            # pos = pygame.mouse.get_pos()
            duck.check(pygame.mouse.get_pos(), points)
            duck_rev.check1(pygame.mouse.get_pos(), points)
            for i in range(0, 5):
                ducks[i].check(pygame.mouse.get_pos(), points)

    #    if ammo == 0:
    #        ammo = 5
    #        reload.play(0)
    z -= 1
    f -= 1
    #    pric.shot(a, screen, pos)
    if z <= 0:
        check = True
        while time >= 0:
            time -= 1
            screen.blit(text, (0, 0))
            pygame.display.flip()
            clock.tick(FPS)
    pygame.mouse.set_visible(False)
    speed += 0.01
    if duck.is_alive:
        duck.update(speed)
    if duck_rev.is_alive:
        duck_rev.update2()
    for i in range(0, 5):
        if ducks[i].is_alive:
            ducks[i].update(speed)
    pric.update()

    screen.fill((0, 100, 100))
    screen.blit(image2, (0, 0))

    # screen.blit(scope_img, (0,0))
    if check:
        for i in range(0, 5):
            if ducks[i].is_alive:
                screen.blit(ducks[i].image, (ducks[i].x, ducks[i].y))
            elif not ducks[i].is_alive and e2[i] > 0:
                e2[i] -= 1
                screen.blit(vsriv, (ducks[i].x, ducks[i].y))
                if e2[i] >= 20:
                    exp.play(0)

        if duck.is_alive:
            screen.blit(duck.image, (duck.x, duck.y))
        else:
            e3 -= 1
            if e3 > 0:
                screen.blit(vsriv, (duck.x, duck.y))
                if e3 >= 20:
                    exp.play(0)

        if duck_rev.is_alive:
            screen.blit(duck_rev.image3, (duck_rev.x, duck_rev.y))
        else:
            e1 -= 1
            if e1 > 0:
                screen.blit(vsriv1, (duck_rev.x, duck_rev.y))
                if e1 >= 20:
                    exp.play(0)

        screen.blit(pric.image, (pric.x, pric.y))
    pygame.display.flip()
    clock.tick(FPS)
    if not duck.is_alive and not duck_rev.is_alive:
        if not ducks[0].is_alive and not ducks[1].is_alive:
            if not ducks[2].is_alive and not ducks[3].is_alive and not ducks[4].is_alive:
                time = 100
                sound.stop()
                while time >= 0:
                    time -= 1
                    sound1.play(1)
                    screen.blit(victory, (100, 100))
                    pygame.display.flip()
                    clock.tick(FPS)
                done = True
    if timer <= 0:
        time = 100
        sound.stop()
        while time >= 0:
            time -= 1
            sound2.play(1)
            screen.blit(defeat, (100, 100))
            pygame.display.flip()
            clock.tick(FPS)
        done = True
    a = divmod(timer, 60)
    print(a[0], ':', a[1])
