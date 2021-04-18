# p18_6.py
import pygame
import sys
# 将 pygame 的所有常量名导入
from pygame.locals import *

# 初始化Pygame
pygame.init()

fullscreen = Fals

size = width, height = 600, 400
bg = (255, 255, 255)
speed = [0, 0]

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption("初次见面，请大家多多关照！")

turtle = pygame.image.load(r"image/turtle.png")
position = turtle.get_rect()

# 指定龟头的左右朝向
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
                turtle = l_head
            if event.key == K_RIGHT:
                speed = [1, 0]
                turtle = r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
            # 全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
        # 用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()

    clock.tick(30)
