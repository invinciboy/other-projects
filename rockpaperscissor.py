
import random


rock = ('''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''')
paper = ('''
            _______
        ---'   ____)____
                  ______)
                  _______)
                _______)
        ---.__________)
        ''')

scissors = ('''
            _______
        ---'   ____)____
                  ______)
              __________)
              (____)
        ---.__(___)
        ''')


game_choice = [rock, paper, scissors]
print("Welcome to Rock Paper Scissor Game. This a game of 7!!!Good luck!!!")

userstat = 0
computerstat = 0

while userstat < 4 or computer_choice < 4:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    if user_input == 0 or user_input == 1 or user_input == 2:
        print("You chose:")
        print(game_choice[user_input])

    else:
        print("Invalid input.")

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_choice[computer_choice])

    if user_input == computer_choice:
        print("It's a Draw")

    elif user_input == 0 and computer_choice == 1:
        computerstat += 1

    elif user_input == 0 and computer_choice == 2:
        userstat += 1

    elif user_input == 1 and computer_choice == 0:
        userstat += 1

    elif user_input == 1 and computer_choice == 2:
        computerstat += 1

    elif user_input == 2 and computer_choice == 0:
        computerstat += 1

    elif user_input == 2 and computer_choice == 1:
        userstat += 1
    else:
        print("Invalid input.")
        computerstat += 1

    print(f"yourstat:{userstat}")
    print(f"computerstat: {computerstat}")


    if userstat == 4 and computerstat < 4:
        print("Congratulations! You won!!!")
        break
    else computerstat == 4 and userstat < 4:
        print("You lose!!!Better luck next time.")
        break

