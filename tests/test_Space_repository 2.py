from lib.database_connection import DatabaseConnection
from lib.Space_repository import Space_repository
from lib.Space import Space

"""
When I call all_spaces() method
all spaces are showing
"""
def test_all_spaces(db_connection):
    db_connection.seed('seeds/db_makers_bnb.sql')
    repository = Space_repository(db_connection)

    assert repository.all_spaces() == [ 
        Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}'
        ),
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}'
        ),
        Space(
            3,
            'Beachfront Paradise',
            'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
            300,
            '22/11/22',
            '05/01/23',
            '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}'
        )
        ]
    

"""
When I call add_space() method
new space is added to database
"""
def test_add_new_space(db_connection):
    repository = Space_repository(db_connection)
    db_connection.seed('seeds/db_makers_bnb.sql')

    test_space = Space(
        None,
        "test name",
        "test description",
        666,
        "test availability_from",
        "test avaiability_till",
        "{test:calendar}"
        )
    repository.add_space(test_space)
    assert repository.all_spaces() == [ 
        Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}'
        ),
        Space(
            2,
            'Modern Urban Loft',
            'Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.',
            200,
            '15/11/22',
            '01/12/22',
            '{"15/11/22":true, "16/11/22":true, "17/11/22":true, "18/11/22":true, "19/11/22":true, "20/11/22":true, "21/11/22":true, "22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true}'
        ),
        Space(
            3,
            'Beachfront Paradise',
            'Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.',
            300,
            '22/11/22',
            '05/01/23',
            '{"22/11/22":true, "23/11/22":true, "24/11/22":true, "25/11/22":true, "26/11/22":true, "27/11/22":true, "28/11/22":true, "29/11/22":true, "30/11/22":true, "01/12/22":true, "02/12/22":true, "03/12/22":true, "04/12/22":true, "05/12/22":true, "06/12/22":true, "07/12/22":true, "08/12/22":true, "09/12/22":true, "10/12/22":true, "11/12/22":true, "12/12/22":true}'
        ),
        Space(
            4,
            "test name",
            "test description",
            666,
            "test availability_from",
            "test avaiability_till",
            "{test:calendar}"
            )
            ]

"""
Search for space row by it's id.
"""
def test_search_for_space_by_id(db_connection):
    repository = Space_repository(db_connection)
    db_connection.seed('seeds/db_makers_bnb.sql')

    assert repository.search_by_id(1) == Space(
        1,
        'Cozy Cottage Retreat',
        'Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.',
        120,
        '10/11/22',
        '23/22/22',
        '{"10/11/22":true,"11/11/22":true,"12/11/22":true,"13/11/22":true,"14/11/22":true,"15/11/22":true,"16/11/22":true,"17/11/22":true,"18/11/22":true,"19/11/22":true,"20/11/22":true,"21/11/22":true,"22/11/22":true,"23/11/22":true}'
        )
    
"""
get rendered html dates options by space id
when date is booked displays: not available
# """
# def test_get_html_template_options_of_calendar(db_connection):
#     repository = Space_repository(db_connection)
#     db_connection.seed('seeds/db_makers_bnb.sql')

#     test_space = Space(
#         None,
#         "test name",
#         "test description",
#         666,
#         "test availability_from",
#         "test avaiability_till",
#         '{"15/11/22":true, "16/11/22":true, "17/11/22":false, "18/11/22":true}'
#         )
#     repository.add_space(test_space)

#     assert repository.get_dates_by_id(4) == [
#         '<option value="15/11/22">15/11/22</option>',
#         '<option value="16/11/22">16/11/22</option>',
#         '<option value="17/11/22">not available</option>',
#         '<option value="18/11/22">18/11/22</option>'   
#     ]