from sqlite3 import *
from contacs import Contacts

# create new data base
conn = connect('contacs.db')

# a cursor of connection
c = conn.cursor()

# create a table if there is a table the output will be "table has already been created"
try:
    c.execute("""CREATE TABLE contacts
        (
        first text,
        last  text,
        number text,
        address text
        )
 """)
except OperationalError:
    print('table has already been created')


# sql command that create new contact for more detail about the class that this func uses go to contacts.py
def insert_contacts(contact):
    with conn:
        c.execute("INSERT INTO contacts VALUES(:first,:last,:number,:address)",
                  {'first': contact.first, 'last': contact.last, 'number': contact.number, 'address': contact.address})


# class of sql commands that's find contact by first and last name, phone number and by address
class Find:
    @staticmethod
    def get_by_first(first):
        with conn:
            c.execute("SELECT * FROM contacts WHERE first=?", (first,))
            for i in c.fetchall():
                print(i)

    @staticmethod
    def get_by_last(last):
        with conn:
            c.execute("SELECT * FROM contacts WHERE last=?", (last,))
            for i in c.fetchall():
                print(i)

    @staticmethod
    def get_by_number(number):
        with conn:
            c.execute("SELECT * FROM contacts WHERE number=?", (number,))
            for i in c.fetchall():
                print(i)

    @staticmethod
    def get_by_address(address):
        with conn:
            c.execute("SELECT * FROM contacts WHERE address=?", (address,))
            for i in c.fetchall():
                print(i)


# implementation of the Find class by cli input
def find():
    try:
        find_command = int(input('which operator do you want to operate:'
                                 '\n(1)find by first name'
                                 '\n(2)find by last name'
                                 '\n(3)find by phone number'
                                 '\n(4)find by address\n\n'))
        if find_command == 1:
            Find.get_by_first(str(input('enter the value:')))
        elif find_command == 2:
            Find.get_by_last(str(input('enter the value:')))
        elif find_command == 3:
            Find.get_by_number(str(input('enter the value:')))
        elif find_command == 4:
            Find.get_by_address(str(input('enter the value:')))
    except:
        print('the input is not correct')


# update number by first and last name
def update_number(first, last, number):
    with conn:
        c.execute('UPDATE contacts SET number =? WHERE first=? AND last=?', (number, first, last))


# create_contact
def create_contact():
    for _ in range(int(input('how many contacts would you want to insert: '))):
        contact_to_insert = Contacts(str(input('first name: ')), str(input('last name: ')), str(input('phone number:')),
                                     str(input('address')))
        print(contact_to_insert)
        insert_contacts(contact_to_insert)


# showing the whole table
def select_all():
    print('this is all tables:\n\n')
    with conn:
        for rows in c.execute('SELECT * FROM contacts'):
            print(rows)


# showing specific row
def select_specific(first, last):
    print('this is the contact:\n\n')
    with conn:
        for rows in c.execute('SELECT * FROM contacts WHERE first=? AND last=?', (first, last)):
            print(rows)


# delete all contacts from the table
def delete_all():
    with conn:
        c.execute('DELETE FROM contacts')


# delete specific contact table
def delete_specific(first, last):
    with conn:
        c.execute('DELETE  FROM contacts WHERE first=? AND last=?', (first, last))
