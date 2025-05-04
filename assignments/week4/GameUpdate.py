#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install rich # For bold text


# In[3]:


# To improve clarity and simplicity of the code, AI was partially used as a tool for assistance.

# ------------------------------------------------------------------------------------------------------------------------------------

from rich import print # For bold text with "print()"
import time # For time delays

# Additionally, "\033[1m" and "\033[0m" were used when bold text was needed for input prompts.

# -------------------- Time constants ----------------------

SHORT_BREAK = 0.25
MEDIUM_BREAK = 1
LONG_BREAK = 2
EXTRA_LONG_BREAK = 3

# ----------------- Function definitions -------------------

def ask_sleep(): # Function Nr. 1
    while True:
        try:
            sleep_quality = int(input("\nOn a scale from 1-10, how well did you sleep? "))
            time.sleep(SHORT_BREAK)
            if 1 <= sleep_quality <= 4:
                print("That's not so well.")
                time.sleep(MEDIUM_BREAK)
                break
            elif 5 <= sleep_quality <= 7:
                print("Well, that sounds solid.")
                time.sleep(MEDIUM_BREAK)
                break
            elif 8 <= sleep_quality <= 10:
                print("That sounds good.")
                time.sleep(MEDIUM_BREAK)
                break
            else:
                print("Please enter a number from 1 to 10.")
        except ValueError:
            print("Come on, I'm really curious—give me a number between 1 and 10")

# ------------------------------------------------------------------------------------------------------------------------------------
            
def test_math():
    time.sleep(MEDIUM_BREAK)
    print("Alright, then here are the questions:")
    time.sleep(LONG_BREAK)
    math_questions = {
        22: "1. What is the result of 7 + 15?",
        4: "2. What is the result of 3 - 3 - (-4)?",
        121: "3. What is the result of 11 x 11?",
        72: "4. What is the result of (-24) - 8 x 12?",
        1: "5. A prime number can only be divided by itself and which other number?"
    }

    for answer, question in math_questions.items():
        while True:
            try:
                guess = int(input(f"{question} "))
                if guess == answer:
                    print(f"✅ Correct! The answer was {answer}\n")
                    break
                else:
                    print("❌ Wrong answer :( Try again!\n")
            except ValueError:
                print("Please enter a valid number.")
        
        next_q = input("Next question? (yes/no) \033[1mIF YOU COMPLETED 5 QUESTIONS OR WANT TO EXIT THE TEST THEN TYPE NO\033[0m: ").strip().lower()
        if next_q == "no":
            break

def question_math(name): # Function Nr. 2
    time.sleep(MEDIUM_BREAK)
    print("Math Teacher: 'I have a test with five questions for you today.'")
    time.sleep(LONG_BREAK)
    while True:
        choice = input(f"\nI heard you’re not feeling well, {name}. Do you want to write the math test or rest until German class? (stay/rest): ").strip().lower()
        if choice == "stay":
            test_math()
            break
        elif choice == "rest":
            time.sleep(MEDIUM_BREAK)
            print("Alright, rest for now.")
            break
        else:
            print("Please enter 'stay' or 'rest'.")
        time.sleep(LONG_BREAK)

# ------------------------------------------------------------------------------------------------------------------------------------
        
def test_german():
    time.sleep(MEDIUM_BREAK)
    print("Alright, then here are the questions:")
    time.sleep(LONG_BREAK)
    german_questions = {
        3: "1. How many syllables does the word 'Germany' have?",
        "berlin": "2. What is the capital of Germany?",
        "noun": "3. What part of speech does the word 'rabbit' belong to?",
        "writing": "4. Every child in school should learn: reading and ...?",
        4: "5. How many grammatical cases are there in the German language?"
    }

    for answer, question in german_questions.items():
        while True:
            guess = input(f"{question} ").strip().lower()
            if str(guess) == str(answer).lower():
                print(f"✅ Correct! The answer was {answer}\n")
                break
            else:
                print("❌ Wrong answer :( Try again!\n")

        next_q = input("Next question? (yes/no) \033[1mIF YOU COMPLETED 5 QUESTIONS OR WANT TO EXIT THE TEST THEN TYPE NO\033[0m: ").strip().lower()
        if next_q == "no":
            break

def question_german(name): # Function Nr. 3
    time.sleep(MEDIUM_BREAK)
    print("German Teacher: 'Welcome to German class. I’ve prepared a test for today’s lesson.'")
    time.sleep(LONG_BREAK)
    while True:
        choice = input(f"\nHow are you feeling, {name}? Want to take the German test or rest until History class? (stay/rest): ").strip().lower()
        if choice == "stay":
            test_german()
            break
        elif choice == "rest":
            time.sleep(MEDIUM_BREAK)
            print("Alright, take a little break.")
            break
        else:
            print("Please enter 'stay' or 'rest'.")
        time.sleep(LONG_BREAK)

# ------------------------------------------------------------------------------------------------------------------------------------
        
def test_history():
    time.sleep(MEDIUM_BREAK)
    print("Alright, then here are the questions:")
    time.sleep(LONG_BREAK)
    history_questions = {
        1945: "1. When did the Second World War end (year)?",
        "france": "2. Where did the revolution from 1789 to 1799 take place?",
        1776: "3. In which year was the American Declaration of Independence signed?",
        4: "4. Into how many occupation zones was Germany divided after WWII?",
        2001: "5. In which year did the 9/11 attacks take place?"
    }

    for answer, question in history_questions.items():
        while True:
            guess = input(f"{question} ").strip().lower()
            if str(guess) == str(answer).lower():
                print(f"✅ Correct! The answer was {answer}\n")
                break
            else:
                print("❌ Wrong answer :( Try again!\n")

        next_q = input("Next question? (yes/no) \033[1mIF YOU COMPLETED 5 QUESTIONS OR WANT TO EXIT THE TEST THEN TYPE NO\033[0m: ").strip().lower()
        if next_q == "no":
            break

def question_history(name): # Function Nr. 4
    time.sleep(MEDIUM_BREAK)
    print("History Teacher: 'Alright, everyone — last subject: History! Let’s finish with a fun quiz.'")
    time.sleep(LONG_BREAK)
    while True:
        choice = input(f"\nDo you want to take the history test or go home now, {name}? (stay/go home): ").strip().lower()
        if choice == "stay":
            test_history()
            break
        elif choice == "go home":
            time.sleep(MEDIUM_BREAK)
            print("Alright, see you next time!")
            break
        else:
            print("Please enter 'stay' or 'go home'.")
        time.sleep(LONG_BREAK)

# --------------------- Main function -----------------------

def main():
    global name
    name = input("What is your name? ").strip().title()
    print(f"\n🎒[bold] Welcome to your virtual school day, {name}! [/bold]\n")
    time.sleep(LONG_BREAK)

    ask_sleep() # Function Nr. 1

    mood = input("\nDo you feel healthy enough to go to school today? (yes/no): ").strip().lower()
    if mood == "yes":
        time.sleep(MEDIUM_BREAK)
        print("\nGreat! But I’ll tell your teachers to check on you during the day...\n")
        time.sleep(EXTRA_LONG_BREAK)
        print("\n📚[bold] Today's schedule: 2h Math, 2h German, 2h History [/bold]")
        time.sleep(LONG_BREAK)

        print("\n[bold] NEXT UP => MATH CLASS [/bold]")
        question_math(name) # Function Nr. 2

        print("\n[bold] NEXT UP => GERMAN CLASS [/bold]")
        question_german(name) # Function Nr. 3

        print("\n[bold] NEXT UP => HISTORY CLASS [/bold]")
        question_history(name) # Function Nr. 4
        
        time.sleep(MEDIUM_BREAK)
        print(f"\n🎉[bold] You did it for today, {name}! [/bold]")
    else:
        time.sleep(MEDIUM_BREAK)
        print("Alright, rest up and get well soon!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

if __name__ == "__main__":
    main()

