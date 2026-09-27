"""Match Coins Game
   Rachel Remick
   This file runs the game. It creates the Player objects and manages the game loop and rules.
   9/27/2026"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    print("Match Coins Game")

    answer: str = input("Would you like to play? (Y/N): ")
    while answer == "Y" or answer == "y":
        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_side()
        side2 = player2.get_side()
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")
        if side1 == side2:
            print(f"It's a match! {player1.get_name()} wins a coin!")
            player1.win_coin()
            player2.lose_coin()
        else:
            print(f"No match! {player2.get_name()} wins a coin!")
            player2.win_coin()
            player1.lose_coin()
        print(f"{player1.get_name()} has {player1.get_wallet()}")
        print(f"{player2.get_name()} has {player2.get_wallet()}")
        answer = input("Would you like to play again? (Y/N): ")

    print("--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if (player1.get_wallet() == player2.get_wallet()):
        print("It's a draw!")
    elif (player1.get_wallet() > player2.get_wallet()):
        print(f"{player1.get_name()} wins!")
    else:
        print(f"{player2.get_name()} wins!")









