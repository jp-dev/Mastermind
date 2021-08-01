# mastermind.py
# Version 0.3

import pygame
from pygame.locals import *
from random import choice
from collections import Counter
import os
import sys
from asciiart import *

# Initialize the available colors of pegs for the game
# (R)ed, (B)lue, (G)reen, (Y)ellow, (W)hite, blac(K)
CODE_PEGS = [
    'R', # Red
    'B', # Blue
    'G', # Green
    'Y', # Yellow
    'W', # White
    'K'  # Black
]

CODE_EMOJI = {
    'R': '\U0001f534', 
    'B': '\U0001f535', 
    'G': '\U0001f7e2', 
    'Y': '\U0001f7e1', 
    'W': '\U000026aa', 
    'K': '\U000026ab'
}


""" --------------------- INITIALIZE ------------------------ """
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init() # Initialize pygame
clock = pygame.time.Clock()

""" ------------------------- LABELS ------------------------------ """
font = pygame.font.SysFont(None, 24)

""" ----------------------- BACKGROUND ---------------------------- """
bg = pygame.image.load(os.path.join("images", "mastermindsplash.png"))
bg_width = bg.get_width()
bg_height = bg.get_height()
# r_width = xxxx / bg_width
# r_height =  xxxx / bg_height
# ratio = r_width if r_width < r_height else r_height
# screen = pygame.display.set_mode((int(bg_width*ratio), int(bg_height*ratio)))
screen = pygame.display.set_mode((bg_width,bg_height))
# bg = pygame.transform.scale(bg, (int(bg_width*ratio), int(bg_height*ratio)))
# # bg = pygame.image.load(os.path.join("images", "gameboard.png")).convert()
pygame.display.set_caption("MASTERMIND 2021")


""" ------------------------ SOUND FX ------------------------------ """
# sound_keypress = pygame.mixer.Sound(os.path.join("audio", "fx-keypress.ogg"))
# sound_keypress.set_volume(0.5)
sound_wrong = pygame.mixer.Sound(os.path.join("audio", "wrong.wav"))
sound_wrong.set_volume(0.5)
sound_invalid = pygame.mixer.Sound(os.path.join("audio", "invalid.wav"))
sound_invalid.set_volume(0.5)
sound_welcome = pygame.mixer.Sound(os.path.join("audio", "welcome.ogg"))
sound_welcome.set_volume(0.5)
sound_welcomeback = pygame.mixer.Sound(os.path.join("audio", "welcomeback.ogg"))
sound_welcomeback.set_volume(0.5)
sound_humiliation = pygame.mixer.Sound(os.path.join("audio", "humiliation.ogg"))
sound_humiliation.set_volume(0.5)

# print(f"Width: {bg_width}  Height: {bg_height}")

def make_code():
    """ 
    Creates new secret code and a counter dictionary
    """
    code = []
    for _ in range(4):
        code.append(choice(CODE_PEGS))
    code_counter = Counter(code)
    return code, code_counter


if __name__ == "__main__":

    # key_index = 0

    # Greeting
    print(title_mastermind)
    print("Welcome to Mastermind! Try to break the secret 4-color code!\n")
    sound_welcome.play()
    pygame.mixer.music.set_volume(0.5)


    # Initialize number of attempts to 10 as per original Mastermind game rules
    attempts = 10

    # Create secret code and count the occurrence of each color by calling the make_code() function
    secret_code, secret_counter = make_code()
    # print(secret_code, secret_counter)

    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     keys = pygame.key.get_pressed()
            #     if pygame.key.get_pressed()[K_ESCAPE]:
            #         sys.exit()
            #     if keys[K_r]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)
            #     if keys[K_g]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)
            #     if keys[K_b]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)
            #     if keys[K_y]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)
            #     if keys[K_w]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)
            #     if keys[K_k]:
            #         print(f"{key_index}: You pressed {event.key:c}")
            #         sound_keypress.play()
            #         pygame.mixer.music.set_volume(0.05)

        pygame.display.update()


        # Start the game
        while attempts > 0:
            # Initialize 'valid_guess' to True
            valid_guess = True

            # Initialized the hint pins list
            pins = []
            
            # Display the remaining attempts
            print(f"Attempts remaining: {attempts}")
            
            # Prompt user for a guess and store in the variable 'guess'
            guess = list(input("Your guess? (R,G,B,Y,W,K) > "))

            # Convert each char in 'guess' to upper case
            guess = [color.upper() for color in guess]
            # print(f"{guess} is of type {type(guess)}") NOTE: For troubleshooting

            # First, confirm that player entered 4 chars
            if len(guess) == 4:
                # Check if player already has correct guess
                if guess == secret_code:
                    print(title_welldone)
                    print("Congratulations, Mastermind! You broke the secret code!")
                    print(" ".join(CODE_EMOJI[peg] for peg in secret_code))
                    # Play hero music!
                    pygame.mixer.music.load(os.path.join("audio", "maintheme.ogg"))
                    pygame.mixer.music.set_volume(0.10)
                    pygame.mixer.music.play(-1)

                    play_again = input("Play again? (y/n) > ")
                    if play_again == 'y':
                        # Shut off the music
                        pygame.mixer.music.fadeout(500)
                        # Reset the 'attempts' counter
                        attempts = 10
                        # Create a new 'secret_code'
                        secret_code, secret_counter = make_code()
                        # print(secret_code)
                        # print(secret_code, secret_counter) NOTE: For troubleshooting
                        sound_welcomeback.play()
                        pygame.mixer.music.set_volume(0.50)
                        print(title_dopamine)
                        print("Your \U0001f9e0  is getting stronger!")

                        print("\n")
                    else:
                        print("Thanks for playing! Bye!\n")
                        attempts = 0
                        sys.exit()

                # If guess not completely correct, start peg comparison
                else:
                    # Check to make sure all colors in 'guess' are valid
                    valid_guess = all(color in CODE_PEGS for color in guess)
                    # print(valid_guess)

                    if valid_guess == True:
                        # Get the count for each color in player's guess
                        guess_count = Counter(guess)
                        # print(guess_count) NOTE: For troubleshooting

                        # First, get all color matches between 'secret_code' and 'guess' and store in 'light_pins'
                        light_pins = sum(min(secret_counter[k], guess_count[k]) for k in secret_counter)
                        
                        # Next, confirm all EXACT matches and store in 'dark_pins'
                        dark_pins = sum(a == b for a, b in zip(secret_code, guess))

                        # Update the light_pins by subtracting dark_pins
                        light_pins -= dark_pins

                        # Update the pins list with the number of dark and/or light pins
                        for _ in range(dark_pins):
                            pins.append('\U000025fe')                
                        for _ in range(light_pins):
                            pins.append('\U000025fd')

                        # Display player guess with emoji
                        print(" ".join(CODE_EMOJI[peg] for peg in guess), "\n")
                        # Display the result of their guess with the pins list
                        print(" ".join(pins), "\n")

                        sound_wrong.play()

                        # After each valid attempt, decrement the 'attempts' counter by 1
                        attempts -= 1
                    else:
                        # Play entered an invalid char
                        sound_invalid.play()
                        print("Your guess is invalid. Try again.\n")
            else:
                # Player didn't enter the correct number of chars.
                valid_guess = False
                sound_invalid.play()
                print("You must enter up to 4 colors. Try again.\n")

        print(title_humiliation)
        print("Sorry, you used up all your chances...")
        sound_humiliation.play()
        pygame.mixer.music.set_volume(0.05)
        print(f"The secret code was: ", " ".join(CODE_EMOJI[peg] for peg in secret_code))
        play_again = input("Play again? (y/n) > ")
        if play_again == 'y':
            # Shut off the music
            # pygame.mixer.music.fadeout(500)
            print(title_dopamine)
            # print("Your \U0001f9e0 is getting stronger!")
            print("Back for another challenge! All your \U0001f9e0  are belong to US!")
            # Reset the 'attempts' counter
            attempts = 10
            # Create a new 'secret_code'
            secret_code, secret_counter = make_code()
            # print(secret_code)
            # print(secret_code, secret_counter) NOTE: For troubleshooting
            sound_welcomeback.play()
            pygame.mixer.music.set_volume(0.05)

            print("\n")
        else:
            print("Thanks for playing! Bye!\n")
            attempts = 0
            sys.exit()



