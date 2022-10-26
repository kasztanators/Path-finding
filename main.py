
import pygame
import math
from settings import *
from spot import *


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2


def make_grid(rows,width):
    grid = []
    gap = width //rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j , gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(surface, rows, width):
    gap = width //rows
    for i in range(rows):
        pygame.draw.line(surface, GREY,(0,i*gap),(width, i * gap))
        for j in range(rows):
            pygame.draw.line(surface, GREY, (j*gap, 0), (j*gap, width))


def draw(surface, grid, rows, width):
    surface.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(surface)

    draw_grid(surface, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row =  y //gap
    col = x // gap
    return row, col


def main(surface, width):
    ROWS = 50 
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = True
    while run:

        draw(surface, grid, ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

                elif not end:
                    end = spot
                    end.make_end()

                elif spot != end  and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()


class Window:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WIDTH,WIDTH))
        pygame.display.set_caption('path finding alogrithm')


if __name__ == '__main__':
    win = Window()
    main(win.display_surface, WIDTH)