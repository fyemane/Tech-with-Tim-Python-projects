#https://www.youtube.com/watch?v=5JuslgfVoFY&list=PLlEgNdBJEO-keECn0rTUTM7Be7PWUr2F-&index=4
#@TokyoEdTech
import os
# one approach
"""
print("My Space Adventure")
room = "closet"

while True:
    if room == "closet":
        print("The Closet")
        print("You are in a small nondescript closet with a shelf.")
        print("You can see a uniform.")
        print("What would you like to do?")
        choice = input()

        if choice == "get uniform":
            print("You take the uniform")
        elif choice == "go north":
            print("You go north.")
            room = "control room"

    if room == "control room":
        print("The Control Room")
        print("You are in a small room that looks like it controls something. There is a guard here.")
        print("You can see an id.")
        print("What would you like to do?")
        choice = input()

        if choice == "kill guard":
            print("You attack the guard and he kills you.")
            quit()
        elif choice == "go south":
            print("You go south.")
            room = "closet"
"""

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# create items
# closet items
shelf = Item("shelf", "The shelf is empty.", False)
uniform = Item("uniform", "The uniform is blue and drab.", True)
# control room items
guard = Item("guard", "The guard looks mean and menacing.", False)
electronic_lock = Item("lock", "The lock is in front of a large door to the east.", False)
id = Item("id", "The id is silver with a barcode on it.", True)
spacesuit = Item("spacesuit", "The spacesuit looks old, but safe.", True)
button = Item("button", "The button has a big red warning symbol on it.", False)

# create rooms
# closet
closet = Room("The Closet", 
              "You are in a small nondescript closet with a shelf.")
closet.items.append(shelf)
closet.items.append(uniform)
# control room
control_room = Room("The Control Room", 
                    "You are in a small room that looks like it controls something. " 
                    "There is a guard here. There is an airlock to the east.")
control_room.items.append(guard)
control_room.items.append(electronic_lock)
control_room.items.append(id)
# arilock 
airlock = Room("The Airlock",
               "You are in a small room that is clearly an airlock. "
               "There is window to space in the east.")
airlock.items.append(spacesuit)
airlock.items.append(button)

# create exits
closet.exits["n"] = control_room
control_room.exits["s"] = closet
airlock.exits["w"] = control_room

#  Start game
print("Welcome to My Space Adventure")
print("You wake up on a space station.")
player = Player("The Player", closet)

while True:
    print("")
    print("----------------------------------------------------------")
    print(player.location.name)
    print(player.location.description)
    print("Here are the exits: ")
    for exit in player.location.exits:
        print("- {}".format(exit))
    print("You see the following: ")
    for item in player.location.items:
        print("- {}".format(item.name))

    # get command
    print("\nWhat would you like to do?")
    command = input("> ")
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]

    # Examine
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    # Get
    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # check if movable
                if item.is_movable:
                    print("You take the {}.".format(item.name))
                    # remove from room
                    player.location.items.remove(item)
                    # add to player's inventory
                    player.inventory.append(item)
                else:
                    print("Sorry you can't move that.")

    # drop
    if verb == "drop":
        for item in player.inventory:
            if item.name == noun:
                print("You dropped the {}.".format(item.name))
                # remove the item's inventory
                player.inventory.remove(item)
                # add to location
                player.location.items.append(item)

    # check inventory
    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print("- {}".format(item.name))

    # movement
    if verb in ["n", "s", "e", "w", "u", "d"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("You go {} and find yourself in a new room.".format(verb))

    # room specific code
    # Control room
    if player.location == control_room:
        if uniform not in player.inventory:
            print("The guard sees you. Without saying a word, he pulls his laser gun and kills you. "
                  "Game Over.")
            os._exit(0)
        else:
            print("The guard looks up, looks at the uniform, and turns his head back to the display.")

        if verb == "open" and noun == "airlock":
            if id in player.inventory:
                print("You swipe the id and the airlock opens.")
                control_room.exits["e"] = airlock
            else:
                print("The airlock won't open. "
                      "You must need some id to enter.")

    # airlock
    if player.location == airlock:
        if "w" in airlock.exits:
            del(airlock.exits["w"])
            print("The airlock door closes! "
                  "You are trapped. "
                  "There is no lock on this side.")

        if verb == "press" and noun == "button":
            if spacesuit in player.inventory:
                print("You put on the spacesuit are push the red button. "
                      "The outer airlock door opens.")
            else:
                print("The outer airlock door opens. "
                      "You are sucked into the vaccuum of space and die.")
                os._exit(0)
