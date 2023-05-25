import time

def question(name):
    print("-------------------")
    print(f"{name}")
    print("-------------------")

def answers(a, b, c, d):
    print(f"A. {a}")
    print(f"B. {b}")
    print(f"C. {c}")
    print(f"D. {d}")

def countdown():
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

def theidiotquiz():
    score = 0
    print("Welcome to the idiot quiz!")
    time.sleep(3)
    print("This is a short quiz that will see if you have the IQ of a cheese stick.")
    time.sleep(3)
    print("Let's get on with it.")
    time.sleep(2.5)
    question("Question 1")
    time.sleep(1)
    print("What is the color of an orange?")
    answers("Red", "Orange", "Blue", "Magenta")
    q1 = input("Answer here: ")
    if q1 == "Orange" or q1 == "orange" or q1 == "b" or q1 == "B":
        print("You got it!")
        time.sleep(1)
        print("Let's move on to the next question.")
        score = score + 1
    elif q1 == "Red" or q1 == "red" or q1 == "a" or q1 == "A":
        print("Hmm. That's unfortunately incorrect. I can understand how red and orange are similar and how they can get mixed up sometimes.")
        time.sleep(4)
        print("Nobody's perfect. Let's just move on to the next question.")
    elif q1 == "Blue" or q1 == "blue" or q1 == "c" or q1 == "C":
        print("Blue???? How the hell did you even get blue???? The color of an orange is in its name! It's ORANGE! OR-ANGE!")
        time.sleep(5)
        print("Let's just move on, and pretend that this never happened.")
    elif q1 == "Magenta" or q1 == "magenta" or q1 == "d" or q1 == "D":
        print("Magenta??? How the hell did you even get magenta???? The color of an orange is in its name! It's ORANGE! OR-ANGE!")
        time.sleep(5)
        print("Let's just move on, and pretend that this never happened.")
    else:
        print("That isn't an answer dummy")
        time.sleep(1)
        print("Self destructing...")
        countdown()
        quit()
    countdown()
    question("Question 2")
    time.sleep(1)
    print("What direction does gravity pull us?")
    answers("Up", "Down", "Left", "Right")
    q2 = input("Answer here: ")
    if q2 == "Up" or q2 == "up" or q2 == "a" or q2 == "A":
        high = input("Are you high?: ")
        if high == "yes" or high == "Yes" or high == "y" or high == "Y":
            print("boi")
            time.sleep(0.3)
            quit()
        else:
            print("That's even worse. It's weird knowing that someone's brain is smaller than a fly. I think we both know who that is...")
            time.sleep(4)
    elif q2 == "Left" or q2 == "left" or q2 == "c" or q2 == "C":
        high = input("Are you high?: ")
        if high == "yes" or high == "Yes" or high == "y" or high == "Y":
            print("boi")
            time.sleep(0.3)
            quit()
        else:
            print("That's even worse. It's weird knowing that someone's brain is smaller than a fly. I think we both know who that is...")
            time.sleep(4)
    elif q2 == "Right" or q2 == "right" or q2 == "d" or q2 == "D":
        high = input("Are you high?: ")
        if high == "yes" or high == "Yes" or high == "y" or high == "Y":
            print("boi")
            time.sleep(0.5)
            quit()
        else:
            print("That's even worse. It's weird knowing that someone's brain is smaller than a fly. I think we both know who that is...")
            time.sleep(4)
    elif q2 == "Down" or q2 == "down" or q2 == "b" or q2 == "B":
        print("You got it correct! Don't feel to proud though. " + '\033[1m' + "Anyone " + '\033[0m' + "could have answered that.")
        score = score + 1
        time.sleep(3)
    else:
        print("That isn't an answer dummy")
        time.sleep(1)
        print("Self destructing...")
        countdown()
        quit()
    countdown()
    question("Question 3")
    time.sleep(1)
    print("What is the eighth letter of the alphabet? (you must put 'letter' in front!)")
    answers("Letter B", "Letter I", "Letter H", "Letter Z" )
    q3 = input("Answer here: ")
    if q3 == "Letter I" or q3 == "letter I" or q3 == "letter i" or q3 == "Letter i" or q3 == "b" or q3 == "B":
        print("Sorry but that is incorrect. You were close though. Letter I is actually the ninth letter, not the eighth.")
        time.sleep(5)
        print("Let's just move on to the next question.")
        time.sleep(2)
    elif q3 == "Letter H" or q3 == "letter H" or q3 == "letter h" or q3 == "Letter h" or q3 == "c" or q3 == "C":
        print("Correct! Good to know that you've passed preschool.")
        score = score + 1
        time.sleep(3)
    elif q3 == "Letter Z" or q3 == "letter Z" or q3 == "letter z" or q3 == "Letter z" or q3 == "d" or q3 == "D":
        print("Okay listen here you piece of shi-")
        time.sleep(1.5)
        quit()
    elif q3 == "Letter B" or q3 == "letter B" or q3 == "letter b" or q3 == "Letter b" or q3 == "a" or q3 == "A":
        counting = input("Do you know how to count?: ")
        if counting == "Yes" or counting == "yes" or counting == "y" or counting == "Y":
            print("Good! Then you must be able to count down until this quiz closes!")
            time.sleep(2)
            countdown()
            quit()
        else:
            print("Don't worry, I'll teach you! Try counting these numbers to the closing of this game!")
            time.sleep(3)
            countdown()
            quit()
    else:
        print("That isn't an answer dummy")
        time.sleep(1)
        print("Self destructing...")
        countdown()
        quit()
    countdown()
    question("Question 4")
    time.sleep(1)
    print("What line is 'Ya like jazz?' in the bee movie script?")
    q4 = int(input("Answer here: "))
    if q4 == 762:
        print("Either you're incredibly cultured, or you looked it up.")
        score = score + 1
        time.sleep(3)
    elif q4 == 69:
        print("nice")
        time.sleep(1)
        quit()
    elif q4 == 420:
        print("Contacting police...")
        time.sleep(3)
        print("Police Contacted!")
        time.sleep(1)
        print("If I were you, I would do as much drugs as I could before the cops arrive.")
        time.sleep(3)
    elif q4 == 69420:
        print("Hey, that's how much your mom weighs! (in metric tons)")
        time.sleep(3)
    elif q4 == 80085:
        print("Go to actual hell.")
        time.sleep(1)
        print("Initiating holy water in:")
        countdown()
        quit()
    elif q4 == 1:
        print("At least you still have the mental capacity to know the amount of brain cells you have left.")
        time.sleep(4)
    elif q4 == 0:
        print("Sorry, but I asked about the bee movie, not the likelyhood of you getting a girlfriend.")
        time.sleep(4)
    else:
        print("Nice try, but you're incorrect. Honestly, I don't know why I asked that question.")
        print("How am I this out of ideas that I already make the fourth question about the damn bee movie.")
        print("I have been typing an arangement of text characters for hours now. The sound of my clacking keyboard is engraved into my brain.")
        print("I just want it to end. I just want to finish this text file of hundreds of lines of code. Please make it stop...")
        time.sleep(15)
    countdown()
    print(f"You scored {str(score)}/4")
    playagain = input("Want to play again?: ")
    if playagain == "Yes" or playagain == "yes" or playagain == "y" or playagain == "Y":
        print("Starting in...")
        countdown()
        print("-----------------------------------")
        theidiotquiz()
    else:
        print("Closing in...")
        countdown()
        quit()
theidiotquiz()










