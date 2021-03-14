from flask import render_template

from app import app
from app.models.player import Player

@app.route('/<choice_1>/<choice_2>')
def play_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    return f"Player 1 chose: {choice_1} Player 2 chose: {choice_2} "