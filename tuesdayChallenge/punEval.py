#!/usr/bin/env python3

# app to test users appreciation for puns
message = ("\nDo you Love Puns? or do they make you Cringe? \n How much do you like puns? \n")
answer = " "
pun_score = 0

print(message)

joke_number = 0 

while joke_number < 6 and answer != "STOP":

    joke_number += 1
    print(joke_number)
    print("I can't believe I got fired from the calendar factory. All I did was take a day off.")
    answer = input("Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":    
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("My dog farted in an elevator, it was wrong on so many levels.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("What do you call a bee that can't make up it's mind? A maybe")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("I went to buy some camouglage pants yesterday, but didn't see any.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("Two windmills are standing in a wind farm. One asks - What's your favorite kind of music? The other replies - I'm a big metal fan.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("Why did the chicken cross the road? To prove to the possum it could be done.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 2
    elif answer == "LOL":
        pun_score += 2
    elif answer == "MEH":
        pun_score == pun_score
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("What's the difference between a hippos and a zippo? One is really heavy and the other is a little lighter.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("It's hard to explain puns to kleptomaniacs because they're always taking things literally.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")
    
    joke_number += 1
    print(joke_number)
    print("Will glass coffins be a success? Remains to be seen.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")

    joke_number += 1
    print(joke_number)
    print("Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea.")
    answer = input(
        "Rate the pun for humour: ( ROFL, LOL, MEH, CRY, STOP) \n").strip().upper()
    if answer == "ROFL":
        pun_score += 5
    elif answer == "LOL":
        pun_score += 3
    elif answer == "MEH":
        pun_score == 1
    elif answer == "CRY":
        pun_score == pun_score
    else:
        print("Sorry it appears you don't enjoy thoughtful humor.")


if pun_score > 45:
    print(f"Your score is {pun_score}, you like to laugh, any pun, any joke - excerise those endorphins.")
elif pun_score == 45:
    print(f"Your score is {pun_score}, you are punster - you probably drive your none pun friends nuts.")
elif pun_score > 38: 
    print(f"Your score is {pun_score}, you appear to enjoy the occasional bit of humor.")
elif pun_score > 20:
    print(f"Your score is {pun_score}, you live a sad life of no laughter.")
else :
    print(f"Your score is {pun_score}, you are not easily amused.")


