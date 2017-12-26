
# coding: utf-8

# In[1]:


import random as rand


# In[2]:


def rpc_logic(comp, user):
    RPC={'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    if (comp == 'r' and user.lower() == 'r'):
        print("It's a tie\nComputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
        
    elif (comp == 'r' and user.lower() == 'p'):
        print("You win!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
    
    elif (comp == 'r' and user.lower() == 's'):
        print("You lose!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
    
    elif (comp == 'p' and user.lower() == 'r'):
        print("You lose!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
        
    elif (comp == 'p' and user.lower() == 'p'):
        print("It's a tie\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
        
    elif (comp == 'p' and user.lower() == 's'):
        print("You win!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
    
    elif (comp == 's' and user.lower() == 'r'):
        print("You win!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
        
    elif (comp == 's' and user.lower() == 'p'):
        print("You lose!!!\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
        
    elif (comp == 's' and user.lower() == 's'):
        print("It's a tie\ncomputer's choice is %s, and yous is %s" %(RPC[comp], RPC[user.lower()]))
    
    else:
        print('Your entry is not valid')


# In[3]:


# Prompt for question
options = ['r','p', 's']
comp = rand.choice(options)
user = input("What's your choice? (R)ock, (P)aper, or (S)cissors")

continue_play = 'Y'
while (continue_play.capitalize() == 'Y'):
    rpc_logic(comp, user)
    continue_play = input("Do you want to play again? (Y)es, (N)o ?")
    

