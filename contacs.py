# class of contacts used in sql_py.py
class Contacts:
    def __init__(self, first, last, number, address):
        self.first = first
        self.last = last
        self.number = number
        self.address = address

    def __repr__(self):
        return f"name:{self.first} {self.last}, phone number:{self.number}, address: {self.address} "
