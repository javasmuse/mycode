#!/usr/bin/env python3
#CREATE A LIST CALLED list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

# DISPLAY list1
print(list1)

# PRINT SECOND ITEM IN THE LIST
print(list1[1])

# CREATE A SECOND LIST list2
list2 = ["juniper"]

# COMBINED list1 AND list2 BY USE OF EXTEND
list1.extend(list2)

# PRINT THE COMBINED LIST
print(list1)

# CREATE A THIRD LIST list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

# COMBINE list3 to list1 BY USE OF APPEND
list1.append(list3)

# PRINT THE NEW COMBINED LIST
print(list1)

# PRINT ITEM 5 FROM THE NEW LIST
print(list1[4])

# PRINT THE FIRST ITEM FROM THE 4 ELEMENT OF THE COMPLEX LIST
print(list1[4][0])

# ANIMAL LIST OF 5 ANIMALS WITH 3 LETTER NAMES AND PRINT THEM TO THE SCREEN
animals = ["kid", "fox", "dog", "asp", "ape"]
print(animals)

# CHALLENGE FOR LISTS A LIST IN A LIST 
challenge = [1,2,3,["a","b","c",[1,4,7,"yeet"]]]
print(f"I think we can all agree that the Lion King is improved by a good {challenge[3][3][3]}")


