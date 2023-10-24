from lib.Space import Space

class Space_repository():
    def __init__(self, connection):
        self._connection = connection

    def all_spaces(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = [Space(
            row['id'],
            row['name'],
            row['description'],
            row['price'],
            row['availability_from'],
            row['availability_till'],
            row['calendar']
            ) for row in rows]

        return spaces

    def add_space(self, space_object):
        self._connection.execute("INSERT INTO spaces (name, description, price, availability_from, availability_till, calendar) "\
                                 "VALUES (%s, %s, %s, %s, %s, %s)",
                                 [space_object.name, space_object.description, space_object.price, space_object.availability_from, space_object.availability_till, space_object.calendar])