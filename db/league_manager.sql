DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS results;


CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  manager  VARCHAR(255),
  stadium VARCHAR (255),
  founded INT (255)
);

CREATE TABLE results (
  id SERIAL PRIMARY KEY,
  home_team_id INT REFERENCES teams(id),
  away_team_id INT REFERENCES teams(id),
  home_score INT,
  away_score INT
  game_date DATE
);