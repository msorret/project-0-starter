class Scene:
    def __init__(self, description, character, item):
        self.description = description
        self.character = character
        self.item = item
        
    
    def enter(self, player):
        print(self.description)
        print("You see a", self.character.description)
        print("You see a", self.item.name)
        choice = input("Do you want to move toward the characters or the item or leave the scene? (C/I/L): ")
        if choice == "C":
            while choice != "L":
                choice = input("Do you want to talk or leave? (T/L): ")
                if choice == "T":
                    print("You said: Hello!")
                    self.character.talk_to_player("Hello!")
                    choice = input("Ask the character what he is looking for? (Y/N)")
                    if choice == "Y":
                        self.character.ask_for_item()
                        choice = input("Do you have what {self.character.name} is looking for? (Y/N)")
                        if choice == "Y":
                            print("You said: I have that item.")
                            self.character.talk_to_player("I have that item.")
                            choice = input("Do you want to give your item to the character? (Y/N)")
                            if choice == "Y":
                                player.give_item(self.item, self.character)
                                print("You said: Here you go!")
                                self.character.talk_to_player("Here you go!")
                            else:
                                print("You said: I have it but I can't give it to you. Sorry.")
                                self.character.talk_to_player("I have it but I can't give it to you. Sorry")
                        else:
                            print("You said: I don't have that sorry!")
                            self.character.talk_to_player("I don't have that sorry!")
                    elif choice == "N":
                        print("You said: Goodbye")
                        self.character.talk_to_player("Goodbye")
                elif choice == "L":
                    print("You leave the room.")
                    self.enter(player)
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "I":
            choice = input("Do you want to pick it up or examine it? P/E")
            if choice == "P":
                print("You picked up a ", self.item.name)
                player.pick_up_item(self.item)
                self.enter(player)
            elif choice == "E":
                print("You found a {self.item.name} {self.item.description}")
                choice = input("Do you want to pick it up now? Y/N")
                if choice == "Y":
                    print("You picked up a ", self.item.name)
                    player.pick_up_item(self.item)
                    self.enter(player)
                else:
                    print("You leave the item.")
                    self.enter(player)
        elif choice == "L":
            print("You leave the room.")
        else:
            print("Invalid choice. Please try again.")
            self.enter(player)
