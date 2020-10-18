__author__ = 'yedidya rashi'

from time import sleep
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
    except ValueError:
        print('this input need must be an integer')
        print('the input is not correct the program will end')
        break
    # command: create a new contact
    if command == 1:
        create_contact()
    # command: find a contact
    elif command == 2:
        find_contact()
    # command:update number
    elif command == 3:
        update_contact_number(input('what is the contact first name? '),
                              input('what is the contact last name? '),
                              input('enter the new number '), )
    # command:showing the specific contact that you want to delete confirm with the user and execute
    elif command == 4:
        first, last = input('what is the contact first name? '), input('what is the contact last name? ')
        select_specific_contact(first, last)
        ans = delete_verification()
        if ans == 'y':
            delete_specific_contact(first, last)
    # command:showing the all contacts that you want to delete confirm with the user and execute
    elif command == 5:
        select_all_contacts()
        ans = delete_verification()
        if ans == 'y':
            delete_all_contacts()
    # command:showing the all contacts
    elif command == 6:
        select_all_contacts()
    # end the program
    else:
        break
    print('\n-----------------------\n')
    # stop the script to certain seconds
    sleep(2.5)
print('program ended')
