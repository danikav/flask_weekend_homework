from flask import render_template

from app import app
# from app.models.player import Player
from app.models.game import Game

@app.route('/')
def home():
    return render_template(
        'index.html',
        title = "Rock, Paper, Scissors")

@app.route('/<choice_1>/<choice_2>')
def game(choice_1, choice_2):
    player_1_choice = choice_1.lower()    
    player_2_choice = choice_2.lower()
    winner = Game(player_1_choice, player_2_choice).play_game(player_1_choice, player_2_choice)
    
    return render_template(
        "game.html", 
        title = "The Results",
        winner=winner, 
        player_1_choice=player_1_choice, 
        player_2_choice=player_2_choice,
        )



    

