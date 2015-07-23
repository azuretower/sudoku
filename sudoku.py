#!/usr/bin/env python
import os

# Main menu loop
while True:
    os.system('clear')
    print '1. Add Number'
    print '2. Delete Number'
    print '3. Quit'

    choice = raw_input(': ')
    if choice is '1':
        pass

    elif choice is '2':
        pass

    elif choice is '3':
        os.system('clear')
        print 'Bye Bye!'
        break

    else:
        'Choice is not Valid'
