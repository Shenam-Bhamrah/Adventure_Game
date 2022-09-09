import time
import random


# funtion that will cause a 2-second delay after the first print() statement.
def print_pause(message):
    print(message)
    time.sleep(2)


# function that makes sure that the user gives a valid input each time.
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if response.lower() == option1:
            break
        elif response.lower() == option2:
            break
    return response


# function that displays introductory lines whenev the games starts/restarts.
def intro(creatures):
    creature = random.choice(creatures)
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")
    return creature


# function that  decribes the things that happen when the player fights.
def fight(creature, weapon):
    print_pause(f"As the {creature} moves to attack,"
                f"you unsheath your {weapon}.")
    if weapon == "dagger":
        print_pause(f"You do your best but your {weapon} "
                    f"is no match for the {creature}.")
        print_pause("You have been defeated!")
    else:
        print_pause(f"The {weapon} shines brightly in your hand \n"
                    "as you brace yourself for the attack.\n"
                    f"But the {creature} takes one look at your \n"
                    "shiny new toy and runs away!\n"
                    f"You have rid the town of the {creature}.\n"
                    "You are victorious!\n")
    restart()


# function that asks player the opton to continue or restart.
def restart():
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        play_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")


# function that decribes the things that happen to the player goes in the cave.
def cave(creature, weapon):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    if weapon == "dagger":
        weapon = "Sword of Ogoroth"
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {weapon}")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
    elif weapon == "Sword of Ogoroth":
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now")
    print_pause("You walk back out to the field.\n")
    choice(creature, weapon)


# function that decribes the things that happen in the field.
def field(creature, weapon):
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n")
    choice(creature, weapon)


# function that decribes the things that happen in the house.
def house(creature, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")
    if weapon == "dagger":
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    elif weapon == "Sword of Ogoroth":
        print_pause(" ")
    response = valid_input("Would you like to (1) fight "
                           "or (2) run away?\n", "1", "2")
    if response == "1":
        fight(creature, weapon)
    elif response == "2":
        field(creature, weapon)


# funtion that allows the user to make choices.
def choice(creature, weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to choose?")
    response = valid_input("(Please enter 1 or 2):\n", "1", "2")
    if response == "1":
        house(creature, weapon)
    elif response == "2":
        cave(creature, weapon)


# funtion that allows player to play game.
def play_game():
    creatures = ["wicked Fairie", "pirate", "troll", "dragon", "gorgon"]
    weapon = "dagger"
    creature = intro(creatures)
    choice(creature, weapon)


play_game()
