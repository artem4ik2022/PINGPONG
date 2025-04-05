import pygame
import random
import os

# INIT Pygame
pygame.init()

#INIT
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 15
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
record = 0
try:
    with open("Record.txt", "r") as file:
        record = int(file.read())
except:
    print("123")
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#END INIT

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")
clock = pygame.time.Clock()

#OBJ
player = pygame.Rect(WIDTH//2 - 50, HEIGHT-15, 100, 15)
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 15, 15)

#SPEEDS
player_speed = 0
ball_speed_x = random.randint(1, 5) * random.choice((1, -1))
ball_speed_y = 4


def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    return random.randint(1, 5) * random.choice((1, -1)), 4

def move_ball():
    global ball_speed_x, ball_speed_y, score, record
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left < 0 or ball.right > WIDTH:
        ball_speed_x *= -1

    if ball.colliderect(player):
        ball_speed_y *= -1
        score += 1

    if ball.top < 0:
        # ball_speed_x, ball_speed_y = reset_ball()
        ball_speed_y *= -1

    if ball.bottom > HEIGHT:
        ball_speed_x, ball_speed_y = reset_ball()
        if record < score:
            record = score
            with open("Record.txt", "w") as file:
                file.write(str(record))
        score = 0

def move_player():
    player.x += player_speed
    if player.left <= 0:
        player.left = 0
    if player.right >= WIDTH:
        player.right = WIDTH

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed = 7
            if event.key == pygame.K_LEFT:
                player_speed = -7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_speed = 0

    #DRAWING
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.ellipse(screen, WHITE, ball)
    player_score_text = font.render(f"Score: {score}", False, WHITE)
    screen.blit(player_score_text, (WIDTH // 4, 20))
    player_record_text = font.render(f"High score: {record}", False, WHITE)
    screen.blit(player_record_text, (WIDTH - 350, 20))

    #GAME PROCESS
    move_ball()
    move_player()

    #UPDTING
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()