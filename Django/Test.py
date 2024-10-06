# write a code to make a white screen
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Pre test Alpha")

# Set the background color to white
background_color = (255, 255, 255)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the window with the background color
    window.fill(background_color)

    # Update the display
    pygame.display.update()