import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)



# Font
FONT = pygame.font.SysFont("comicsans", 40)

# Sudoku Grid (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

selected = None


def draw_grid(win):
    # Draws the 9x9 grid lines
    for i in range(10):
        line_width = 5 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (i * 60, 0), (i * 60, 540), line_width)
        pygame.draw.line(win, BLACK, (0, i * 60), (540, i * 60), line_width)

def draw_numbers(win, grid):
    # Draws numbers on the grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                value = FONT.render(str(grid[i][j]), True, BLACK)
                win.blit(value, (j * 60 + 20, i * 60 + 10))

def draw_selected(win, pos):
    # Highlights the selected cell
    if pos:
        pygame.draw.rect(win, BLUE, (pos[1] * 60, pos[0] * 60, 60, 60), 3)

def check_valid_move(grid, num, pos):
    # Check if the number is valid at the position
    for i in range(9):
        if grid[pos[0]][i] == num or grid[i][pos[1]] == num:
            return False
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    return True

def click(pos):
    # Returns the cell clicked on
    if pos[0] < 540 and pos[1] < 540:
        return (pos[1] // 60, pos[0] // 60)
    return None

def main():
    run = True
    key = None
    global selected, grid

    while run:
        WIN.fill(WHITE)

        draw_grid(WIN)
        draw_numbers(WIN, grid)
        draw_selected(WIN, selected)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = click(pos)
                if clicked:
                    selected = clicked

            if event.type == pygame.KEYDOWN:
                if selected:
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9

                    if key is not None:
                        if check_valid_move(grid, key, selected):
                            grid[selected[0]][selected[1]] = key
                        key = None

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

