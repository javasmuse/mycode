#!/usr/bin/env python3

# global variables used in this file
message = "\nCalculator in Python, please enter two values (int or decimals okay) and then an operator. \n"
operators_possible = ["+", "-", "*", "/"]

# functions to do the calculation and print result
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
    while True:
        try:
            val1 = float(input("Please enter the first number: "))
            val2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Please enter only a decimal or integer value.")
    while round < 3 and userOps != "q":
        userOps = input("Please enter an operator ( + - * / ) ").strip()
        round += 1
        if round == 3:
            print("sorry - you had three tries, comeback later")
        elif userOps == "q":
            print("Goodbye.")
            break
        elif userOps == "+":
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
        elif userOps not in operators_possible:
            print('oopsy - please enter only + - * /  or q to quit: ')

userEntry()




































































