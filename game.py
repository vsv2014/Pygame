import pygame
from obstacles import *
import config
from random import randint
from random import seed, random

"""Imports the pygame modules , random library modules and also imports all 
definitions and functions from the config file obstacles.py"""


pygame.init()

def obstacle_draw(obstacles):
    for obstacle in obstacles:
        obstacle.draw()

"""Function to draw all obstacles present in the obstacle(sprite list"""

yellow = (243, 229, 9)
green = (0, 255, 0)
blue = (0, 0, 128)

clock = pygame.time.Clock()
backcolor = pygame.color.Color('#C2C5CC')

rectanglecolor = pygame.color.Color('#00FF00')

deer_img = pygame.transform.scale(pygame.image.load('deer.png'), (70, 70))
deer_img = pygame.transform.flip(deer_img, True, False)

def deer(x, y):
    screen.blit(deer_img, (x, y))

x = (width * 0.45)
y = (height * 0.93)

obst_list = []
mov_obstacle_list = []
all_sprites_list = []

cat_img = pygame.transform.scale(pygame.image.load('cat.png'), (70, 70))

def cat(a, b):
    screen.blit(cat_img, (a, b))

y2 = (height * 0.005)
x2 = (width * 0.75)

"""Functions to display player1(deer) and player2(cat) respectively 
according to the coordinates given as parameters"""



"""FONTS ETC"""
font = pygame.font.Font('freesansbold.ttf', 32)

score = font.render('score: 0', True, green, blue)

wonp1 = font.render('Player 1 wins!!', True, green, blue)
wonp2 = font.render('Player 2 wins!!', True, green, blue)
start = font.render('START', True, blue, None)
text = font.render('YOU LOSE!!', True, green, blue)
end = font.render('END', True, blue, None)

startRect = start.get_rect()
endRect = end.get_rect()
wonrectangle1 = wonp1.get_rect()
wonrectangle2 = wonp2.get_rect()
textRect = text.get_rect()
scoreRect = score.get_rect()

scoreRect.center = (100, 20)
scoreRect.center = (100, 20)
startRect.center = (1200, 970)
endRect.center = (1200, 20)

wonrectangle1.center = (width // 2, height // 2)
wonrectangle2.center = (width // 2, height // 2)
textRect.center = (width // 2, height // 2)
screen.fill(backcolor)


font2 = pygame.font.Font(None, 29)
config.sc = '5'


"""This block of code defines all the fonts and their styles"""



#making the backgrounds and rectangles
pygame.draw.rect(screen, (rectanglecolor), (0, 0, 1320, 72))
pygame.draw.rect(screen, (rectanglecolor), (0, 232, 1320, 72))
pygame.draw.rect(screen, (rectanglecolor), (0, 464, 1320, 72))
pygame.draw.rect(screen, (rectanglecolor), (0, 696, 1320, 72))
pygame.draw.rect(screen, (rectanglecolor), (0, 928, 1320, 72))

for i in range(0, 5):
    sh1 = car(i * 250, 800)
    all_sprites_list.append(sh1)
    mov_obstacle_list.append(sh1)

    sh1 = car(i * 280, 570)
    all_sprites_list.append(sh1)
    mov_obstacle_list.append(sh1)

    sh1 = car(i * 220, 340)
    all_sprites_list.append(sh1)
    mov_obstacle_list.append(sh1)

    sh1 = car(i * 180, 110)
    all_sprites_list.append(sh1)
    mov_obstacle_list.append(sh1)

    if i == 0:
        cact = cactus(0, 688)
        all_sprites_list.append(cact)
        obst_list.append(cact)
        cact = cactus(0, 228)
        all_sprites_list.append(cact)
        obst_list.append(cact)
        cact = cactus(0, 458)
        all_sprites_list.append(cact)
        obst_list.append(cact)
    elif i == 4:
        cact = cactus(1100, 688)
        all_sprites_list.append(cact)
        obst_list.append(cact)
        cact = cactus(1100, 228)
        all_sprites_list.append(cact)
        obst_list.append(cact)
        cact = cactus(1100, 458)
        all_sprites_list.append(cact)
        obst_list.append(cact)
    else:
        cact = cactus(randint(0, 1175), 688)
        all_sprites_list.append(cact)
        obst_list.append(cact)
        cact = cactus(randint(0, 1175), 228)
        all_sprites_list.append(cact)
        cact = cactus(randint(0, 1175), 458)
        obst_list.append(cact)
        all_sprites_list.append(cact)
        obst_list.append(cact)



"""All these loops add the respective obstacles(moving or stationary) to 
their lists along with the position they are supposed to be displayed at"""

pygame.display.flip()
time = 0
score = font.render('score: ' + config.sc, True, green, blue)

pygame.mixer.music.load("deer_song.mp3")
pygame.mixer.music.play(-1)

"""Loads the music and plays it in an infinite loop"""
"""bish"""
def p1end():
    global time
    config.player_1_score = int(config.sc)
    config.player_1_time = time
    print(config.player_1_time)
    # screen.blit(win, wonrectangle)
    pygame.display.flip()
    pygame.time.delay(1500)
    config.sc = '0'
    config.st_pos = 20
    config.end_pos = 970
    config.start_time_flag = 0
    config.round = 1
    config.x2_move = 0
    config.y2_move = 0
    time=0
    global x
    x = (width * 0.45)
    global y
    y = (height * 0.93)


def p2end():
    global time
    config.lost = 0
    config.victory = 0
    pygame.display.flip()
    pygame.time.delay(1500)
    config.sc = '0'
    config.st_pos = 970
    config.end_pos = 20
    config.round = 0
    config.x_move = 0
    config.y_move = 0
    time=0
    global x2
    global y2
    x2 = (width * 0.75)
    y2 = (height * 0.005)


while not config.done:

    if not config.round:
        if y + 20 <= 928:
            config.start_time_flag = 1

    else:
        if y2 + 35 >= 70:
            config.start_time_flag = 1

    if config.start_time_flag:
        time += 1

        """This assures that the timer only starts when the players cross the first rectangle fully"""

    score = font.render('score: ' + config.sc, True, green, blue)
    startRect.center = (1200, config.st_pos)
    endRect.center = (1200, config.end_pos)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.done = True
        if not config.round:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    config.x_move = -5
                    config.y_move = 0
                    deer_img = pygame.transform.flip(deer_img, True, False)
                elif event.key == pygame.K_RIGHT:
                    config.x_move = 5
                    config.y_move = 0
                    deer_img = pygame.transform.flip(deer_img, True, False)

                if event.key == pygame.K_UP:
                    config.x_move = 0
                    config.y_move = -5

                elif event.key == pygame.K_DOWN:
                    config.x_move = 0
                    config.y_move = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    config.x_move = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    config.y_move = 0

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    config.x2_move = -5
                    config.y2_move = 0
                    cat_img = pygame.transform.flip(
                        cat_img, True, False)
                elif event.key == pygame.K_d:
                    config.x2_move = 5
                    config.y2_move = 0
                    cat_img = pygame.transform.flip(
                        cat_img, True, False)

                if event.key == pygame.K_w:
                    config.x2_move = 0
                    config.y2_move = -5

                elif event.key == pygame.K_s:
                    config.x2_move = 0
                    config.y2_move = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    config.x2_move = 0
                
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    config.y2_move = 0
                obst_list.append(cact)

    if not config.round:
        x += config.x_move
        y += config.y_move
    else:
        x2 += config.x2_move
        y2 += config.y2_move

    """These for loops are the event handling mechanisms for controling the 
    players with arrow keys and wasd keys respectively"""

    screen.fill(backcolor)
   
    if x > (width - 70):
        x = (width - 70)
    elif x < 0:
        x = 0

    if x2 > (width - 70):
        x2 = (width - 70)
    elif x2 < 0:
        x2 = 0

    if y > (height - 70):
        y = (height - 70)
    elif y < 0:
        y = 0

    if y2 > (height - 70):
        y2 = (height - 70)
    elif y2 < 0:
        y2 = 0

    pygame.draw.rect(screen, (rectanglecolor), (0, 928, 1320, 72))
    pygame.draw.rect(screen, (rectanglecolor), (0, 696, 1320, 72))
    pygame.draw.rect(screen, (rectanglecolor), (0, 464, 1320, 72))
    pygame.draw.rect(screen, (rectanglecolor), (0, 232, 1320, 72))
    pygame.draw.rect(screen, (rectanglecolor), (0, 0, 1320, 72))

    """Gives boundaries so player doesnt go beyond the screen"""

    deer(x, y)
    cat(x2, y2)
    screen.blit(score, scoreRect)

    player_hitbox = (x + 13, y + 5, 50, 55)
    player2_hitbox = (x2 + 13, y2 + 5, 50, 60)
    screen.blit(start, startRect)

    player_x = player_hitbox[0]
    player2_x = player2_hitbox[0]
    screen.blit(end, endRect)

    player_y = player_hitbox[1]
    player2_y = player2_hitbox[1]

    obstacle_draw(obst_list)
    obstacle_draw(mov_obstacle_list)

    l = len(mov_obstacle_list)

    """Defines hitboxes for the sprites as well as the players for collision 
    detection"""

    for i in range(0, l):
        if not config.round:
            mov_obstacle_list[i].update(config.speed1)

        else:
            mov_obstacle_list[i].update(config.speed2)

    """Moves the cars"""

    if not config.round:

        if player_y > 800:
            config.sc = '0'

        if player_y < 800 and player_y > 696:
            config.sc = '10'

        if player_y < 696 and player_y > 570:
            config.sc = '15'

        if player_y < 570 and player_y > 464:
            config.sc = '25'

        if player_y < 464 and player_y > 340:
            config.sc = '30'

        if player_y < 340 and player_y > 232:
            config.sc = '40'

        if player_y < 232 and player_y > 110:
            config.sc = '45'

        if player_y < 110 and player_y > 0:
            config.sc = '55'

        """Updates the scores according to position of player1"""

        if y == 0:
            p1end()
            config.victory = 1
        """Code for when player1 has reached the end"""

    else:

        if player2_y + 60 < 175:
            config.sc = '0'

        if player2_y + 60 > 175 and player2_y + 60 < 307:
            config.sc = '10'

        if player2_y + 60 > 307 and player2_y + 60 < 405:
            config.sc = '15'

        if player2_y + 60 > 405 and player2_y + 60 < 539:
            config.sc = '25'

        if player2_y + 60 > 539 and player2_y + 60 < 635:
            config.sc = '30'

        if player2_y + 60 > 635 and player2_y + 60 < 771:
            config.sc = '40'

        if player2_y + 60 > 771 and player2_y + 60 < 865:
            config.sc = '45'

        if player2_y + 60 > 865 and player2_y + 60 < height:
            config.sc = '55'

        """Updates the score according to the position of player2"""

        if y2 + 70 == height:

            config.start_time_flag = 0
            config.player_2_score = int(config.sc)
            config.player_2_time = time
            print(config.player_2_time)

            if not config.lost:
                if config.player_2_score == config.player_1_score:
                    if config.player_1_time >= config.player_2_time:
                        config.speed2 += 0.3
                        screen.blit(wonp2, wonrectangle2)
                    else:
                        config.speed1 += 0.3
                        screen.blit(wonp1, wonrectangle1)
                else:
                    if config.player_1_score > config.player_2_score:
                        config.speed1 += 0.3
                        screen.blit(wonp1, wonrectangle1)
                    else:
                        config.speed2 += 0.3
                        screen.blit(wonp2, wonrectangle2)

            else:
                screen.blit(wonp2, wonrectangle2)

            p2end()
    #code for when player2 reaches the end
    for ent in obst_list:

        if not config.round:
            if player_x <= ent.hitbox[0] + 115 and player_x > ent.hitbox[0]:
                if player_y <= ent.hitbox[1] + 80 and player_y > ent.hitbox[1]:
                    p1end()
                    config.lost = 1
                    break

            elif player_x + 50 >= ent.hitbox[0] and player_x + 50 < ent.hitbox[0] + 115:
                if player_y > ent.hitbox[1] and player_y <= ent.hitbox[1] + 80:
                    p1end()
                    config.lost = 1
                    break

            elif player_x <= ent.hitbox[0] + 115 and player_x > ent.hitbox[0]:
                if player_y + 55 >= ent.hitbox[1] and player_y + 55 < \
                        ent.hitbox[1] + 80:
                    p1end()
                    config.lost = 1
                    break

            elif player_x + 50 <= ent.hitbox[0] + 115 and player_x + 50 > \
                    ent.hitbox[0]:
                if player_y + 55 >= ent.hitbox[1] and player_y + 55 < \
                        ent.hitbox[1] + 80:
                    p1end()
                    config.lost = 1
                    break

            elif player_x + 50 >= ent.hitbox[0] and player_x + 50 < ent.hitbox[
                    0] + 115:
                if player_y <= ent.hitbox[1] and player_y + 55 >= ent.hitbox[
                        1] + 80:
                    p1end()
                    config.lost = 1
                    break

            #This code is to handle collision detection of player1 with stationary objects"""

        else:

            if player2_x <= ent.hitbox[0] + 115 and player2_x > ent.hitbox[0]:
                if player2_y > ent.hitbox[1] and player2_y <= ent.hitbox[
                        1] + 80:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    else:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 >= ent.hitbox[0] and player2_x + 50 < ent.hitbox[
                    0] + 115:
                if player2_y > ent.hitbox[1] and player2_y <= ent.hitbox[
                        1] + 80:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    else:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x <= ent.hitbox[0] + 115 and player2_x > ent.hitbox[0]:
                if player2_y + 60 >= ent.hitbox[1] and player2_y + 60 < \
                        ent.hitbox[1] + 80:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    else:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 <= ent.hitbox[0] + 115 and player2_x + 50 > \
                    ent.hitbox[0]:
                if player2_y + 60 >= ent.hitbox[1] and player2_y + 60 < \
                        ent.hitbox[1] + 80:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    else:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 >= ent.hitbox[0] and player2_x + 50 < ent.hitbox[
                    0] + 115:
                if player2_y <= ent.hitbox[1] and player2_y + 60 >= ent.hitbox[
                        1] + 80:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    else:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            #This code is to handle collision detection of player2 with            stationary objects"""

    for ent in mov_obstacle_list:

        if not config.round:
            if player_x <= ent.hitbox[0] + 110 and player_x > ent.hitbox[0]:
                if player_y > ent.hitbox[1] and player_y <= ent.hitbox[1] + 39:
                    p1end()
                    config.lost = 1
                    break

            if player_x + 50 >= ent.hitbox[0] and player_x + 50 < ent.hitbox[
                    0] + 110:
                if player_y > ent.hitbox[1] and player_y <= ent.hitbox[1] + 39:
                    p1end()
                    config.lost = 1
                    break

            if player_x <= ent.hitbox[0] + 110 and player_x > ent.hitbox[0]:
                if player_y + 55 >= ent.hitbox[1] and player_y + 55 < \
                        ent.hitbox[1] + 39:
                    p1end()
                    config.lost = 1
                    break

            if player_x + 50 <= ent.hitbox[0] + 110 and player_x + 50 > \
                    ent.hitbox[0]:
                if player_y + 55 >= ent.hitbox[1] and player_y + 55 < \
                        ent.hitbox[1] + 39:
                    p1end()
                    config.lost = 1
                    break

            if player_x + 50 >= ent.hitbox[0] and player_x + 50 < ent.hitbox[
                    0] + 110:
                if player_y <= ent.hitbox[1] and player_y + 55 >= ent.hitbox[
                        1] + 39:
                    p1end()
                    config.lost = 1
                    break

            if player_x <= ent.hitbox[0] + 110 and player_x > ent.hitbox[0]:
                if player_y < ent.hitbox[1] and player_y + 55 >= ent.hitbox[
                        1] + 39:
                    p1end()
                    config.lost = 1
                    break

            #This code is to handle collision detection of player1 with moving objects"""

        else:

            if player2_x <= ent.hitbox[0] + 110 and player2_x > ent.hitbox[0]:
                if player2_y > ent.hitbox[1] and player2_y <= ent.hitbox[
                        1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 >= ent.hitbox[0] and player2_x + 50 < ent.hitbox[
                    0] + 110:
                if player2_y > ent.hitbox[1] and player2_y <= ent.hitbox[
                        1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x <= ent.hitbox[0] + 110 and player2_x > ent.hitbox[0]:
                if player2_y + 60 >= ent.hitbox[1] and player2_y + 60 < \
                        ent.hitbox[1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 <= ent.hitbox[0] + 110 and player2_x + 50 > \
                    ent.hitbox[0]:
                if player2_y + 60 >= ent.hitbox[1] and player2_y + 60 < \
                        ent.hitbox[1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x + 50 >= ent.hitbox[0] and player2_x + 50 < ent.hitbox[
                    0] + 110:
                if player2_y <= ent.hitbox[1] and player2_y + 60 >= ent.hitbox[
                        1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            if player2_x <= ent.hitbox[0] + 110 and player2_x > ent.hitbox[0]:
                if player2_y < ent.hitbox[1] and player2_y + 55 >= ent.hitbox[
                        1] + 39:
                    config.player_2_score = int(config.sc)
                    config.player_2_time = time
                    time = 0
                    config.start_time_flag = 0
                    
                    if not config.victory:
                        if config.player_2_score == config.player_1_score:
                            if config.player_1_time >= config.player_2_time:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                            else:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                        else:
                            if config.player_1_score > config.player_2_score:
                                screen.blit(wonp1, wonrectangle1)
                                config.speed1 += 0.3
                            else:
                                screen.blit(wonp2, wonrectangle2)
                                config.speed2 += 0.3
                        pygame.display.flip()

                    if config.victory:
                        screen.blit(wonp1, wonrectangle1)

                    p2end()
                    break

            """This code is to handle collision detection of player2 with 
                        moving objects"""

    pygame.display.flip()
    """Updates everything"""
    clock.tick(1020)
    """Clock tick speed (frames per second)"""

pygame.quit()

"""Quits the game once close is pressed"""