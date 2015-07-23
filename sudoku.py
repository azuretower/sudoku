#!/usr/bin/env python
import os

row_A = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_B = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_C = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_D = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_E = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_F = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_G = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_H = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_I = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}

current_puzzle = {'1': row_A, '2': row_B, '3': row_C, '4': row_D, '5': row_E, '6': row_F, '7': row_G, '8': row_H, '9': row_I}


def print_puzzle():
    letters = 'ABCDEFGHI'
    print '   1 2 3 | 4 5 6 | 7 8 9'
    print ''
    temp = ''
    for i in range(1, 10):
        temp = ''
        temp += letters[i - 1] + '  '
        if i is 4:
            print '   - - - + - - - + - - -'
        if i is 7:
            print '   - - - + - - - + - - -'
        for j in range(1, 10):
            if current_puzzle[str(i)][str(j)] is -1:
                temp += 'X '
            else:
                temp += str(current_puzzle[str(i)][str(j)]) + ' '
            if j is 3:
                temp += '| '
            if j is 6:
                temp += '| '
        print temp


# Main menu loop
os.system('clear')
while True:

    print ''
    print '1. Add Number'
    print '2. Delete Number'
    print '3. Quit'

    choice = raw_input(': ')
    if choice is '1':
        os.system('clear')
        print current_puzzle['A']['A1']

    elif choice is '2':
        os.system('clear')
        print_puzzle()


    elif choice is '3':
        os.system('clear')
        print 'Bye Bye!'
        break

    else:
        os.system('clear')
        'Choice is not Valid'
