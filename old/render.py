# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("black")
            pos = pygame.mouse.get_pos()
            print(pos)
            print(pos[0], pos[1])
            pygame.draw.circle(screen, "red", pygame.Vector2(pos[0], pos[1]), 20)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
