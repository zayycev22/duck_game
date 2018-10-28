# -*- coding: utf-8 -*-
import pygame

pygame.init()  # инициализация
display = pygame.display.set_mode((400, 400))  # создание окна

screen = pygame.display.get_surface()  # определяем поверхность для рисования
image_path = "Images/skeleton.png"
# TODO: Задание-2 Загрузить и отобразить на сцене ещё несколько произвольных картинок
try:
    image = pygame.image.load(image_path)  # загружаем картинку
    done = False
except pygame.error:
    print("Can't load image:", image_path)
    done = True

x = 100
y = 50

# TODO: Задание-5* Загрузите картинку зайца "hare.png". Реализуйте его непрерывное движение вверх-вних-вверх-... по окну

while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            done = True
            # TODO: Задание-1 Дописать закрытие окна по нажатию клавиши Esc |"K_ESCAPE" - константа клавиши Esc
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            print("Key Down")
            print("e.key =", e.key)
            x += 10
            # TODO: Задание-3 Реализовать двидение объекта во все 4 стороны
            # TODO: Задание-3 Вынесите реализацию в отдельную функцию move(e, x, y)
        if e.type == pygame.KEYUP:  # Событие "Клавиша отпущена"
            print("Key Up")
            # TODO: Задание-4* Реализуйте непрерывное движение объекта пока нажата клавиша и остановку при отпускании
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            print("Mouse Down")
    # @uncomment-1 screen.fill((0,100,100))
    screen.blit(image, (x, y))  # отрисовываем содержимое поверхности image на поверхность screen
    pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности