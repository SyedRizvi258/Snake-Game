import pygame
import time
import random

pygame.init()

# Define colors for various game elements
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (255,50,80)
green = (0,255,0)
blue = (50,153,213)

# Screen dimensions
width = 600
height = 400

# Display and caption of the screen
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Syed')

# Initialize clock to control game speed
clock = pygame.time.Clock()

# Default snake size and snake speed
snake = 10
snake_speed = 15

# Fonts for score and messages
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score on the top left part of the screen
def player_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

# Function to draw a snake consisting of a series of black rectangles (each representing one part of the snake's body)
def snake_s(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake, snake])

# Function to print a message when the game ends
def message(msg, color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [width/6, height/3])

# Main game loop
def game_loop():
    game_end = False #Flag to check if the game has ended
    game_close = False #Flag to check if the game has closed

    # Initial position of the snake (center of the screen)
    x1 = width/2
    y1 = height/2

    # Variables to track the change in the snake's position
    x1_change = 0
    y1_change = 0

    snake_list = [] #List to store the snake's body parts (as coordinates)
    snake_len = 1 #Initial length of the snake

    #randomized x and y coordinates of the food (rounded to the nearest 10)
    food_x = round(random.randrange(0, width - snake)/10.0) * 10.0
    food_y = round(random.randrange(0, height - snake)/10.0) * 10.0

    # Main game loop to keep the game running
    while not game_end:

        # When the game is over, display message and allow player to quit or play again
        while game_close:
            dis.fill(blue)
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

        # Initialize the current direction
        current_direction = None

        # Event handling for arrow keys to control snake direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    x1_change = -snake # move left
                    y1_change = 0
                    current_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    x1_change = snake # move right
                    y1_change = 0
                    current_direction = "RIGHT"
                elif event.key == pygame.K_UP and current_direction != "DOWN":
                    x1_change = 0
                    y1_change = -snake # move up
                    current_direction = "UP"
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    x1_change = 0
                    y1_change = snake # move down
                    current_direction = "DOWN"

        # Game ends if the player touches the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Fill the screen with blue color before drawing the snake and food
        dis.fill(blue)

        # Draw the food for the snake
        pygame.draw.rect(dis, green, [food_x, food_y, snake, snake])
        
        # Track the snake's head position and add it to the snake list
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        # Remove the tail of the snake to simulate movement 
        if len(snake_list) > snake_len:
            del snake_list[0]

        # Game ends if the snake touches itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        snake_s(snake, snake_list)

        # Display the score on the screen
        player_score(snake_len - 1)

        pygame.display.update()

        # Check if the snake eats the food and generate new food location
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake)/10.0) * 10.0
            food_y = round(random.randrange(0, height - snake)/10.0) * 10.0
            snake_len += 1 # Increase the snake length by 1
            
        clock.tick(snake_speed) # Control the speed of the game
    
    pygame.quit() # Quit the game
    quit()

game_loop() # Start the game
