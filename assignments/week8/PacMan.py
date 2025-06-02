# I decided to do this week's task with two images from the well-known game "Pac-Man";
# letting Pac-Man and the ghosts move across the screen.
# To handle this task, AI and the dino-example were used as tools for assistance;
# With the requirement for myself to understand the code.

# libraries for the game
import pygame # for py game animation
import random # for randomness

# adjustment of the background with these constants (colour, width, height and also the number of images added here)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
NUM_CHARACTERS = 10

# to activate the pygame library
pygame.init()

# to create the display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# for the pygame window name
pygame.display.set_caption('image')

# the class for animated image
class AnimatedImage:
    def __init__(self, image_path):
        # load and scale image
        self.image = pygame.image.load(image_path).convert_alpha() # convert_alpha() for png images
        self.image = pygame.transform.scale(self.image, (120, 100)) # size of the image (width, height)

        # random position and speed
        self.x = random.randint(0, SCREEN_WIDTH - 100)   # random position of the images (width)
                                                            # 0 = far left; 100 far right
        self.y = random.randint(0, SCREEN_HEIGHT - 100)  # random position of the images (height)
                                                            # 0 = far on top; 100 far at the bottom
        self.speed = random.randint(1, 5)     # random speed of the images
                                                    # 1 = 1 pixel per frame = slow
                                                    # 5 = 5 pixels per frame = fast

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -100  # method for the position reset of the image after moving outside the screen

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  # method for actually putting the image on the screen;
                                                    # and also at the right position.

image_files = ["PAC-man.png", "pixel_art.png"] # the image files that should be used

characters = [
    AnimatedImage(random.choice(image_files)) for i in range(NUM_CHARACTERS)
]   # The image files defined in the class (4 lines above) are accessed and from these two defined images,
    # random images are selected until the number of images defined in the constants at the beginning is reached.

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.fill(BACKGROUND_COLOR) # paint the screen with background color

    for character in characters:
        character.move()
        character.draw(screen)
        # necessary for the animation and display of each image on the screen.

    pygame.display.flip() # refresh the display

pygame.quit()
exit(0)
