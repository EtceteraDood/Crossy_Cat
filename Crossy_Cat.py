import pygame

GAME_TITLE = "Crossy Cat"
# Adjusted size 800x800 standard
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE_BACKGROUNG = (255, 255, 255)
clock = pygame.time.Clock()

class Game:
    FPS = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        game_screen = pygame.display.set_mode((width, height))
        game_screen.fill(WHITE_BACKGROUNG)
        pygame.display.set_caption(title)

    def run_game(self):
        is_gameover = False

        # Main game loop
        while not is_gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: is_gameover = True
            print(event)  # Console event logger (Can be deleted)

            pygame.display.update()  # Update all game graphics
            clock.tick(self.FPS)  # Updates everything within the game

pygame.init()

new_game = Game(GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game()

# Quit pygame and the program
pygame.quit()
quit()