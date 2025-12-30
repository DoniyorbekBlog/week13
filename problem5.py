import itertools
import random
n=0
d=1
team_names = ["Tigers", "Dragons", "Eagles", "Sharks", "Wolves", "Bears"]
random.shuffle(team_names)
for team1, team2 in itertools.combinations(team_names, 2):
    print(f"Match {d}: {team1} vs {team2}")
    d+=1
    n+=1
print(n)