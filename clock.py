import pygame
import time

# Initialize pygame
pygame.init()

# Define screen size and colors
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Load and set the logo
pygame.display.set_caption('Mindful Meal Timer')

# Set timer for eating and pause
time_to_eat = 600
time_to_pause = 120

# Timer and Sound Initialization
current_time = pygame.time.get_ticks()
eating_timer = pygame.time.get_ticks()
pause_timer = pygame.time.get_ticks()

sound_on = True
pause_now = False

# Game Loop
while not pause_now:
    # Check if pause is triggered
    if pygame.time.get_ticks() - pause_timer > time_to_pause * 1000:
        pause_now = True
        pause_timer = pygame.time.get_ticks()

    # Check if sound is toggled
    if sound_on:
        pygame.mixer.music.load('countdown_tick.mp3')
        pygame.mixer.music.play()

    # Draw and update screen
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # Calculate time remaining
    time_remaining = (time_to_eat - (pygame.time.get_ticks() - eating_timer) / 1000) / 60
    print('{:02d}:{:02d}'.format(int(time_remaining // 60), int(time_remaining % 60)))

    # Pause the game for 1 second
    pygame.time.delay(1000)

print('LET\'S STOP I\'M FULL NOW')