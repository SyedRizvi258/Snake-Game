import pygame
import time
import random

pygame.init()

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (255,50,80)
green = (0,255,0)
blue = (50,153,213)

width = 600
height = 400

#Display and caption of the screen
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Syed')

#Game time
clock = pygame.time.Clock()

#Default snake size and snake speed
snake = 10
snake_speed = 20

font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Function to display the score on the top left part of the screen
def player_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

#Function to draw a snake consisting of a bunch of black rectangles
def snake_s(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake, snake])

#Function to print message when the game ends
def message(msg, color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [width/6, height/3])

def game_loop():
    game_end = False
    game_close = False

    x1 = width/2
    y1 = height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_len = 1

    #randomized x and y coordinates of the food
    food_x = round(random.randrange(0, width - snake)/10.0) * 10.0
    food_y = round(random.randrange(0, height - snake)/10.0) * 10.0

    while not game_end:

        while game_close == True:
            dis.fill(blue)

            #Prints this message when player loses
            message("You Lost! Press Q-Quit or C-Play Again", red)
            player_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #Game ends if Q/q is pressed
                    if event.key == pygame.K_q:
                        game_end = True
                        game_close = False
                    #Game restarts if C/c is pressed
                    if event.key == pygame.K_c:
                        game_loop()

        # moves the snake in the appropriate directions when the arrow keys are pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake

        #Game ends if the player touches the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        #Draws the food for the snake
        pygame.draw.rect(dis, green, [food_x, food_y, snake, snake])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_len:
            del snake_list[0]

        #Game ends if the snake touches itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
                
        snake_s(snake, snake_list)
        player_score(snake_len - 1)

        pygame.display.update()

        #If the snake eats the food then the next location of the food is determined
        #Increases the snake size by 1
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake)/10.0) * 10.0
            food_y = round(random.randrange(0, height - snake)/10.0) * 10.0
            snake_len += 1
            
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
