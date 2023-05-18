import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
playerScore = 0
computerScore = 0
running = True

while running:
    player = None

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor)")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")

    elif player == "rock" and computer == "scissors":
        print("you win!")

    elif player == "paper" and computer == "rock":
        print("you win!")

    elif player == "scissors" and computer == "paper":
        print("you win!")

    else:
        print("You lose!")

    if not input("Play again? (y/n)").lower() == "y":
        running = False


print("GG noob ")










