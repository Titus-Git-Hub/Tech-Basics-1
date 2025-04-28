#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install rich # For bold text


# In[ ]:


# To improve clarity and simplicity of the code, AI was partially used as a tool for assistance.

import random # For randomness
import time # For time delays
from rich import print # For bold text

# Introduction
print("Welcome to 'Football Player ASCII Creation Simulator ⚽️'!")
time.sleep(1)
print("Let's get started!")
time.sleep(1)

# Personal inputs
name = input("Enter a name for your player: ")
club = input("Enter the name of the club your player should play for: ")
time.sleep(1.5)

# Predefined numbers and famous players
possible_numbers = [6, 7, 9]
number6 = ["Joshua Kimmich", "Xavi", "Paul Pogba"]
number7 = ["Cristiano Ronaldo", "David Beckham", "Franck Ribery"]
number9 = ["Zlatan Ibrahimovic", "Robert Lewandowski", "Gerd Müller"]
possible_number_add = [1, 2, 3, 4, 5, 8]

# Displaying the options
print("\nAvailable Jersey Numbers:")
for num in possible_numbers:
    print(num)
time.sleep(2)

# Choose a number or "add"
while True:
    choice = input("\nPick one of the given numbers (6, 7, 9) that interests you the most or type 'add' to add a new number: ").lower()
    
    if choice in ["6", "7", "9"]:
        picked_number = int(choice)
        if picked_number == 6:
            time.sleep(0.5)
            print(f"Great idea! None other than superstar {random.choice(number6)} has worn this number before you.")
        elif picked_number == 7:
            time.sleep(0.5)
            print(f"Great idea! None other than superstar {random.choice(number7)} has worn this number before you.")
        elif picked_number == 9:
            time.sleep(0.5)
            print(f"Great idea! None other than superstar {random.choice(number9)} has worn this number before you.")
        break
    
    elif choice == "add":
        number_add = input("Which single-digit number do you want to add (1-5, 8)? ")
        try:
            number_add = int(number_add)
            if number_add in possible_number_add:
                possible_numbers.append(number_add)
                print(f"Number {number_add} has been added!")
                picked_number = number_add  
                break
            else:
                print("Invalid input. Only single-digit numbers (1-5,8) are allowed.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    else:
        print("Invalid choice. Please pick 6, 7, 9 or type 'add'.")

# Final selection of the jersey number
time.sleep(2)
while True:
    try:
        number = int(input("\nNow enter the final jersey number of your player (you can choose from all the given numbers or any that you’ve added): "))
        if number in possible_numbers:
            time.sleep(0.5)
            print("Alright! This will be your final jersey number.")
            time.sleep(2)
            break
        else:
            print("This number is not possible. Please pick correctly.")
    except ValueError:
        print("Your jersey number cannot be a text. Please enter a number.")

# Body length settings
leg_length = input("\nHow long should the legs of your player be? (Short/Medium/Long): ").lower()

def draw_ascii(number, leg_length):
    print("          ///////                           ")
    print("         ---------                          ")
    print("         |(x) (x)|                          ")
    print("         |   >   |                          ")
    print("         |  -o-  |                          ")
    print("         ---------                          ")
    print(f"   o=====|   [bold]{number}[/bold]   |=====o                    ")
    print("         |   -   |                          ")
    print("         |e-sport|                          ")
    print("         ---------                          ")

    if leg_length == "short":
        print("         |       |")
        print("         |       |")
    elif leg_length == "medium":
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
    elif leg_length == "long":
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
    else:
        print("Invalid leg length. Drawing medium by default.")
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
    
    print("       <=|       |=>   (=)                  ")

# First drawing
time.sleep(1)
draw_ascii(number, leg_length)
time.sleep(1)

# Option to make changes
while True:
    final_change = input("Are you happy with your decision? (yes/no): ").lower()
    if final_change == "yes":
        break
    elif final_change == "no":
        time.sleep(1)
        print("Then here you have the chance to update your ASCII art!")
        time.sleep(1)
        leg_length = input("Re-enter leg length (Short/Medium/Long): ").lower()
        time.sleep(1)
        draw_ascii(number, leg_length)
        time.sleep(1)
    else:
        print("Please type 'yes' or 'no'.")

print("Perfect🥳")     
        
# Presentation of the created ASCII art
time.sleep(2)
print("\nAre you ready?!")
time.sleep(2)
print("Drum cheer🥁...")
time.sleep(1)
print("⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤")
time.sleep(1)
print("Here comes your custom ASCII art football player!🎨")
time.sleep(2)
print(f"\nFrom {club.upper()}")
time.sleep(2)
print(f"With the jersey number {number}")
time.sleep(2)
print("\nHere is...")
time.sleep(2)
print(f"🎉[bold]{name.upper()}[/bold]🎉\n")
time.sleep(1)

# Final ASCII art display
print("                         ******************     ")
print(f"                          Name = [bold]{name.upper()}[/bold]     ")
print(f"                          Club = [bold]{club.upper()}[/bold]     ")
print("          ///////        ******************     ")
print("         ---------                          ")
print("         |[bold](x)[/bold] [bold](x)[/bold]|                          ")
print("         |   [bold]>[/bold]   |                          ")
print("         |  [bold]-o-[/bold]  |                          ")
print("         ---------                          ")
print(f"   [bold]o=====[/bold]|   [bold]{number}[/bold]   |[bold]=====o[/bold]                    ")
print("         |   -   |                          ")
print("         |e-sport|                          ")
print("         ---------                          ")

if leg_length == "short":
    print("         |       |")
    print("         |       |")
elif leg_length == "medium":
    print("         |       |")
    print("         |       |")
    print("         |       |")
    print("         |       |")
elif leg_length == "long":
    print("         |       |")
    print("         |       |")
    print("         |       |")
    print("         |       |")
    print("         |       |")
    print("         |       |")
else:
    print("         |       |")
    print("         |       |")
    print("         |       |")
    print("         |       |")

print("       [bold]<=[/bold]|       |[bold]=>[/bold]   (=)                 ")
print(" ______________________________            ")

