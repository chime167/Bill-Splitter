#!usr/bin/env python3
import random


def bill_split():
    number_of_friends = int(
        input('Enter the number of friends joining (including you):\n'))
    if number_of_friends <= 0:
        print('\nNo one is joining for the party')
        return

    print('Enter the name of every friend (including you), each on a new line:')
    friends = {input(): 0 for _ in range(number_of_friends)}
    print('\nEnter the bill value:')
    bill = int(input())
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    luck_feature = input()
    if luck_feature.lower() == 'yes':
        winner = random.choice(list(friends))
        friends.update({friend: round(bill / (number_of_friends - 1), 2)
                       for friend in friends})
        friends.update({winner: 0})
        print(f'\n{winner} is the lucky one!')
        print(f'\n{friends}')
        return
    print('\nNo one is going to be lucky')
    friends.update({friend: round(bill / number_of_friends, 2)
                   for friend in friends})
    print(f'\n{friends}')
    return


bill_split()
