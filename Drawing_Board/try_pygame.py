"""
制作一个简单的飞机大战游戏，来测试pygame
"""

import pygame as pg
from pygame.locals import *


def main():
    # 初始化
    screen = pg.display.set_mode((480, 800))
    pg.display.set_caption("Try_Pygame")
    clock = pg.time.Clock()

    bg = pg.image.load('images/background.png').convert()
    plane = pg.image.load('images/plane.png').convert_alpha()  # png图片包含透明通道，需要alpha

    while True:
        clock.tick(30)
        screen.blit(bg, (0, 0))  # 左上角坐标

        (x, y) = pg.mouse.get_pos()
        x -= plane.get_width() / 2
        y -= plane.get_height() / 2
        screen.blit(plane, (x, y))


        for event in pg.event.get():  # 得到消息队列
            # print(event)
            if event.type==QUIT:
                return

        pg.display.update()


if __name__ == "__main__":
    main()
