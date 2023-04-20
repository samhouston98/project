import pdb
from models.teams import Teams
from models.results import Results

import repositories.teams_repository as teams_repository
import repositories.results_repository as results_repository

teams_repository.delete_all()
results_repository.delete_all()

team1 = Teams("Scotland", "Steve Clark", "Hampden Park", 1873)
teams_repository.save(team1)
team2 = Teams("England", "Gareth Southgate", "Wembley", 1870)
teams_repository.save(team2)
team3 = Teams("Wales", "Ryan Giggs", "Millenium Stadium", 1890)
teams_repository.save(team3)


result1 = Results("Scotland", "England", 4, 1, "May 3rd")
results_repository.save(result1)

result2 = Results("Wales", "Scotland", 2, 3, "March 9th")
results_repository.save(result2)

result3 = Results("England", "Wales", 2, 1, "June 11th")
results_repository.save(result3)

