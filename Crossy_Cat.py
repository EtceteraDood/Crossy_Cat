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

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_BACKGROUNG)
        pygame.display.set_caption(title)

    def run_game(self):
        is_gameover = False
        direction = 0

        player_character = PlayerCharacter('Assets\Black Cat.png', 275, 500, 50, 50)
        enemy_00 = EnemyCharacter('Assets\Spike Ball.png', 20, 300, 50, 50)

        # Main game loop
        while not is_gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: is_gameover = True
                elif event.type == pygame.KEYDOWN:  # Detect when a key is pressed down
                    if event.key == pygame.K_UP: direction = 1
                    elif event.key == pygame.K_DOWN: direction = -1
                elif event.type == pygame.KEYUP:  # Detect when a key is released
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN: direction = 0
                print(event)  # Console event logger (Can be deleted)

            # Redraw the screen to be a blank window
            self.game_screen.fill(WHITE_BACKGROUNG)
            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)
            # Move and draw the enemy character(s)
            enemy_00.move(self.width)
            enemy_00.draw(self.game_screen)

            pygame.display.update()  # Update all game graphics
            clock.tick(self.FPS)  # Updates everything within the game

class GameObjects:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))  #Scale the image up
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObjects):
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0: self.y_pos -= self.SPEED  # UP
        elif direction < 0: self.y_pos += self.SPEED  # DOWN

        if self.y_pos >= max_height - 20: self.y_pos = max_height - 20  # Bottom bounds

class EnemyCharacter(GameObjects):
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20: self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width -20: self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game(GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game()

# Quit pygame and the program
pygame.quit()
quit()