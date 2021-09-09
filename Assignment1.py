import random
userscore=0
computerscore=0
choices={}
for i in range(1,11):
        user_choice = input("Enter a choice (rock, paper, scissors)\n")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie ")
            winner='tie'
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors. You win")
                userscore=userscore+1
                winner='user'
            else:
                print("Paper covers rock. You lose.")
                computerscore=computerscore+1
                winner='computer'
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock.  You win")
                userscore=userscore+1
                winner='user'
            else:
                print("Scissors cuts paper. You lose.")
                computerscore=computerscore+1
                winner='computer'
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper. You win")
                userscore=userscore+1
                winner='user'
            else:
                print("Rock smashes scissors. You lose.")
                computerscore=computerscore+1
                winner='computer'
        choices[i]=[user_choice, computer_choice, winner]
print(f"\nThe final scores are \nUser = {userscore}\nComputer = {computerscore}\n")
print("\nUser wins" if userscore > computerscore else "\nComputer wins")
roundnum = int(input("\nEnter the Round number for details.\n"))
if choices[roundnum][2] == 'Tie':
        print(f"Round {roundnum} was tied")
else:
        print(f"User Choice = {choices[roundnum][0]}\nComputer Choice = {choices[roundnum][1]}\n{winner} won Round {roundnum}")



        
