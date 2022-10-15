import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# First, some functions to determine the player and computer moves and who won (or if it's a tie).
def player_turn(n):
    if n == 1:
        return rock
    elif n == 2:
        return paper
    else:
        return scissors

def computer_turn(n):
    time.sleep(1) # The computer move is shown after a 1 sec delay.
    return player_turn(n)

def is_victory(player_choice, computer_choice):
    if computer_choice in loses_to[player_choice]:
        return 'You won!'
    elif player_choice in loses_to[computer_choice]:
        return 'The computer won!'
    else:
        return 'It\'s a tie!'

# We create a dictionary of sets for is_victory(). The sets represent all of the items that lose to the key element in the dictionary.
# This will allow us adding new items in our game in case we want to spice it up a bit
# (for example, Rock, Paper, Scissors, Lizard and Spock )
loses_to = {
    rock: {scissors},
    paper: {rock},
    scissors: {paper}
}

# Let's ask the user for their choice of move and use a while loop till they enter a valid value.
choice = int(input('What do you choose? Type 1 for Rock, type 2 for Paper or type 3 for Scissors.\n'))
while choice not in range(1,4):
    choice = int(input('Please enter a value between 0 and 2.\n'))
print(f'You chose {player_turn(choice)}')
        

# The computer move will be chosen randomly using the random module. 
computer_choice = random.randint(0,2)
print(f'The computer chose {computer_turn(computer_choice)}')

# Let's see if there's a victory...
print(is_victory(player_turn(choice), computer_turn(computer_choice)))




