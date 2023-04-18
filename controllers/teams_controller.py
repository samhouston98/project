# from app import app
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.teams import Teams
from models.results import Results
import repositories.teams_repository as teams_repository
import repositories.results_repository as results_repository


teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = teams_repository.select_all() # NEW
    return render_template("teams/index.html", all_teams = teams)

# NEW
# GET '/teams/new'
@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = teams_repository.select_all()
    return render_template("teams/new.html", all_teams = teams)

# CREATE
# POST '/teams'
@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    name    = request.form['name']
    print(name)
    manager = request.form['manager']
    stadium   = request.form['stadium']
    founded   = request.form['founded']
    teams = Teams(name, manager, stadium, founded)
    teams_repository.save(teams)
    return redirect('/teams')


# SHOW
# GET '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['GET'])
def show_results(id):
    teams = teams_repository.select(id)
    return render_template('teams/show.html', teams = teams)

# EDIT
# GET '/teams/<id>/edit'
@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_teams(id):
    teams = teams_repository.select(id)
    teams = teams_repository.select_all()
    return render_template('teams/edit.html', teams = teams, all_teams = teams)

# UPDATE
# PUT '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_teams(id):
    name    = request.form['name']
    manager = request.form['manager']
    stadium   = request.form['stadium']
    founded   = request.form['founded']
    teams = Teams(name, manager, stadium, founded, id)
    print(teams.name())
    teams_repository.update(teams)
    return redirect('/teams')

# DELETE
# DELETE '/teams/<id>'
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_teams(id):
    teams_repository.delete(id)
    return redirect('/teams')
