"""
Main pygame module
"""

from swap_puzzle import *

import pygame
import tkinter
import tkinter.filedialog
from pygame.locals import *

import copy

if __name__ == '__main__':
    tk = tkinter.Tk()  # otherwise with the file dialog the pygame window open in the background :/
    tk.title("Solving...")
    f = tkinter.filedialog.askopenfilename(title="Choose a grid file !")

    grid = Grid.grid_from_file(f)
    grid_data = copy.deepcopy(grid.state)
    solver = NaiveSolver()
    steps, solution = solver.solve(grid)

    pygame.init()
    tk.withdraw()

    cell_size = 50
    grid_width = len(grid_data[0])
    grid_height = len(grid_data)
    padding_x = 2
    padding_y = 1
    screen_width = grid_width * cell_size + padding_x * cell_size
    screen_height = grid_height * cell_size + padding_y * cell_size
    screen = pygame.display.set_mode((screen_width, screen_height))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 24)

    swap_list = []
    swap = False
    animating = False
    swap_cell_a = cell
    swap_cell_b = cell


    def draw_grid(animated_cells={}):
        for row_index, row in enumerate(grid_data):
            for col_index, item in enumerate(row):
                dx, dy = animated_cells.get((row_index, col_index), (0, 0))
                rect = pygame.Rect(((col_index + (padding_x / 2)) * cell_size) + dx,
                                   ((row_index + (padding_y / 2)) * cell_size) + dy, cell_size, cell_size)
                pygame.draw.rect(screen, BLACK, rect, 1)

                text_surf = font.render(str(item), True, BLACK)
                text_rect = text_surf.get_rect(center=rect.center)
                screen.blit(text_surf, text_rect)


    def animate_swap(cell_a, cell_b):
        global animating
        global swap

        if not swap:
            return
        swap = False  # Prevent re-triggering animation
        animating = True

        speed = 1
        ay, ax = cell_a
        by, bx = cell_b
        distance_x, distance_y = (bx - ax) * cell_size, (by - ay) * cell_size

        steps = max(abs(distance_x), abs(distance_y)) // speed
        if steps == 0:
            return

        dx = distance_x / steps
        dy = distance_y / steps

        for step in range(int(steps)):
            animated_cells = {
                cell_a: (dx * step, dy * step),
                cell_b: (-dx * step, -dy * step)
            }
            screen.fill(WHITE)
            draw_grid(animated_cells)
            pygame.display.flip()
            pygame.time.wait(10)

        grid_data[ay][ax], grid_data[by][bx] = grid_data[by][bx], grid_data[ay][ax]
        animating = False


    def trigger_swap(cell_a: cell, cell_b: cell):
        global swap
        global swap_cell_a
        global swap_cell_b

        swap_cell_a, swap_cell_b = cell_a, cell_b
        swap = True


    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()

        # Trigger the swap animation once at the start or under specific conditions
        if swap:
            animate_swap(swap_cell_a, swap_cell_b)
        elif len(solution) > 0 and not animating:
            trigger_swap(*solution.pop(0))

    pygame.quit()
    tk.destroy()
    sys.exit()
