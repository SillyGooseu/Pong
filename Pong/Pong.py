import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Game objects
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
player_paddle = pygame.Rect(20, HEIGHT // 2 - 40, 10, 80)
ai_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - 40, 10, 80)

ball_dx, ball_dy = BALL_SPEED, BALL_SPEED
player_dy = 0

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                player_dy = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_dy = 0

    # Move player paddle
    player_paddle.y += player_dy
    player_paddle.y = max(0, min(HEIGHT - player_paddle.height, player_paddle.y))

    # AI logic (tracks the ball)
    if ai_paddle.centery < ball.centery:
        ai_paddle.y += PADDLE_SPEED
    elif ai_paddle.centery > ball.centery:
        ai_paddle.y -= PADDLE_SPEED
    ai_paddle.y = max(0, min(HEIGHT - ai_paddle.height, ai_paddle.y))

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_dx *= -1

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
        ball_dx, ball_dy = random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])

    # Draw objects
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
