"""CodSoft Task 4 - Rock-Paper-Scissors with score tracking."""
import random

CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


def get_user_choice():
    while True:
        pick = input("Choose (r)ock, (p)aper or (s)cissors: ").strip().lower()
        if pick in CHOICES:
            return CHOICES[pick]
        if pick in CHOICES.values():
            return pick
        print("Invalid choice. Please try again.")


def decide(user, computer):
    if user == computer:
        return "tie"
    return "user" if BEATS[user] == computer else "computer"


def main():
    print("=== ROCK - PAPER - SCISSORS ===")
    print("Rock beats scissors, scissors beat paper, paper beats rock.\n")
    user_score = computer_score = 0
    round_no = 1

    while True:
        print(f"--- Round {round_no} ---")
        user = get_user_choice()
        computer = random.choice(list(BEATS))
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        winner = decide(user, computer)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")
        round_no += 1

        if input("Play another round? (y/n): ").strip().lower() != "y":
            print("\nFinal score ->", f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
