# from app import app
from flask import render_template, request, redirect
from flask import Blueprint
from models.teams import Teams
from models.results import Results
import repositories.teams_repository as teams_repository
import repositories.results_repository as results_repository
import pdb



results_blueprint = Blueprint("results", __name__)

# @app.route('/')
# def index():
#     return render_template("index.html", title="Home", results=results)

@results_blueprint.route("/results")
def results():
    results = results_repository.select_all() # NEW
    return render_template("results/index.html", all_results = results)

# @app.route('/results', methods=['POST'])
# def add_result():
#     home_team_name = request.form['home_team_name']
#     away_team_name = request.form['away_team_name']
#     home_score = request.form['home_score']
#     away_score = request.form['away_score']
#     game_date = request.form['game_date']
#     new_result = Results(home_team_name, away_team_name, home_score, away_score, game_date)
#     add_result(new_result)

#     return redirect('/events')

# NEW
# GET '/results/new'
@results_blueprint.route("/results/new", methods=['GET'])
def new_result():
    results = results_repository.select_all()
    return render_template("results/new.html", all_results = results)

# CREATE
# POST '/results'
@results_blueprint.route("/results",  methods=['POST'])
def create_results():
    pdb.set_trace()
    away_team_name = request.form['away_team_name']
    home_team_name = request.form['home_team_name']
    
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    game_date = request.form['game_date']
    results = Results(home_team_name,away_team_name, home_score, away_score, game_date)
    print(results.__dict__)
    teams_repository.save(results)
    return redirect('/results')


# SHOW
# GET '/results/<id>'
@results_blueprint.route("/results/<id>", methods=['GET'])
def show_results(id):
    teams = results_repository.select(id)
    return render_template('results/show.html', results = results)

# EDIT
# GET '/results/<id>/edit'
@results_blueprint.route("/results/<id>/edit", methods=['GET'])
def edit_results(id):
    results = results_repository.select(id)
    results = results_repository.select_all()
    return render_template('results/edit.html', resutls = results, all_results = results)

# UPDATE
# PUT '/results/<id>'
@results_blueprint.route("/results/<id>", methods=['POST'])
def update_results(id):
    home_team_name    = request.form['home_team_name']
    away_team_name = request.form['away_team_name']
    home_score   = request.form['home_score']
    away_score   = request.form['away_score']
    game_date = request.form['game_date']
    results = Results(home_team_name, away_team_name, home_score, away_score,game_date, id)
    results_repository.update(results)
    return redirect('/results')

# DELETE
# DELETE '/results/<id>'
@results_blueprint.route("/results/<id>/delete", methods=['POST'])
def delete_results(id):
    results_repository.delete(id)
    return redirect('/results')