#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To improve clarity and simplicity of the code, AI was partially used as a tool for assistance.

# ------------------------------------------------------------------------------------------------------------------------------------

MAX_BAG_SIZE = 5
bag = [{"name": "Laptop", "type": "tool", "description": "Your school laptop. Not very helpful for sports."}]

rooms = {
    "Gym": [
        {"name": "Light Switch", "type": "tool", "description": "Helps you see the room more clearly."},
        {"name": "Rice Cakes", "type": "food", "description": "Gives you some energy."},
        {"name": "Jersey", "type": "clothing", "description": "Team jersey to identify players."},
        {"name": "Basketball", "type": "ball", "description": "A basketball, essential for training."}
    ],
    "Locker Room": [
        {"name": "Shorts", "type": "clothing", "description": "Shorts for playing sports indoors."},
        {"name": "Water Bottle", "type": "drink", "description": "Water bottle to stay hydrated."},
        {"name": "Shampoo", "type": "care", "description": "Shampoo for after your workout."},
    ],
    "Equipment Room": [
        {"name": "Key", "type": "tool", "description": "Used to unlock the basket lowering mechanism."},
    ],
    "Basket Control": []
}

current_room = "Gym"
basket_switch_found = False

# ----------------- Function definitions -------------------

def show_bag():
    if not bag:
        print("Your bag is empty.")
    else:
        print("Bag:")
        for item in bag:
            print(f"- {item['name']}")

def show_room_items():
    print(f"Items in the room ({current_room}):")
    if not rooms[current_room]:
        print("No items here.")
    else:
        for item in rooms[current_room]:
            print(f"- {item['name']}")

def pick_up(item_name):
    global bag
    for item in rooms[current_room]:
        if item["name"].lower() == item_name:
            if len(bag) >= MAX_BAG_SIZE:
                print("Your bag is full. You can't carry more.")
                return
            bag.append(item)
            rooms[current_room].remove(item)
            print(f"You picked up the {item_name}.")
            return
    print(f"{item_name} is not in the room.")

def drop(item_name):
    for item in bag:
        if item["name"].lower() == item_name:
            bag.remove(item)
            rooms[current_room].append(item)
            print(f"You dropped the {item_name}.")
            return
    print(f"{item_name} is not in your bag.")

def use(item_name):
    global current_room, basket_switch_found

    for item in bag:
        if item["name"].lower() == item_name:
            if item["type"] == "food":
                print(f"You eat the {item_name}. Tasty!")
                bag.remove(item)
            elif item["type"] == "drink":
                print(f"You drink the {item_name}. Refreshing!")
                bag.remove(item)
            elif item["name"].lower() == "light switch":
                if not basket_switch_found:
                    basket_switch_found = True
                    print("You flip the light switch and discover the basket control room!")
                    rooms["Basket Control"] = [
                        {"name": "Control Panel", "type": "opportunity", "description": "A panel to lower the basketball hoops."}
                    ]
                else:
                    print("The basket control room is already discovered.")
            elif item["name"].lower() == "key" and current_room == "Basket Control":
                print("You use the key. The hoops are lowered... Time to start your training!")
                exit()
            else:
                print(f"You try to use the {item_name}, but nothing happens. Something is missing")
            return
    print(f"{item_name} is not in your bag.")

def examine(item_name):
    for item in bag + rooms[current_room]:
        if item["name"].lower() == item_name:
            print(f"{item['name']}: {item.get('description', 'No description available.')}")
            return
    print(f"{item_name} is not in the room or your bag.")

def change_room(new_room):
    global current_room
    if new_room not in rooms:
        print("That room doesn't exist.")
    elif new_room == "Basket Control" and not basket_switch_found:
        print("You don't know how to get there yet.")
    else:
        current_room = new_room
        print(f"You enter the room: {current_room}")

# --------------------- Game-loop (Main) function -----------------------

def game_loop():
    print("Welcome! You find yourself in the school gym, not during regular class.")
    print("You feel like playing basketball, but the hoops are still up and you only have your school laptop with you.")
    print("Your goal is to explore the rooms, find useful items, and prepare the gym for basketball.")
    print("Try 'help' to see available commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: bag, look, pickup [item], drop [item], use [item], examine [item], goto [room], quit")
            print("Rooms: Gym, Locker Room, Equipment Room, Basket Control (only available once discovered)")
        elif command == "bag":
            show_bag()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:].strip()
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:].strip()
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:].strip()
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:].strip()
            examine(item_name)
        elif command.startswith("goto "):
            room_name = command[5:].title()
            change_room(room_name)
        elif command == "quit":
            print("You leave the gym. See you next time!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

if __name__ == "__main__":
    game_loop()

