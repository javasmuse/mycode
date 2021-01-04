#!/usr/bin/env python3
user_name = input("Please enter your name: ")
user_day_of_week = input("What day of the week is it? ")

# PRINT OBJECTS
print("Hello ", user_name, "! Happy ", user_day_of_week, "!", sep="")

# CONCATENATION
print("Hello " + user_name + "! Happy " + user_day_of_week + "!")

# MIX AND MATCH
print("Hello", user_name + "! Happy", user_day_of_week + "!")

## alternate print out styles

## FORMAT
print("Hello {}! Happy {}!".format(user_name,user_day_of_week))

## F-STRING the shortest
print(f"Hello {user_name}! Happy {user_day_of_week}!")

