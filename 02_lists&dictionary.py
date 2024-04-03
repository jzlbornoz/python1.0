# List Comprenhension
numbers = [i for i in range(0, 100) if i % 2 == 0]

print(numbers)

dict = {}
for i in range(1, 5):
  dict[i] = i * 2

#print(dict)
dict = {i: i * 2 for i in range(1, 5)}
print(dict)

teams = ['barca', 'madrid', 'chelsea']
goals = [32, 43, 65]

teamsHistory = {}
for i in range(len(teams)):
  teamsHistory[teams[i]] = goals[i]

print(teamsHistory)

#Dictionary Comprenhension
teamsHistory = {teams[i]: goals[i] for i in range(len(teams))}
teamsHistoryV2 = {team: goal for (team, goal) in zip(teams, goals) if goal > 40}

print('first', teamsHistory)
print('second', teamsHistoryV2)
