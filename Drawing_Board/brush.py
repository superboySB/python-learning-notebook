import pygame
import math


# 画笔类
class Brush:
    def __init__(self, screen):
        """
        初始化函数
        """
        self.screen = screen  # pygame.surface
        self.color = (0, 0, 0)

        self.size = 1  # 画笔大小
        self.drawing = False
        self.last_pos = None  # 存储上一点的位置

        # style :True -> png brush  // False->Pencil
        self.style = True

        self.brush = pygame.image.load("images/brush.png").convert_alpha()
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))  # 子表面

    def start_draw(self, pos):
        """
        开始绘制，并记录当前坐标
        """
        self.drawing = True
        self.last_pos = pos  # # 存储上一点的位置

    def end_draw(self):
        """
        结束绘制
        """
        self.drawing = False

    def set_brush_style(self, style):
        """
        设置笔刷的样式
        """
        print("* set brush style to", style)
        self.style = style

    def get_brush_style(self):
        """
        获取笔刷的类型
        """
        return self.style

    def get_current_brush(self):
        """
        获取当前笔刷
        """
        return self.brush_now

    def set_size(self, size):
        """
        设置笔刷大小
        """
        if size < 1:
            size = 1
        elif size > 32:
            size = 32
        print("* set brush size to", size)
        self.size = size
        self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))  # 子表面

    def get_size(self):
        """
        获取笔刷大小
        """
        return self.size

    def set_color(self, color):
        """
        设定笔刷颜色
        """
        self.color = color
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                self.brush.set_at((i, j), color + (self.brush.get_at((i, j)).a,))  # 改变png导入的笔刷颜色，但保留alpha

    def get_color(self):
        """
        获取笔刷颜色
        """
        return self.color

    def _get_points(self, pos):   #TODO:属于线性插值
        """
        为了绘制的线条更加平滑，我们需要获取前一个点与当前点之间的所有需要绘制的点
        """
        points = [(self.last_pos[0], self.last_pos[1])]  # 上一个点，考虑鼠标动的飞快时的情况
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)

        step_x = len_x / length
        step_y = len_y / length

        for i in range(int(length)):
            points.append((points[-1][0] + step_x, points[-1][1] + step_y))  # 添加沿途的点

        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)

        return list(set((points)))  # 相当于{xxx,xxx,xxx}，无序的不重复元素序列，给过程点”去重“专用

    def draw(self, pos):
        """
        绘制
        """
        if self.drawing:
            for p in self._get_points(pos):
                if self.style:
                    self.screen.blit(self.brush_now, p)
                else:
                    pygame.draw.circle(self.screen, self.color, p, self.size)  # 过程中的点全部连接

            self.last_pos = pos
