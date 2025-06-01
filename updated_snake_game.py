import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Fonts
font = pygame.font.SysFont('arial', 24, bold=True)
large_font = pygame.font.SysFont('arial', 48, bold=True)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def draw_snake(snake_body):
    for i, block in enumerate(snake_body):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(position):
    pygame.draw.rect(screen, RED, pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))

def show_text(text, size, color, y_offset=0):
    fnt = large_font if size == "large" else font
    text_surface = fnt.render(text, True, color)
    rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, rect)

def get_random_position():
    return [random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE)]

def select_difficulty():
    selecting = True
    difficulty = {"label": "Normal", "fps": 10}
    while selecting:
        screen.fill(BLACK)
        show_text("Select Difficulty", "large", WHITE, -80)
        show_text("1 - Easy", "small", GRAY, -20)
        show_text("2 - Normal", "small", GRAY, 20)
        show_text("3 - Hard", "small", GRAY, 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = {"label": "Easy", "fps": 7}
                    selecting = False
                elif event.key == pygame.K_2:
                    difficulty = {"label": "Normal", "fps": 10}
                    selecting = False
                elif event.key == pygame.K_3:
                    difficulty = {"label": "Hard", "fps": 15}
                    selecting = False
    return difficulty

def main():
    difficulty = select_difficulty()
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = get_random_position()
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_e and game_over:
                    main()

        if not game_over:
            direction = change_to
            head_x, head_y = snake[0]

            if direction == 'UP':
                head_y -= BLOCK_SIZE
            elif direction == 'DOWN':
                head_y += BLOCK_SIZE
            elif direction == 'LEFT':
                head_x -= BLOCK_SIZE
            elif direction == 'RIGHT':
                head_x += BLOCK_SIZE

            new_head = [head_x, head_y]

            if (
                head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT or
                new_head in snake
            ):
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                if new_head == food_pos:
                    score += 1
                    food_pos = get_random_position()
                else:
                    snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food_pos)

        score_text = font.render(f"Score: {score}  |  {difficulty['label']}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            show_text("GAME OVER", "large", WHITE, -30)
            show_text("Press 'E' to Restart", "small", GRAY, 20)

        pygame.display.flip()
        clock.tick(difficulty["fps"])

if __name__ == "__main__":
    main()
