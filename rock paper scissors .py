import random
def play_game():
    print("--- WELCOME TO ROCK, PAPER, SCISSORS! ---")
    
    # 1. Define the valid choices
    choices = ["rock", "paper", "scissors"]
    
    # 2. Get the player's input and make it lowercase
    player_choice = input("Enter rock, paper, or scissors: ").lower().strip()
    
    # 🚀 SPOT THE FIX (Input Validation): What if they type something else?
    if player_choice not in choices:
        print("Error: Invalid choice! Please type exactly rock, paper, or scissors.")
        return  # This stops the game safely before a logic crash happens
        
    # 3. Let the computer choose randomly
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")
    
    # 4. Determine the winner using logic blocks
    if player_choice == computer_choice:
        print("Result: It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("Result: You win! 🎉")
    else:
        print("Result: The computer wins! 🤖")