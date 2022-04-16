import pygame
import requests


WIDTH = HEIGHT = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
offset = 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
my_font = pygame.font.SysFont('Comic Sans MS', 35)


def insert(screen, position, grid, grid_original):
    global my_font
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i - 1][j - 1] != 0:
                    return
                if event.key == 48:  # checking for 0 to erase the value
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(screen, background_color, (
                        position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:  # checking for valid input 1-9
                    print(event.key)
                    pygame.draw.rect(screen, background_color, (
                        position[0] * 50 + offset, position[1] * 50 + offset, 50 - 2 * offset, 50 - 2 * offset))
                    value = my_font.render(str(event.key - 48), True, (0, 0, 0))
                    screen.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def game(grid, grid_original):
    for i in range(10):
        if not i % 3:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = my_font.render(str(grid[i][j]), True, original_grid_element_color)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(screen, (pos[0] // 50, pos[1] // 50), grid, grid_original)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def main():
    screen.fill(background_color)

    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")

    grid_original = response.json()['board']
    grid = [[grid_original[x][y] for y in range(len(grid_original[0]))] for \
            x in range(len(grid_original))]

    game(grid, grid_original)

if __name__ == '__main__':
    main()