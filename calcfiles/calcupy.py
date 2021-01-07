#!/usr/bin/env python3

# global variables used in this file
message = "\nCalculator in Python, please enter two values (int or decimals okay) and then an operator. \n"
operators_possible = ["+", "-", "*", "/"]

# function to do the calculation and print result
def calcAdd(val1, val2):
    print("results: ", val1 + val2)

def calcMinus(val1, val2):
    print("results: ", val1 - val2)

def calcMulti(val1, val2):
    print("results: ", val1 * val2)

def calcDiv(val1, val2):
    print("results: ", val1 / val2)

# function to get user input and call calc
def userEntry():
    print(message)
    round = 0
    userOps = ""
    quit = ""
    while True and quit != "q":
        try:
            val1 = float(input("Please enter the first number: "))
            val2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Please enter only a decimal or integer value or q to quit")
    while round < 3 or  userOps != "q":
        userOps = input("Please enter an operator ( + - * / ) ").strip()
        if userOps == "+":
            calcAdd(val1, val2)
            break
        elif userOps == "-":
            calcMinus(val1, val2)
            break
        elif userOps == "*":
            calcMulti(val1, val2)
            break
        elif userOps == "/":
            calcDiv(val1, val2)
            break
        elif userOps == "q":
            print("Goodbye!")
            break
        elif userOps not in operators_possible:
            print('oopsy - please enter only + - * /  or q to quit: ')
            round += 1
        elif round == 3: 
            print('sorry - you had three tries, comeback later') 

userEntry()



