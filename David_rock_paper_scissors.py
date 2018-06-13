"""This program let the user play rock, paper, scissors with the computer"""

print "Running Rock, Paper, Scissors..."

#Imports the random module and the sleep function
import random
from time import sleep

choices = ["ROCK", "PAPER", "SCISSORS"]

#Selects randomly for the computer
computerChoice = random.choice(choices)

#Asks the user for their choice and checks if it is valid
message = "Choose one of %s %s or %s: " % (choices[0], choices[1], choices[2])
valid = False

while not valid:  
  userChoice = raw_input(message).upper()

  for choice in choices:
    if userChoice == choice:
      valid = True
  
  if not valid:
    print "Invalid choice"
    sleep(1)
    
# Displays results
print "You chose %s" % userChoice
sleep(1)

print "The computer chose %s" %computerChoice
sleep(1)

if computerChoice == userChoice:
  print "The game is a tie"

elif userChoice == choices[0] and computerChoice == choices[2] \
or userChoice == choices[1] and computerChoice == choices[0] \
or userChoice == choices[2] and computerChoice == choices[1]:
  print "The user wins"

else:
  print "The computer wins"
sleep(1)

#Finished
print "Exiting Rock, Paper, Scissors..."
    