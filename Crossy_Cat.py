import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_TITLE = "Crossy Cat"
WHITE_BACKGROUNG = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60
is_gameover = False

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_BACKGROUNG)
pygame.display.set_caption(GAME_TITLE)

# Main game loop
while not is_gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: is_gameover = True
    print(event)  # Console event logger (Can be deleted)

    pygame.display.update()  # Update all game graphics
    clock.tick(FPS)  # Updates everything within the game

# Quit pygame and the program
pygame.quit()
quit()