import pygame
import random

pygame.init()

screen_x = 1000
screen_y = 500

points_left = 0
points_right = 0

p_width = 15
p_height = 100
p_speed = 15

ball_r = 10
ball_speed = 6
ball_d = ball_r * 2

ball_start_x = screen_x / 2 - ball_r
ball_start_y = screen_y / 2 - ball_r

fps = 60

screen = pygame.display.set_mode((screen_x, screen_y))

platform_right = pygame.Rect(
    screen_x - p_width - 5, screen_y / 2 - p_height / 2, p_width, p_height
)
platform_left = pygame.Rect(5, screen_y / 2 - p_height / 2, p_width, p_height)
ball = pygame.Rect(ball_start_x, ball_start_y, ball_d, ball_d)

font = pygame.font.Font(None, 50)

dx = 1
dy = -1

green = (0, 133, 35)

clock = pygame.time.Clock()

pygame.display.set_caption("Ping-Pong Pixel Game")
game = True
while game:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and platform_right.top > 0:
        platform_right.top -= p_speed
    elif key[pygame.K_DOWN] and platform_right.bottom < screen_y:
        platform_right.bottom += p_speed
    elif key[pygame.K_w] and platform_left.top > 0:
        platform_left.top -= p_speed
    elif key[pygame.K_s] and platform_left.bottom < screen_y:
        platform_left.bottom += p_speed

    pygame.draw.rect(screen, pygame.Color("White"), platform_right)
    pygame.draw.rect(screen, pygame.Color("White"), platform_left)

    pygame.draw.circle(screen, pygame.Color("White"), ball.center, ball_r)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centery < ball_r or ball.centery > screen_y - ball_r:
        dy = -dy
    elif ball.colliderect(platform_left) or ball.colliderect(platform_right):
        dx = -dx

    if ball.centerx > screen_x:
        points_right += 1
        ball.x = ball_start_x
        ball.y = ball_start_y
    elif ball.centerx < 0:
        points_left += 1
        ball.x = ball_start_x
        ball.y = ball_start_y

    right_text = font.render(f"{points_left}", True, pygame.Color("White"))
    screen.blit(right_text, (screen_x - 40, 20))

    left_text = font.render(f"{points_right}", True, pygame.Color("White"))
    screen.blit(left_text, (20, 20))

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()