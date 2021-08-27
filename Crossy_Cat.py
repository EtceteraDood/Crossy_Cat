import pygame

GAME_TITLE = "Crossy Cat"
# Adjusted size 800x800 standard
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE_BACKGROUNG = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    FPS = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_BACKGROUNG)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game(self, level):
        is_gameover = False
        winner = False
        direction = 0

        player_character = PlayerCharacter('Assets\Black Cat.png', 275, 500, 50, 50)

        enemy_00 = EnemyCharacter('Assets\Spike Ball.png', 20, 425, 50, 50)
        enemy_00.SPEED *= level
        enemy_01 = EnemyCharacter('Assets\Spike Ball.png', self.width - 40, 350, 50, 50)
        enemy_01.SPEED *= level
        enemy_02 = EnemyCharacter('Assets\Spike Ball.png', 20, 275, 50, 50)
        enemy_02.SPEED *= level
        enemy_03 = EnemyCharacter('Assets\Spike Ball.png', self.width - 40, 160, 50, 50)
        enemy_03.SPEED *= level
        enemy_04 = EnemyCharacter('Assets\Spike Ball.png', 20, 110, 50, 50)  # Goal Protector
        enemy_04.SPEED *= level

        pizza = GameObjects('Assets\Pizza.gif', 275, 25, 50, 50)
        enemies = [enemy_00, enemy_01, enemy_02, enemy_03, enemy_04]

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
            # Draw the background image
            self.game_screen.blit(self.image, (0, 0))
            # Draw the forbidden pizza
            pizza.draw(self.game_screen)
            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)
            # Move and draw the enemy character(s)
            enemy_00.move(self.width)
            enemy_00.draw(self.game_screen)
            # Add more enemies as you progress farther in the game
            if level > 1.5:
                enemy_02.move(self.width)
                enemy_02.draw(self.game_screen)
            if level > 2:
                enemy_04.move(self.width)
                enemy_04.draw(self.game_screen)
            if level > 2.5:
                enemy_01.move(self.width)
                enemy_01.draw(self.game_screen)
            if level > 3:
                enemy_03.move(self.width)
                enemy_03.draw(self.game_screen)

            # Game winning and losing conditions
            for enemy in enemies:
                if player_character.collision_detection(enemy):
                    is_gameover = True
                    winner = False
                    text = font.render('Game Over', True, BLACK_COLOR)
                    self.game_screen.blit(text, (180, 270))
                    pygame.display.update()
                    clock.tick(1)
                    break
            
            if player_character.collision_detection(pizza):
                is_gameover = True
                winner = True

            pygame.display.update()  # Update all game graphics
            clock.tick(self.FPS)  # Updates everything within the game

        # Restart the game if you win otherwise exit the game loop and game
        if winner: self.run_game(level + .1)
        else: return

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

    def collision_detection(self, other_object):
        if self.y_pos > other_object.y_pos + other_object.height: return False
        elif self.y_pos + self.height < other_object.y_pos: return False

        if self.x_pos > other_object.x_pos + other_object.width: return False
        elif self.x_pos + self.width < other_object.x_pos: return False
        return True

class EnemyCharacter(GameObjects):
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20: self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width -20: self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('Assets\Background.png', GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game(1)

# Quit pygame and the program
pygame.quit()
quit()