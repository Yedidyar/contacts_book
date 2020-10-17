__author__ = 'yedidya rashi'

from sql_py import *

# running command until insert unavailable input
while True:
    # main menu can handle unexpected input
    try:
        command = int(input('which operator do you want to operate:'
                            '\n(1)create new contacts'
                            '\n(2)find contact'
                            '\n(3)update contact'
                            '\n(4)delete contact'
                            '\n(5)delete all table'
                            '\n(6)see table\n'))
    except:
        print('the input is not correct the program will end')
        break
    # command: create a new contact
    if command == 1:
        create_contact()
    # command: find a contact
    elif command == 2:
        find()
    # command:update number
    elif command == 3:
        update_number(input('what is the contact first name? '),
                      input('what is the contact last name? '),
                      input('enter the new number '), )
    # command:showing the specific contact that you want to delete confirm with the user and execute
    elif command == 4:
        first, last = input('what is the contact first name? '), input('what is the contact last name? ')
        select_specific(first, last)
        ans = input('---------------------------------------------'
                    '\nare you sure that you want to delete all data?[y/n]')
        if ans == 'y':
            delete_specific(first, last)
    # command:showing the all contacts that you want to delete confirm with the user and execute
    elif command == 5:
        select_all()
        ans = input('---------------------------------------------'
                    '\nare you sure that you want to delete all data?[y/n]')
        if ans == 'y':
            delete_all()
    # command:showing the all contacts
    elif command == 6:
        select_all()
    # end the program
    else:
        break
    print('\n-----------------------\n')
print('program ended')
