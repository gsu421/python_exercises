
# coding: utf-8

# In[1]:


import os
import csv

csvpath = os.path.join("Resources/store_items.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# In[2]:


sports_store = {"snowboard": 10, "helment": 15, "gloves": 5, "binding": 30, "snacks":{"energy bar": 5, "granola bar": 6, "chewy": 10}}


# In[9]:


def add_an_item(item):
    # if adding an existing item
    if add_new_item in sports_store:
            sports_store[item] = int(sports_store[item]) + int(increase_quantity)
    # if adding a brand new item
    else:
            sports_store[item] = int(increase_quantity)    


# In[10]:


manage_system = 'Y'
while (manage_system.capitalize() == 'Y'):
    action_item = input("What would you like to do? (A)dd a new item , (R)emove an existing one, or to (D)isplay all the items currently in stock")   
    if action_item.capitalize() == 'A':
        add_new_item = input('what item would you like to add?')
        increase_quantity = input('how many would you like to add?')
        add_an_item(add_new_item)
    elif action_item.capitalize() == 'R':
        remove_item = input('what item would you like to remove?')
        if remove_item in sports_store:
            del sports_store[remove_item]
        else:
            print("itmes is not in the store")
    elif action_item.capitalize() == 'D':
        for key, value in sports_store.items():
            print(key + ": " + str(value))
    else:
        print("Sorry the action is not available")
    manage_system = input('Would you like to continue to work? (Y)es or (N)o')

