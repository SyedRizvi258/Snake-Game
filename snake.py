import pygame
import random
import sys

class SnakeGame:
    def __init__(self):
        pygame.init()

        # Define colors for various game elements
        self.yellow = (255, 255, 102)
        self.red = (255, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.black = (0, 0, 0)

        # Screen dimensions
        self.width = 600
        self.height = 400

        # Display and caption of the screen
        self.dis = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game by Syed')

        # Initialize clock to control game speed
        self.clock = pygame.time.Clock()

        # Default snake size and snake speed
        self.snake_size = 10
        self.snake_speed = 15

        # Fonts for score and messages
        self.font = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)

    # Function to display the score on the top left part of the screen
    def player_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.yellow)
        self.dis.blit(value, [0, 0])

    # Function to draw the snake using the loaded image
    def draw_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.black, [x[0], x[1], self.snake_size, self.snake_size])

    # Function to print a message when the game ends
    def message(self, msg, color):
        mesg = self.font.render(msg, True, color)
        self.dis.blit(mesg, [self.width / 6, self.height / 3])

    # Main game loop
    def game_loop(self):
        game_end = False  # Flag to check if the game has ended
        game_close = False  # Flag to check if the game has closed

        # Initial position of the snake (center of the screen)
        x1 = self.width / 2
        y1 = self.height / 2

        # Variables to track the change in the snake's position
        x1_change = 0
        y1_change = 0

        snake_list = []  # List to store the snake's body parts (as coordinates)
        snake_len = 1  # Initial length of the snake

        # Randomized x and y coordinates of the food (rounded to the nearest 10)
        food_x = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, self.height - self.snake_size) / 10.0) * 10.0

        # Main game loop
        while not game_end:
            while game_close:
                self.dis.fill(self.blue)
                self.message("You Lost! Press Q-Quit or C-Play Again", self.red)
                self.player_score(snake_len - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_end = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.game_loop()

            current_direction = None

            # Event handling for arrow keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = True
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                        x1_change = -self.snake_size  # move left
                        y1_change = 0
                        current_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                        x1_change = self.snake_size  # move right
                        y1_change = 0
                        current_direction = "RIGHT"
                    elif event.key == pygame.K_UP and current_direction != "DOWN":
                        x1_change = 0
                        y1_change = -self.snake_size  # move up
                        current_direction = "UP"
                    elif event.key == pygame.K_DOWN and current_direction != "UP":
                        x1_change = 0
                        y1_change = self.snake_size  # move down
                        current_direction = "DOWN"

            # Game ends if the player touches the boundary
            if x1 >= self.width or x1 < 0 or y1 >= self.height or y1 < 0:
                game_close = True

            # Update the snake's position
            x1 += x1_change
            y1 += y1_change

            # Fill the screen with blue before drawing the snake and food
            self.dis.fill(self.blue)

            # Draw the food for the snake using the loaded image
            pygame.draw.rect(self.dis, self.green, [food_x, food_y, self.snake_size, self.snake_size])

            # Track the snake's head position
            snake_head = [x1, y1]
            snake_list.append(snake_head)

            # Remove the tail of the snake to simulate movement
            if len(snake_list) > snake_len:
                del snake_list[0]

            # Game ends if the snake touches itself
            if snake_head in snake_list[:-1]:
                game_close = True

            # Draw the snake
            self.draw_snake(snake_list)

            # Display the score on the screen
            self.player_score(snake_len - 1)

            pygame.display.update()

            # Check if the snake eats the food and generate new food location
            if x1 == food_x and y1 == food_y:
                food_x = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
                food_y = round(random.randrange(0, self.height - self.snake_size) / 10.0) * 10.0
                snake_len += 1  # Increase the snake length by 1

                # Increase speed every 5 segments
                if snake_len % 5 == 0:
                    self.snake_speed += 1 

            self.clock.tick(self.snake_speed)  # Control the speed of the game

        pygame.quit()  # Quit the game
        sys.exit()

# Create an instance of the game and start it
game = SnakeGame()
game.game_loop()
