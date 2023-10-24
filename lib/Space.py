## Space
# Properties:
# - self.id - INT
# - self.name - STRING
# - self.description - STRING
# - self.price - FLOAT
# - self.availability_from - STRING
# - self.availability_till - STRING
# - self.calendar - DICT (date:boolean)

class Space():
    def __init__(self, id, name, description, price, availability_from, availability_till, calendar):
        self.id = id
        self.name = name
        self. description = description
        self.price = price
        self.availability_from = availability_from
        self.availability_till = availability_till
        self.calendar = calendar

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nAvailable: {self.availability_from} - {self.availability_till}\nDates: {self.calendar}"
