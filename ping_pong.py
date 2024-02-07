import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
paddle_speed = 10

# Ball settings
ball_speed_x, ball_speed_y = 5, 5
ball_size = 10

# Player and Ball positions
player1_x, player1_y = 10, (SCREEN_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
player2_x, player2_y = SCREEN_WIDTH - 20, (SCREEN_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
ball_x, ball_y = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)

# Score
player1_score = 0
player2_score = 0

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player2_y += paddle_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= player1_x + PADDLE_WIDTH and player1_y < ball_y < player1_y + PADDLE_HEIGHT) or \
       (ball_x >= player2_x - ball_size and player2_y < ball_y < player2_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Ball goes out of bounds
    if ball_x <= 0:
        player2_score += 1
        ball_x, ball_y = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
        ball_speed_x, ball_speed_y = 5, 5
    elif ball_x >= SCREEN_WIDTH:
        player1_score += 1
        ball_x, ball_y = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
        ball_speed_x, ball_speed_y = -5, 5

    # Fill the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Draw scores
    font = pygame.font.Font(None, 36)
    text = font.render(f"{player1_score} : {player2_score}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, 10))

    # Update display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(60)

pygame.quit()
sys.exit()
