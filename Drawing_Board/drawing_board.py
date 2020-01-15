"""
基于Pygame的画板
"""

# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from brush import Brush
from menu import Menu



# 画板类
class Painter:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Painter")
        self.clock = pygame.time.Clock()

        self.brush = Brush(self.screen)
        self.menu = Menu(self.screen)

        self.menu.set_brush(self.brush)  # 设置笔刷

    def run(self):
        self.screen.fill((255, 255, 255))
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen.fill((255, 255, 255))  # 用填充清屏
                elif event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] <= 74 and self.menu.click_button(event.pos):
                        # 若没有点击菜单，则画画
                        pass
                    else:
                        self.brush.start_draw(event.pos)  # drawing->true
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.brush.end_draw()  # drawing->false

            self.menu.draw()
            pygame.display.update()


# 主函数
def main():
    app = Painter()
    app.run()


if __name__ == '__main__':
    main()
