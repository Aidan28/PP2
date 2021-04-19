import pygame
from random import randrange
import sys
import time
import pygame_menu

res = 600
size = 30 

pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
pygame.display.set_caption("жуланчик")
font_score = pygame.font.SysFont('Arial', 26, bold = True)
font_end = pygame.font.SysFont('Arial', 66, bold = True)
img = pygame.image.load('gui.png').convert() 
bg_intro = pygame.image.load('1.jpg')

def start_the_game(): 
    x, y = randrange(0, res, size), randrange(0, res, size)
    food = randrange(0, res, size), randrange(0, res, size)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    score = 0
    fps = 4

    green = (124, 252, 0)
    red = (255, 0, 0)
    coral = (255, 127, 80)

    running = True

    while running:
        screen.blit(img, (0, 0))

        #drawing snack and food
        for i in snake:
            pygame.draw.rect(screen, green, (i[0], i[1], size - 2, size - 2))
        screen.blit(pygame.image.load('food.png'), (food[0], food[1]))

        #show score
        render_score = font_score.render(f'SCORE: {score}', 1, coral)
        screen.blit(render_score, (5, 5))

        #snake movement
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length:]

        #eating food
        if snake[-1] == food:
            food = randrange(0, res, size), randrange(0,res, size)
            length += 1
            score += 1
            if length % 3 == 0:
                fps += 1 

        #when game over 
        if x < 0 + size or x == res - size or y < size or y == res- size or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', 1, coral)
                screen.blit(render_end, (res // 2 - 200, res // 3))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
        

        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                if event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                if event.key == pygame.K_DOWN:
                    dx, dy = 0, 1
                    
menu = pygame_menu.Menu(220, 300, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='player 1')

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_intro, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()

        
