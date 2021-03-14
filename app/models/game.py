class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self, choice_1, choice_2):
        if choice_1 == choice_2:
            return "a draw..."
        elif choice_1 == "rock" and choice_2 == "scissors":
                return "Player 1 wins!"
        elif choice_1 == "rock" and choice_2 == "paper":
                return "Player 2 wins!"
        elif choice_1 == "scissors" and choice_2 == "rock":
                return "Player 2 wins!"
        elif choice_1 == "scissors" and choice_2 == "paper":
                return "Player 1 wins!"
        elif choice_1 == "paper" and choice_2 == "scissors":
                return "Player 2 wins!"   
        elif choice_1 == "paper" and choice_2 == "rock":
                return "Player 1 wins!"   
        

