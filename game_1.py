import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Arsenal Dash!")

# Load image
arsenal_img = pygame.image.load("Arsenal.png").convert()
arsenal_img.set_colorkey((255, 255, 255)) # Set white to be transparent
arsenal_img = pygame.transform.scale(arsenal_img, (64, 64))

# Font
font = pygame.font.Font(None, 36)

# Clock and timer
clock = pygame.time.Clock()
timer = 30  # seconds
start_ticks = pygame.time.get_ticks()

# Game state
x = 0
y = 300
speed = 200
score = 0

# Target rectangle
target = pygame.Rect(500, y, 64, 64)

running = True

while running:
    dt = clock.tick(60) / 1000  # Delta time

    # Timer countdown
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, timer - int(seconds_passed))
    
    if time_left <= 0:
        running = False  # Time's up!

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Arsenal
    x += speed * dt

    # Collision detection
    arsenal_rect = pygame.Rect(x, y, 64, 64)
    if arsenal_rect.colliderect(target):
        score += 1
        x = 0  # Reset Arsenal
        y = random.randint(50, 400)
        target.y = y

    # Drawing
    screen.fill((200, 255, 255))  # Light blue background
    screen.blit(arsenal_img, (x, y))
    pygame.draw.rect(screen, (255, 100, 100), target)

    # Score + Timer display
    score_text = font.render(f"Goals: {score}", True, (0, 0, 0))
    timer_text = font.render(f"Time Left: {time_left}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    screen.blit(timer_text, (20, 60))

    pygame.display.flip()

pygame.quit()
print(f"Final Score: {score}")
