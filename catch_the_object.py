import pygame # type: ignore
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Catch the Falling Object')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define player paddle
player_width = 100
player_height = 20
player_x = (screen_width // 2) - (player_width // 2)
player_y = screen_height - player_height - 10
player_speed = 10

# Define falling object
object_width = 50
object_height = 50
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height
object_speed = 5

# Set score and game clock
score = 0
font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

# Function to display score
def show_score(score):
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the key press for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the falling object
    object_y += object_speed
    if object_y > screen_height:
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)

    # Check for collision with the player
    if (object_x + object_width > player_x and object_x < player_x + player_width) and (object_y + object_height > player_y):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)
        object_speed += 0.5  # Increase object speed as score increases

    # Fill screen with white
    screen.fill(WHITE)

    # Draw player and falling object
    pygame.draw.rect(screen, BLACK, [player_x, player_y, player_width, player_height])
    pygame.draw.rect(screen, RED, [object_x, object_y, object_width, object_height])

    # Display score
    show_score(score)

    # Update the display
    pygame.display.update()

    # Set the game clock speed
    clock.tick(60)

# Quit the game
pygame.quit()
