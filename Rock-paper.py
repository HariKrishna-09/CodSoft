import random

def get_computer():
    return random.choice(["rock", "paper", "scissors"])

def get_user():
    while True:
        choice = input("\nChoose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("\nInvalid input. Please try again.\n")

def winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Developed by Hari Krishna (CodSoft Intern) \n")

    while True:
        user = get_user()
        computer = get_computer()

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        result = winner(user, computer)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore Card :- You: {user_score} | Computer: {computer_score}\n")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing!\n")
            print("________________________________________________\n")
            print("\nMatch Summary:-\n")
            if user_score > computer_score:
                print("🎉 Congrats!!! You Won The Game")
            elif user_score == computer_score:
                print("🤝 Ohhh!! It's a Tie Between You and the Computer")
            else:
                print("💻 Computer Won The Game\nBetter Luck Next Time!")

            break
game()
