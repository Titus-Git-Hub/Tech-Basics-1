#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install rich # For bold text


# In[ ]:


# To improve clarity and simplicity of the code, AI was partially used as a tool for assistance.

from rich import print # For bold text
import time # For time delays

# Initially, four definitions were created using the 'def ()' function in order to access them later via variables and thus make the code more structured and easier to read.


def ask_sleep(): # 'def ()' function number 1
    schlaf = None
    answer = list(range(1,11))
    
    while schlaf not in answer:
        try:
            schlaf = int(input("\nOn a scale from 1-10, how well did you sleep? "))
            time.sleep(0.25)
            if 0 < schlaf <= 4:
                print("That's not so well.")
            elif 4 < schlaf <= 7:
                print("Well, that sounds solid.")
            elif 7 < schlaf <= 10:
                print("That sounds good.")
            else:
                print("And on a scale from 1 to 10.")
        except ValueError:
            time.sleep(0.25)
            print("Come on, I'm really curious—give me a number between 1 and 10")


def ask_math(): # 'def ()' function number 2
    time.sleep(1)
    print("Alright, than here are the questions:")
    time.sleep(2)
    Math_questions = {
        22: "1.QUESTION: What is the result of 7 + 15?",
        4: "2.QUESTION: What is the result of 3 - 3 - (-4)?",
        121: "3.QUESTION: What is the result of 11 x 11?",
        72: "4.QUESTION: What is the result of (-24) - 8 x 12?",
        1: "LAST QUESTION: A prime number can only be divided by itself and which other number?"
    }

    for answer, question in Math_questions.items():
        while True:
            try:
                guess = int(input(f"{question} "))
                if guess == answer:
                    print(f"✅ Correct! The answer was {answer}\n")
                    break
                else:
                    print("❌ Wrong Answer :( Try again!\n")
            except ValueError:
                print("Please enter a valid number.")

        next_question = input("Do you want the next question? (yes/no); IF YOU COMPLETED 5 QUESTIONS OR DON'T WANT TO ENTER / EXIT THE TEST THAN TYPE NO: ").strip().lower()
        if next_question == "no":
            break


def ask_german(): # 'def ()' function number 3
    time.sleep(1)
    print("Alright, than here are the questions:")
    time.sleep(2)
    German_questions = {
        3: "1.QUESTION: How many syllables does the word 'Germany' have?",
        "Berlin": "2.QUESTION: What is the capital of Germany?",
        "Noun": "3.QUESTION: What part of speech does the word 'rabbit'(animal) belong to?",
        "Writing": "4.QUESTION: Every child in school should learn: reading and ...?",
        4: "LAST QUESTION: How many grammatical cases are there in the German language?"
    }

    for answer, question in German_questions.items():
        while True:
            guess = input(f"{question} ").strip()
            if str(guess).lower() == str(answer).lower():
                print(f"✅ Correct! The answer was {answer}\n")
                break
            else:
                print("❌ Wrong Answer :( Try again!\n")

        next_question = input("Do you want the next question? (yes/no); IF YOU COMPLETED 5 QUESTIONS OR DON'T WANT TO ENTER / EXIT THE TEST THAN TYPE NO: ").strip().lower()
        if next_question == "no":
            break


def ask_history(): # 'def ()' function number 4
    print("Alright, than here are the questions:")
    time.sleep(2)
    history_questions = {
        1945: "1.QUESTION: When did the Second World War end (year)?",
        "France": "2.QUESTION: Where did the revolution from 1789 to 1799 take place?",
        1776: "3.QUESTION: In which year was the American Declaration of Independence declared?",
        4: "4.QUESTION: Into how many occupation zones was Germany divided after World War II?",
        2001: "LAST QUESTION: In which year did the 9/11 attack take place?"
    }

    for answer, question in history_questions.items():
        while True:
            guess = input(f"{question} ").strip()
            if str(guess).lower() == str(answer).lower():
                print(f"✅ Correct! The answer was {answer}\n")
                break
            else:
                print("❌ Wrong Answer :( Try again!\n")

        next_question = input("Do you want the next question? (yes/no); IF YOU COMPLETED 5 QUESTIONS OR DON'T WANT TO ENTER / EXIT THE TEST THAN TYPE NO: ").strip().lower()
        if next_question == "no":
            break


# Game start
name = input ("What is your name? ")
print("Thanks! Now enjoy playing the game :)")

time.sleep(2)
print(f"\n🎒[bold] Welcome to your virtual school day {name}! [/bold]\n")
time.sleep(2)

ask_sleep() # 'def ()' function number 1

time.sleep(2)
mood = input("\nDo you feel healthy enough to go to school today? (yes/no): ").strip().lower()

if mood == "yes":
    time.sleep(1)
    print("\nGreat! But I'll tell your teachers to check on you during the day...\n")
    time.sleep(3)
    print("\n📚[bold] Today's schedule: 2h Math, 2h German, 2h History [/bold]")
    time.sleep(2)
    
    print("\n[bold] NEXT UP => MATH CLASS [/bold]")
    time.sleep(2)
    print("Math Teacher: 'I have a test with five questions for you today.'")
    time.sleep(3)
    if input(f"\nI got told that you don't feel so well today, {name}. Do you want to write the math test or rest until the german class? (stay/rest): ").strip().lower() == "stay":
        ask_math() # 'def ()' function number 2
    time.sleep(2)
    
    print("\n[bold] NEXT UP => GERMAN CLASS [/bold]")
    time.sleep(2)
    print("German Teacher: 'Welcome to German class, everyone. I’ve prepared a test for today’s lesson.'")
    time.sleep(3)
    if input(f"\nHow is it going, {name}? Do you want to write the German test or rest until the history class? (stay/rest): ").strip().lower() == "stay":
        ask_german() # 'def ()' function number 3
    time.sleep(2)
    
    print("\n[bold] NEXT UP => HISTORY CLASS [/bold]")
    time.sleep(2)
    print("History Teacher: 'Alright, guys — last subject: History! Let’s end the day with a quick history challenge.'")
    time.sleep(3)
    if input(f"\nAre you feeling well enough, {name}? Do you want to write the history test or go home now? (stay/go home): ").strip().lower() == "stay":
        ask_history() # 'def ()' function number 4
    time.sleep(2)

    print(f"\n🎉[bold] You did it for today {name}, now go home and keep recovering from your sickness! [/bold]")
    time.sleep(1)
    print("\nTHANK YOU FOR PLAYING 😃")
else:
    print("Alright, rest up and get well soon!!") 

