
print("This is a simple Python script.")
# name = input("Enter your name: ")
# print(f"Welcome, {name}!")  
# code to build a snake game using the pygame library
import pygame
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Direction enum
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = Direction.RIGHT

    def move(self):
        dx, dy = self.direction.value
        new_head = (self.body[0][0] + dx * GRID_SIZE, self.body[0][1] + dy * GRID_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        dx, dy = self.direction.value
        new_head = (self.body[0][0] + dx * GRID_SIZE, self.body[0][1] + dy * GRID_SIZE)
        self.body.insert(0, new_head)

    def check_collision(self):
        # Check wall collision
        if (self.body[0][0] < 0 or self.body[0][0] >= SCREEN_WIDTH or
            self.body[0][1] < 0 or self.body[0][1] >= SCREEN_HEIGHT):
            return True
        # Check self collision
        if self.body[0] in self.body[1:]:
            return True
        return False

# Food class
class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

# Game setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = Snake()
food = Food()
score = 0
running = True

# Game loop
while running:
    clock.tick(10)  # 10 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
                snake.direction = Direction.UP
            elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
                snake.direction = Direction.DOWN
            elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
                snake.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
                snake.direction = Direction.RIGHT

    snake.move()

    # Check food collision
    if snake.body[0] == (food.x, food.y):
        snake.grow()
        food.spawn()
        score += 10

    # Check collision
    if snake.check_collision():
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    screen.fill(BLACK)
    
    # Draw snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    # Draw food
    pygame.draw.rect(screen, RED, (food.x, food.y, GRID_SIZE, GRID_SIZE))
    
    pygame.display.flip()

pygame.quit()