from db.run_sql import run_sql

from models.results import Results
from models.teams import Teams
import repositories.teams_repository as teams_repository
import repositories.results_repository as results_reposiory


def save(result):
    sql = "INSERT INTO results (home_team_name, away_team_name, home_score, away_score, game_date) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [result.home_team_name, result.away_team_name, result.home_score, result.away_score, result.game_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    result.id = id
    return result


def select_all():
    results_list = []

    sql = "SELECT * FROM results"
    results = run_sql(sql)

    for row in results:
        results = Results(row['home_team_name'], row['away_team_name'], row['home_score'], row['away_score'] , row['game_date'], row['id'] )
        results_list.append(results)
    return results_list



def select(id):
    results = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        # results = teams_repository.select(result['teams_id'])
        results = Results(result['home_team_name'], result['away_team_name'], result['home_score'], result['away_score'] , result['game_date'], result['id'])
    return results


def delete_all():
    sql = "DELETE FROM results"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM results WHERE id = %s"
    values = [id]
    print(values)
    run_sql(sql, values)


def update(results):
    sql = "UPDATE teams SET (home_team_name, away_team_name, home_score, away_score, game_date) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [results.home_team_name, results.away_team_name, results.home_score, results.away_score, results.game_date, results.id]
    run_sql(sql, values)
