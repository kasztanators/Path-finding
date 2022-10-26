from doctest import FAIL_FAST
import pygame

from settings import BLACK, GREEN, ORANGE, PURPLE, RED, TURQUOISE, WHITE


class Spot:
    def __init__(self, row, col, width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row , self.col

    def is_closed(self):
        return self.is_closed ==RED
    
    def is_open(self):
        return self.color ==GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        return self.color == WHITE
    
    def start(self):
        self.color = ORANGE
    
    def make_closed(self):
        return self.color == GREEN
    
    def make_barrier(self):
        self.color == BLACK

    def make_end(self):
        self.color == TURQUOISE

    def make_path(self):
        self.col == PURPLE

    def draw(self, win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def __lt__(self,other):
        return False

