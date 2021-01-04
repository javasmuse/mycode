
#!/usr/bin/env python3

# CREATE A LIST OF 3 ITEMS
my_list = ["192.168.0.5", 5060, "UP"]

# PRINT THE FIRST LIST ITEM
print("The first item in the list (IP): " + my_list[0])

# PRINT THE SECOND LIST ITEM, IT WILL BE A STRING
print("The second item in the list (port): " + str(my_list[1]))

# PRINT THE THIRD LIST ITEM
print("The last item in the list (state): " + my_list[2])

# CREATE A NEW LIST
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ] 

# PRINT THE NEW LIST IN ONE LINE
print("When I", str(new_list[-1]), "into IP addresses", str(new_list[3]), "or", str(new_list[4]), "I am unable to ping ports", new_list[0], str(new_list[1]), "or", new_list[2])

# F String 
print(f"When I {str(new_list[-1])} into IP addresses {str(new_list[3])} or {str(new_list[4])} I am unable to ping ports {new_list[0]}, {str(new_list[1])}, or {new_list[2]}”)


