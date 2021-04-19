import pygame, random

pygame.init()

pygame.display.set_icon(pygame.image.load("icon.png"))
brushImage = pygame.transform.scale(pygame.image.load("brush.png"), (30, 30))
eraserImage = pygame.transform.scale(pygame.image.load("eraser.png"), (30, 30))
saveImage = pygame.transform.scale(pygame.image.load("save.png"), (90, 40))

font = pygame.font.SysFont('freesansbold.ttf', 25)

black = (0, 0, 0)
white = (255, 255, 255)
red = (204, 0, 0)
blue = (0, 128, 255)
purple = (127, 0, 255)
pink = (255, 153, 153)
green = (0, 255, 0)
orange = (255, 153, 51)
gray = (96, 96, 96)
yellow = (255, 255, 102)
gray1 = (221, 221, 221)
mint = (102, 255, 178)
yellow1 = (255, 255, 204)
pink1 = (255, 204, 204)
mint1 = (153, 255, 204)
blue1 = (102, 255, 255)
orange1 = (255, 204, 153)
green1 = (153, 255, 153)
purple1 = (229, 204, 255)
red1 = (255, 51, 51)

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

def drawRect(screen, start, end, color,rad):
    x1=start[0]
    y1=start[1]
    x2=end[0]
    y2=end[1]
    width=x2-x1
    height=y2-y1
    pygame.draw.rect(screen,color,(x1,y1,width,height),rad)

def drawCircle(screen,start, end, color,rad):
    x1=start[0]
    y1=start[1]
    x2=end[0]
    y2=end[1]
    width=x2-x1
    height=y2-y1
    pygame.draw.ellipse(screen,color,(x1,y1,width,height),rad)

def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255,255,255))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    func='l'

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    
    pygame.draw.rect(screen, gray1, (700, 0, 700, 600))
    pygame.draw.line(screen, gray, (700, 0), (700, 600), 4)
    pygame.draw.line(screen, gray, (1, 0), (1, 600), 4)
    pygame.draw.line(screen, gray, (0, 598), (800, 598), 4)
    pygame.draw.line(screen, gray, (0, 1), (800, 1), 4)
    pygame.draw.line(screen, gray, (798, 0), (798, 600), 4)

    tools_text = font.render('Tools:', True, gray)
    screen.blit(tools_text, (710, 10))
    colors_text = font.render('Colors:', True, gray)
    screen.blit(colors_text, (710, 245))
    size_text = font.render('SIZE:', True, gray)
    screen.blit(size_text, (710, 140))
    pygame.draw.rect(screen, white, (715, 170, 70, 70))
    pygame.draw.rect(screen, white, (710, 30, 80, 80))
    
    pygame.draw.rect(screen, black, (718, 77, 25, 25), 2)
    pygame.draw.circle(screen, black, (770, 90), 12, 2)
   
    screen.blit(brushImage, (715, 37))
    screen.blit(eraserImage, (755, 37))
    screen.blit(saveImage, (705, 550))

    colors_list1 = [yellow, pink, mint, blue, orange, green, purple, red, black]

    colors_list2 = [yellow1, pink1, mint1, blue1, orange1, green1, purple1, red1]

    colors_circle1 = []
    colors_circle2 = []

    for cl, i in enumerate(range(285, 555, 30), 0):
        pygame.draw.circle(screen, colors_list1[cl], (725, i), 14)
        colors_circle1.append(pygame.Rect((725, i, 50, 25)))
        
    for cl, i in enumerate(range(285, 525, 30), 0):
        pygame.draw.circle(screen, colors_list2[cl], (770, i), 14)
        colors_circle2.append(pygame.Rect((770, i, 50, 25)))

    pygame.display.update()

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_l:
                    func='l'
                if event.key == pygame.K_p:
                    func='r'
                if event.key == pygame.K_c:
                    func='c'
                if event.key == pygame.K_e:
                    func='e'
                if event.key == pygame.K_UP:
                    pygame.draw.rect(screen, white, (715, 170, 70, 70))
                    radius += 1
                if event.key == pygame.K_DOWN:
                    pygame.draw.rect(screen, white, (715, 170, 70, 70))
                    radius -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random' and func=='l':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                elif func=='l':
                    color = colors[mode]
                if func=='l':
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True
                if func=='e':
                    pygame.draw.circle(screen, (255,255,255),event.pos,radius)
                    draw_on = True
            if event.type == pygame.MOUSEBUTTONUP and (func=='l' or func=='e'):
                draw_on = False
            if event.type == pygame.MOUSEBUTTONDOWN and (func=='r' or func=='c'):
                start_pos=event.pos
            if event.type == pygame.MOUSEBUTTONUP and (func=='r' or func=='c'):
                last_pos=event.pos
                if func=='r':
                    drawRect(screen,start_pos,last_pos,color,radius)
                elif func=='c':
                    drawCircle(screen,start_pos,last_pos,color,radius)
            if event.type == pygame.MOUSEMOTION and (func=='l' or func=='e'):
                if draw_on and func=='l':
                    drawLine(screen, last_pos, event.pos, radius, color)
                if draw_on and func=='e':
                    drawLine(screen, last_pos, event.pos, radius,(255,255,255))
                last_pos = event.pos

           
        radius_text = font.render(f'R = {radius}', True, black)     
        screen.blit(radius_text, (720, 190))
        pygame.display.flip()

    pygame.quit()

main()

