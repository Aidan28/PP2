import pygame
import time
import random
import sys
pygame.init()

gray = (119, 118, 110)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()
carimg = pygame.image.load('car1.jpg')
backgroundpic = pygame.image.load("download12.jpg")
yellow_stripe = pygame.image.load("yellow strip.jpg")
stripe = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
coin = pygame.image.load("coin.png")
car_width = 56


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf,TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, blue, bright_blue, "play")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()


    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf,textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car1.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed"+str(passed), True, white)
    score = font.render("Score"+str(score), True, white)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("GAME OVER")


def background():
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_stripe, (390, 0))
    gamedisplays.blit(yellow_stripe, (390, 100))
    gamedisplays.blit(yellow_stripe, (390, 200))
    gamedisplays.blit(yellow_stripe, (390, 300))
    gamedisplays.blit(yellow_stripe, (390, 400))
    gamedisplays.blit(yellow_stripe, (390, 500))
    gamedisplays.blit(stripe, (120, 0))
    gamedisplays.blit(stripe, (120, 100))
    gamedisplays.blit(stripe, (120, 200))
    gamedisplays.blit(stripe, (680, 0))
    gamedisplays.blit(stripe, (680, 100))
    gamedisplays.blit(stripe, (680, 200))


def car(x, y):
    gamedisplays.blit(carimg, (x, y))

coinx, coiny = random.randrange(0.2 * display_width, 0.8 * display_width), 0
def game_loop():
    x = (350) 
    y = (480)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    
    def draw_coin():
        global coinx, coiny 
        gamedisplays.blit(coin, (coinx, coiny))
        coiny += 5
        if coiny >= display_width:
            coinx, coiny = random.randrange(0.2 * display_width, 0.8 * display_width), 0
            

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a: 
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gamedisplays.fill(gray)
        
        
        rel_y = y2 % backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
        draw_coin()
        
        if rel_y < 800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_stripe,(400,rel_y))
            gamedisplays.blit(yellow_stripe,(400,rel_y+100))
            gamedisplays.blit(yellow_stripe,(400,rel_y+200))
            gamedisplays.blit(yellow_stripe,(400,rel_y+300))
            gamedisplays.blit(yellow_stripe,(400,rel_y+400))
            gamedisplays.blit(yellow_stripe,(400,rel_y+500))
            gamedisplays.blit(yellow_stripe,(400,rel_y-100))
            gamedisplays.blit(stripe,(120,rel_y-200))
            gamedisplays.blit(stripe,(120,rel_y+20))
            gamedisplays.blit(stripe,(120,rel_y+30))
            gamedisplays.blit(stripe,(680,rel_y-100))
            gamedisplays.blit(stripe,(680,rel_y+20))
            gamedisplays.blit(stripe,(680,rel_y+30))
   
        y2 += obstacle_speed
        

        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 690 - car_width or x < 110:
            crash()
        if x > display_width - (car_width + 110) or x < 110:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 7)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed + 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf,textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
    
        pygame.display.update()
        clock.tick(60)

intro_loop()
game_loop()
pygame.quit()
quit()