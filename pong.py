import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
BALL_RADIUS = 20
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_COLOR = (255, 0, 0)
BALL_COLOR = (0, 0, 255)  # Blue ball color
BACKGROUND_COLOR = (0, 0, 0)
BALL_SPEED = [0, 0]  # Initially, ball speed is set to (0, 0)

# Function to reset the game
def reset_game():
    global ball, paddle, BALL_SPEED, game_over, game_started, score
    ball = pygame.Rect(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)  # Initial position is the top-left corner
    paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
    BALL_SPEED = [10, 10]
    game_over = False
    game_started = False  # Reset game_started to False
    score = 0  # Initialize score to 0

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One-Player Pong")

# Initialize clock for controlling the game's speed
clock = pygame.time.Clock()

# Font for buttons and score display
font = pygame.font.Font(None, 36)

# Initialize game state
reset_game()

# Main game loop
running = True
start_button = font.render("Start Game", True, (255, 255, 255))
play_again_button = font.render("Play Again", True, (255, 255, 255))
game_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started and event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_x, mouse_y):
                game_started = True
                BALL_SPEED = [5, 5]  # Start the ball moving to the right

        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_again_button_rect.collidepoint(mouse_x, mouse_y):
                reset_game()  # Reset the game state
                game_started = True  # Start the game again

    keys = pygame.key.get_pressed()
    if game_started and not game_over:
        if keys[pygame.K_LEFT]:
            paddle.x -= 10
        if keys[pygame.K_RIGHT]:
            paddle.x += 10

    # Ball movement
    if game_started and not game_over:
        ball.x += BALL_SPEED[0]
        ball.y += BALL_SPEED[1]

    # Ball collision with walls
    if game_started and not game_over:
        if ball.left <= 0 or ball.right >= WIDTH:
            BALL_SPEED[0] = -BALL_SPEED[0]
        if ball.top <= 0:
            BALL_SPEED[1] = -BALL_SPEED[1]

    # Ball collision with paddle
    if game_started and not game_over:
        if ball.colliderect(paddle):
            BALL_SPEED[1] = -BALL_SPEED[1]
            score += 1  # Increment the score when the ball hits the paddle

    # Ball falls, game over
    if game_started and not game_over:
        if ball.bottom >= HEIGHT:
            game_over = True

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the paddle and ball
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.circle(screen, BALL_COLOR, ball.center, BALL_RADIUS)

    # Draw buttons
    if not game_started and not game_over:
        start_button_rect = screen.blit(start_button, (WIDTH // 2 - start_button.get_width() // 2, HEIGHT // 2))
    if game_over:
        play_again_button_rect = screen.blit(play_again_button, (WIDTH // 2 - play_again_button.get_width() // 2, HEIGHT // 2))

    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    clock.tick(60)

# Add this line to pause the program before it exits
input("Press Enter to exit the game")

pygame.quit()
sys.exit()
