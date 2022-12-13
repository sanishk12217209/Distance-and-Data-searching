#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.A Robot moves in a Plane starting from the origin point (0,0).The robot can move UP,DOWN,LEFT,and RIGHT. 
The trace of Robot movement is as given following:UP 5DOWN 3LEFT 3RIGHT 2(The numbers after 
directions are steps) Write a program to compute the current distance from the origin point after sequencing 
of movements. Hint: Use the math module.


# In[1]:


import math

x, y = 0, 0

while True:
    movement = input("ENTER THE STEPS MOVED IN THE ORDER NORTH/SOUTH/WEST/EAST: ")

    if movement == "":
        break

    else:
        movement = movement.split(" ") 

        if movement[0] == "NORTH":
            y = y + int(movement[1])
        elif movement[0] == "SOUTH":
            y = y - int(movement[1])
        elif movement[0] == "WEST":
            x = x - int(movement[1])
        elif movement[0] == "EAST":
            x = x + int(movement[1])

c = math.sqrt(x**2 + y**2)

print("Distance from starting point:", c)


# In[ ]:





# In[ ]:


2. Data of XYZ company is stored in a sorted list. Write a program to search for specific data 
from that list.Hint:Use if/elif to deal with conditions.


# In[3]:


data = input("Enter the list seperated by hyphen")
data_to_search = input("Enter the data to be found from the list ")

split_data = str(data).split("-")

if data_to_search in split_data:
    print(f"{data_to_search} is present in given list at position {split_data.index(data_to_search)+1}")
else:
    print( f"{data_to_search} not found in the given data list")

