set_teams = {'barca', 'madrid', 'chelsea'}

set_wc_years = {22, 18, 14, 10, 6, 2}

set_goals = {20, '12', 10, '8', 6, '4', '2'}

print(set_teams)
print(type(set_teams))
print(set_wc_years)
print(set_goals)

set_from_string = set('El campeon es argentina')

print(set_from_string)

set_from_tupla = set(('abc', 'def', 'ghi'))

print(set_from_tupla)

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 44, 44, 22, 22, 1, 1, 1, 3, 3, 3, 555
]
print(numbers)

uniqueNumbersArray = list(set(numbers))
print(uniqueNumbersArray)
