#!/usr/bin/python3
# LIST OF FLAVORS
icecream = ["flavors", "salty"]

# APPEND THE INTEGER 99 TO THE LIST CREATED ABOVE
icecream.append(99)

# CHECKING TO SEE IF IT WORKED (IT DID)
print(icecream)

# INPUT ASKING FOR USERS NAME
user_name = input("What is your name? ")

# OUTPUT EVERYTHING 
print(f"{icecream[-1]} {icecream[0]}, and {user_name} chooses to be {icecream[1]}.")



