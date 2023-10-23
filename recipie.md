# Specification
```
Any signed-up user can list a new space.
Users can list multiple spaces.
Users should be able to name their space, provide a short description of the space, and a price per night.
Users should be able to offer a range of dates where their space is available.
Any signed-up user can request to hire any space for one night, and this should be approved by the user that owns that space.
Nights for which a space has already been booked should not be available for users to book that space.
Until a user has confirmed a booking request, that space can still be booked for that night.
```

# Nouns
- space
    - name
    - description
    - price per night

- availability
    - availability of space (available or not)- date
    - booking request

- user
    - username
    - name
    - email
    - password

# Actions
- Sign-up
- Login
- Add a new space (many times)
    - Change availability
- Request to book space
- Approve (confirm) a booking request


# Classes
## User
Properties:
- self.id - INT
- self.username - STRING
- self.name - STRING
- self.password - STRING

## User_repository
| id | username | name | password |
|-----------------|-----------------|-----------------|-----------------|

add_user()
login_valid()

## Space
Properties:
- self.id - INT
- self.name - STRING
- self.description - STRING
- self.prive - FLOAT
- self.availability_from - STRING
- self.availability_to - STRING

## SpaceRepository
| id | name | name | descrition | price | available_from | available to |
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|

- add_space()

## Calendar
- self.start - STRING
- self.end - STRING

## Request
- self.

## RequestRepository
| id | user_id | space_id | date_from | date_to |  |  |
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
add_request()
















# Stretch
- List all spaces listed by users