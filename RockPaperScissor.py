#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


from enum import IntEnum


# In[3]:


class Action(IntEnum):
    Rock=0
    Paper=1
    Scissor=2


# In[4]:


def get_user_choice():
    choices = [f"{action.name}={action.value}" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action=Action(selection)
    return action


# In[5]:


def get_computer_choice():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


# In[6]:


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissor:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Rock smashes scissor! You win!")
        else:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Paper covers rock! You win!")
        else:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Scissor cuts paper! You lose.")
    elif user_action == Action.Scissor:
        if computer_action == Action.Paper:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Scissor cuts paper! You win!")
        else:
            print(f"your choice is {user_action.name}")
            print(f"Computer choice is {computer_action.name}")
            print("Rock smashes scissor! You lose.")


# In[7]:


while True:
    try:
        user_action = get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_choice()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


# In[ ]:




