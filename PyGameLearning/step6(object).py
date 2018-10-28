# -*- coding: utf-8 -*-
import os
import pygame
from pygame import *


class Unit:
    def __init__(self, pos):
        self.image = pygame.image.load(os.path.join("Images", "skeleton.png"))
        self.x = pos[0]
        self.y = pos[1]

# TODO: Доработку Класса Unit выполняем вместе с преподавателем

def move(event, skeleton):
    print(event.key)
    if event.key == 198:
        skeleton.x -= 10
    elif event.key == 215:
        skeleton.x += 10


pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна
screen = pygame.display.get_surface()  # определяем поверхность для рисования

skeleton = Unit((50, 50))
done = False
while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            done = True

        if e.type == pygame.KEYDOWN:
            move(e, skeleton)

        screen.fill((0, 100, 100)) # Заливаем экран цветом
        screen.blit(skeleton.image,(skeleton.x, skeleton.y))  # отрисовываем содержимое поверхности
        pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности
