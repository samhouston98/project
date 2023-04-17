from db.run_sql import run_sql

from models.teams import Teams
from models.results import Results
import repositories.teams_repository as teams_repository
import repositories.results_repository as results_reposiory

def save(teams):
    sql = "INSERT INTO teams (name, manager, stadium, founded) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [teams.name, teams.manager, teams.stadium, teams.founded]
    results = run_sql(sql, values)
    results[0].id = id
    return teams


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Teams(row['name'], row['manager'], row['stadium'], row['founded'], row['id'] )
        teams.append(team)
    return teams


def select(id):
    teams = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        teams = Teams(result['name'], result['manager'], result['stadium'], result['id'] )
    return teams


def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(teams):
    sql = "UPDATE teams SET (name, manager, stadium, founded) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [teams.name, teams.manager, teams.stadium, teams.founded]
    run_sql(sql, values)

