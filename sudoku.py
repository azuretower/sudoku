#!/usr/bin/env python
import os

# I will be useing functions called chr() and ord()
# ord() returns the ascii value of the character passed to it
# chr() reverses ord() and returns the ascii chracter of the number passed to it

# setting up the default sudoku values
row_A = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_B = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_C = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_D = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_E = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_F = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_G = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_H = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
row_I = {'1': -1, '2': -1, '3': -1, '4': -1, '5': -1, '6': -1, '7': -1, '8': -1, '9': -1}
current_puzzle = {'A': row_A,
                  'B': row_B,
                  'C': row_C,
                  'D': row_D,
                  'E': row_E,
                  'F': row_F,
                  'G': row_G,
                  'H': row_H,
                  'I': row_I}


# printing out the current status of the puzzle
def print_puzzle():
    letters = 'ABCDEFGHI'
    print '    1 2 3 | 4 5 6 | 7 8 9'
    print ''
    temp = ''
    for i in range(1, 10):
        temp = ''
        temp += letters[i - 1] + '   '
        if i is 4:
            print '    - - - + - - - + - - -'
        if i is 7:
            print '    - - - + - - - + - - -'
        for j in range(1, 10):
            # chr(i+64) will return A through I, see top of file
            if current_puzzle[chr(i + 64)][str(j)] is -1:
                # the character to print if spot is empty
                temp += '. '
            else:
                temp += str(current_puzzle[chr(i + 64)][str(j)]) + ' '
            if j is 3:
                temp += '| '
            if j is 6:
                temp += '| '
        print temp


def print_menu():
    print ''
    print '1. Enter Number'
    print '2. Remove Number'
    print '3. Quit'
    print ''
    print status_message

# clears the terminal window
os.system('clear')
status_message = 'Welcome to Sudoku cli Edition!'

# Main program loop
while True:
    print_puzzle()
    print_menu()
    choice = raw_input(':')

    # Enter a number
    if choice is '1':
        status_message = 'Enter Location as Row Column Entry. ie: A 1 1'
        error = False
        row = ''
        column = -1
        number = -1
        os.system('clear')
        print_puzzle()
        print ''
        print status_message
        number = raw_input(':')
        try:
            row, column, number = number.split()
        except ValueError, e:
            status_message = 'Incorrect input'
            error = True
        if row != range(ord('A'), ord('J')):
            pass

        os.system('clear')
        if not error:
            status_message = ''

    elif choice is '2':
        os.system('clear')
        print ord('I')

    elif choice is '3':
        os.system('clear')
        print 'Bye Bye!'
        break

    else:
        os.system('clear')
        status_message = 'Choice is not Valid'
