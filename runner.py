from character import Character
from item import Item
from player import Player
from scene import Scene
from wordle import playWordle

print("Welcome to Ms. Orret's game!")
player_name = input("What is your name?")
player = Player(player_name)
fairy = Character("Tinkerbell", "A small fairy dressed in green and sparkling with fairy dust", [], {"Hello!": "Hello! My name is Tink! It is nice to meet you but I can't stay long. I am very busy looking for something", "I have that item.": "You do? Great! Can I have it?","Here you go!": "Thank you so so much!", "I have it but I can't give it to you. Sorry": "Boo! I'll keep looking then. Goodbye!", "Goodbye": "Bye!", "I don't have that sorry!": "It's okay I'll keep looking - bye!"}, "a Book")
book = Item("Book", "A book about fairy tales", 10)
scene1 = Scene("You entered a dark forest.", fairy, book)
owl = Character("Mr. Owl", "A gray owl with glasses", [], {"Hello!": "Hello! My name is Mr. Owl It is nice to meet you but I can't stay long. I am very busy looking for something", "I have that item.": "You do? Great! Can I have it?","Here you go!": "Thank you so so much!", "I have it but I can't give it to you. Sorry": "Boo! I'll keep looking then. Goodbye!", "Goodbye": "Bye!", "I don't have that sorry!": "It's okay I'll keep looking - bye!"}, "a Book")
lollipop = Item("Lollipop", "A cherry tootsie roll pop", 10)
scene2 = Scene("You entered a cave", owl, lollipop)


choice = 0
while choice != "E":
    print("You are in a fork in the road. You can either go into the forest or into a cave. ")
    choice = input("Which way do you go? (F/C/) Enter E to exit the game.")
    if choice == "F":
        scene1.enter(player)
    elif choice == "C":
        print("To enter the cave, you must solve a word puzzle.")
        win = playWordle("FUNKY")
        if win == True:
            print("You entered the cave.")
            scene2.enter(player)
        else:
            print("You failed the word puzzle.")
    else:
        print("Invalid choice. Please enter F, C, or E.")

print("Thanks for playing!")
    

