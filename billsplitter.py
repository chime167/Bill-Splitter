#!usr/bin/env python3

number_of_friends = int(input('Enter the number of friends joining (including you):\n'))
if number_of_friends > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    friends = {input(): 0 for _ in range(number_of_friends)}
    print(f'\n{friends}')
else:
    print('\nNo one is joining for the party')
