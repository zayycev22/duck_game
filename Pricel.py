# -*- coding: utf-8 -*-
import pygame

pygame.init()  # инициализация

done = False
while not done:  # главный цикл программы
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
        elif i.button == 3:
            if i.pos == duck.pos:
                pygame.display.update()
            elif i.pos == duck_rev.pos:
                pygame.display.update()
                    
    pygame.time.delay(20)