# Date 06-10-2025
# We all have played snake, water gun game in our childhood. 
# If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.
'''
1 for snake
-1 for water
0 for gun
'''

import random

# for final score
computer_win = 0
you_win = 0
Tie = 0

while True:  # Game loop
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    # Check invalid input
    if youstr not in youDict:
        print(" Invalid choice! Please enter 's', 'w', or 'g'.")
        continue

    you = youDict[youstr]

    # By now we have 2 numbers (variables), you and computer
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("Its a draw")
        Tie += 1
    else:
        if computer == -1 and you == 1:
            print("You win!")
            you_win += 1

        elif computer == -1 and you == 0:
            print("You Lose!")
            computer_win += 1

        elif computer == 1 and you == -1:
            print("You lose!")
            computer_win += 1

        elif computer == 1 and you == 0:
            print("You Win!")
            you_win += 1

        elif computer == 0 and you == -1:
            print("You Win!")
            you_win += 1

        elif computer == 0 and you == 1:
            print("You Lose!")
            computer_win += 1

        else:
            print("Something went wrong!")

    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print(f"\nFinal Scores:\nYou: {you_win}\nComputer: {computer_win}\nTies: {Tie}")
        print("👋 Thanks for playing! Goodbye!")

        # 🎯 SCOREBOARD LOGIC ADDED HERE
        with open("scoreboard.txt", "w") as f:
            f.write("=== Snake Water Gun Game Scoreboard ===\n")
            f.write(f"You: {you_win}\n")
            f.write(f"Computer: {computer_win}\n")
            f.write(f"Ties: {Tie}\n")
            f.write("\nThanks for playing!\n")

        break
