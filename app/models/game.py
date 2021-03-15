class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
  

    def play_game(self, player_1_choice, player_2_choice):
        winner = "player 2"

        if player_1_choice == player_2_choice:
            winner = "draw"
        if player_1_choice == "rock" and player_2_choice == "scissors":
            winner = "player 1"
        if player_1_choice == "scissors" and player_2_choice == "paper":
            winner = "player 1"
        if player_1_choice == "paper" and player_2_choice == "rock":
            winner = "player 1"

        return winner
        

