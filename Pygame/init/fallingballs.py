import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
x_pos, y_pos = 0, 0
v = 100  # пикселей в секунду
fps = 60
falling = False
screen2 = pygame.Surface(screen.get_size())
r = 0
g = 0
b = 0
while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            r = int(random.random() * 255)
            g = int(random.random() * 255)
            b = int(random.random() * 255)
            pygame.draw.circle(screen, (r, g, b), (int(x_pos), int(y_pos)), 10)
            falling = True
    screen.fill((0, 0, 0))
    screen.blit(screen2, (0, 0))
    if falling:
        pygame.draw.circle(screen, (r, g, b), (int(x_pos), int(y_pos)), 10)
        y_pos += v / fps
        clock.tick(fps)
        if y_pos > 290:
            screen2.blit(screen, (0, 0))
            falling = False

    # обновление экрана
    pygame.display.flip()

pygame.quit()