import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class character :
    speed = 15
    points = 0
    strenght = 20
    stamina = 15


    def __init__(self) :
        print("De Character zijn constructor")

    def walk(self) :
        print("Character loopt met een snelheid", self.speed)

class Mario1 (character) :

    lives = 2
    item = None

    def __init__(self) :
        # We cullen aan op de constructor van de character:
        super().__init__()

        # Snelheid van Mario1 is hoger dan Standaar:
        self.speed = 35


        # De "Walk" funciotnaliteit van de Character ga ik OVERSCHRIJVEN
        def walk(self) :
            print("Mario1 loopt sneller dan normaal waardoor hij apart loopt", self.speed)
        
    def jump(self) :
        print("Mario1 kan springen")

class Mario :

    _coins = 1
    lives = 3

    def __init__(self, lives):
        self.lives = levens


print("Mario.lives: ", Mario.lives)

Mario5 = Mario
Mario5.lives = 500

print("Mario5.lives", Mario5.lives)

# Instanties maken:
CharacterA = character
MarioX = Mario1

CharacterA.walk
MarioX.walk
MarioX.jump

print(CharacterA.speed)
print(MarioX.speed)
print(MarioX.lives)

# Het resultaat wordt hier weergeven:
print(MarioX)

playerSprite = pygame.image.load("../Art/spr_Player.png")
playerRect = playerSprite.get_rect()
playerSpeed = 5


while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    if (KEYS_DOWN[K_UP]):
        playerRect.y -= playerSpeed
    elif (KEYS_DOWN[K_DOWN]):
        playerRect.y += playerSpeed

    if (KEYS_DOWN[K_LEFT]):
        playerRect.x -= playerSpeed
    elif (KEYS_DOWN[K_RIGHT]):
        playerRect.x += playerSpeed
    

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG_COLOUR)

    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
