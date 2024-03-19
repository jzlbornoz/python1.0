set_teams = {'barca', 'madrid', 'chelsea', 'estudiantes'}

set_wc_years = {22, 18, 14, 10, 6, 2}

set_goals = {20, '12', 10, '8', 6, '4', '2'}

set_from_string = set('El campeon es argentina')

set_from_tupla = set(('abc', 'def', 'ghi'))

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 44, 44, 22, 22, 1, 1, 1, 3, 3, 3, 555
]

uniqueNumbersArray = list(set(numbers))
print(uniqueNumbersArray)

#add
set_teams.add('villa')
set_teams.add('liverpool')

#update  
set_teams.update({'girona' , 'atm'})

#remove
set_teams.remove('madrid')
set_teams.discard('bayern')
set_teams.discard('estudiantes')
#set_teams.remove('bayern') Error becouse not exist in the set

print(set_teams)