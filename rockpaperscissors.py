# we're going to create a game that simulates rock, paper, scissors in python
# with interactive user input

# next up: error checking
# thanks!

import random 

# keep score
wins = 0
draws = 0
losses = 0

play_again = "y"
# check to see if we want to play again
# and loop till they say no ("n")
while play_again == "y":

    print "Let's play Rock, Paper, Scissors!"
    # get the player's play
    my_play = raw_input("What do you play? (Rock, Paper, or Scissors?)").lower()

    choices = ["Rock","Paper","Scissors"]
    # get the computer's play
    their_play = random.choice(choices).lower()

    print "My play was {}, and their play was {}".format(my_play, their_play)
    

    # look at the winning conditions
    if my_play == "rock":
        winner = (their_play == "scissors")
        draw = (their_play == "rock")
        if winner:
            print "You win this round!"
            wins += 1
        elif draw:
            print "It was a draw."
            draws += 1
        else:
            print "You lost this round."
            losses += 1

    if my_play == "paper":
        winner = (their_play == "rock")
        draw = (their_play == "paper")
        if winner:
            print "You win this round!"
            wins += 1
        elif draw:
            print "It was a draw."
            draws += 1
        else:
            print "You lost this round."
            losses += 1

    if my_play == "scissors":
        winner = (their_play == "paper")
        draw = (their_play == "scissors")
        if winner:
            print "You win this round!"
            wins += 1
        elif draw:
            print "It was a draw."
            draws += 1
        else:
            print "You lost this round."
            losses += 1

    print "The score after this round is: {}w {}l {}d".format(wins, losses, draws)
            
    play_again = raw_input("Do you want to play again? (y/n)")
