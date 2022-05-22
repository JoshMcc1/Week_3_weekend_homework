from flask import render_template, request
from app import app
from models.game import play_game, create_computer_player
from models.player import Player

global player_1
global player_2


@app.route("/")
def index():
    return render_template(
        "index.html", title="Rock, Paper, and Scissors the Online Game!"
    )


@app.route("/player1choice", methods=["POST"])
def choice_1():
    global player_1
    player_name = request.form["name"]
    player_choice = request.form["choice"]
    player_1 = Player(player_name, player_choice)
    return render_template("player1choice.html", title="Hello!", player1=player_1)


@app.route("/result", methods=["POST"])
def choice_2():
    global player_2
    player_name = request.form["name"]
    player_choice = request.form["choice"]
    player_2 = Player(player_name, player_choice)
    winning_player = play_game(player_1, player_2)
    return render_template("result.html", title="Result", winning_player=winning_player)


@app.route("/play")
def play_computer():
    global player_1
    player_1 = create_computer_player()
    return render_template("play.html", title="Play with computer", computer=player_1)
