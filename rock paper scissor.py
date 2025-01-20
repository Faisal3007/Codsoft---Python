import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def find_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Rock, Paper, Scissors - Let's play!")
    player_score = 0
    comp_score = 0
    
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again!")
            continue

        comp_choice = computer_choice()
        print(f"\nYou picked: {player_choice}")
        print(f"Computer picked: {comp_choice}")

        result = find_winner(player_choice, comp_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            comp_score += 1

        print(f"Score: Player - {player_score} | Computer - {comp_score}")
        
        play_more = input("\nPlay again? (y/n): ").lower()
        if play_more != 'y':
            print("Goodbye! Thanks for playing!")
            break

if __name__ == "__main__":
    main()