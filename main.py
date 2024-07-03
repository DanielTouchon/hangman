from login import login_loop
from game import game_loop


def main():
    print("Welcome to Hangman.")
    print(" -------- ")

    login_loop()
    game_loop()

main()