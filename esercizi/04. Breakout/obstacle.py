import pygame

class Obstacle:
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int], size: tuple[int, int]):
        x, y = pos
        w, h =  size
        self.rect  =pygame.Rect(x, y, w, h)
        self.color = color
        self.active = True
    
    def hit(self):
        self.active = False

    def draw(self, surface: pygame.Surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=4)
        
        