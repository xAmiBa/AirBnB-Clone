from lib.Space import Space
import json

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
        
    def search_by_id(self, space_id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id=%s", [space_id])
        row = rows[0]
        return Space(
            row['id'],
            row['name'],
            row['description'],
            row['price'],
            row['availability_from'],
            row['availability_till'],
            row['calendar']
            )
    
    # renders list of html options for dropdown menu to list in template
    # all unavailable dates are greyed out
    def get_dates_by_id(self, space_id):
        space = self.search_by_id(space_id)

        # turn calendar dict string into dict
        calendar = json.loads(space.calendar)

        calendar_html = []
        for key, value in calendar.items():
            if value == True:
                calendar_html.append(f'<option value="{key}">{key}</option>')
            if value == False:
                calendar_html.append(f'<option value="{key}">not available</option>')
        return calendar_html
