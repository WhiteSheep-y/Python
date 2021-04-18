# p18_3.py
import pygame
import sys

pygame.init()

size = width, height = 600, 400
bg = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")
event_texts = []

# 要在Pygame中使用文本，必须创建Font对象
# 第一个参数指定字体，第二个参数指定字体的尺寸
font = pygame.font.Font(None, 20)

# 调用get_linesize()方法获得每行文本的高度
line_height = font.get_linesize()

position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # render()方法将文本渲染成Surface对象
        # 第一个参数是待渲染的文本
        # 第二个参数指定是否消除锯齿
        # 第三个参数指定文本的颜色
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += line_height

        if position > height:
            # 满屏时清屏
            position = 0
            screen.fill(bg)

    pygame.display.flip()
