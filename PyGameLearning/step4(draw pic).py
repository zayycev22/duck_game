# -*- coding: utf-8 -*-
import pygame

pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image_path = 'Images/keleton.png'
try:
    image = pygame.image.load(image_path)  # загружаем картинку
    done = False
except pygame.error:
    print("Can't load image:", image_path)
    done = True

while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            done = True
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print('Key Down')
            # тут можно вызвать функцию, которая обработает это событие
        if e.type == pygame.KEYUP:  # Событие "Клавиша отпущена"
            print('Key Up')
            # тут можно вызвать функцию, которая обработает это событие
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            print('Mouse Down')
            # тут можно вызвать функцию, которая обработает это событие
    screen.blit(image, (100, 50))  # отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности