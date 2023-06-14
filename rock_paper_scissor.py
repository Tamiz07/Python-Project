import random

options = ['rock', 'paper', 'scissors']
game_running = True

# Initially player and computer won 0 game
player_won = 0
computer_won = 0

while game_running:
    player = None  # Initially player choice is  none
    computer = random.choice(options)  # computer choices

    # Checks if player enter a corrct choice or not
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) : ").lower()

    print("Player : ", player)
    print("Computer : ", computer)


    def is_win(user, opponent):
        global player_won, computer_won
        if user == opponent:
            return "It's a Tie..!"

        # rock > scissors, scissors > paper, paper > rock
        if (user == 'rock' and opponent == 'scissors') or (user == 'scissors' and opponent == 'paper') \
                or (user == 'paper' and opponent == 'rock'):
            player_won += 1  # count increase if player won the game
            return "Player Won ..!"

        computer_won += 1  # count increase if computer won the game
        return "Computer Won ..!"


    print(is_win(player, computer))
    print(f'Player {player_won} game won')
    print(f'Computer {computer_won} game won')

    if not input("Play again? (y/n) : ").lower() == 'y':
        game_running = False

print("Thanks for playing!")
