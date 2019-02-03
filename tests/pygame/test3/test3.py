#!/usr/bin/python3
#fastmind
#by boot1110001

### IMPORTS ####################################################################
import sys
import pygame

### NON EDITABLE VARIABLES #####################################################
window = 0 # glut window number
lvlist = [] # level file list
wmap = [] # wall list
womap = [] # wall object list
goal = 0 # goal object
player = 0 # player object
victory = False
old_time = 0
lvl_time = 0

### EDITABLE VARIABLES #########################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

stdsize=15 # test with 10
stdR, stdG, stdB=Color.BLUE2

### FUNCTIONS ##################################################################


### MAIN #######################################################################
def main(argv):
    pygame.init()

    # Set the height and width of the screen
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Bouncing Rectangle")
    logo = pygame.image.load('fastmind.png')
    pygame.display.set_icon(logo)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50

    # Speed and direction of rectangle
    rect_change_x = 2
    rect_change_y = 2

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Logic
        # Move the rectangle starting point
        rect_x += rect_change_x
        rect_y += rect_change_y

        # Bounce the ball if needed
        if rect_y > 450 or rect_y < 0:
            rect_change_y = rect_change_y * -1
        if rect_x > 650 or rect_x < 0:
            rect_change_x = rect_change_x * -1

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)

        # Draw the rectangle
        pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
        pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
