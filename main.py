# Homepage: Spiderman-Club member checker
from pyscript import display, document

# list of club members
club = [
    'Peter Parker', 'Miles Morales', 'Gwen Stacy', 'Mary Jane Watson',
    'Ned Leeds', 'Harry Osborn', 'May Parker', 'Miguel Ohara'
]


def view_user(e):
    # clear the old message
    document.getElementById('result').innerHTML = ''

    # get the first name and last name
    first = document.getElementById('first_name').value.strip()
    last = document.getElementById('last_name').value.strip()
    full_name = f'{first} {last}'.title()

    # True if the name is in the club, False if not
    is_member = full_name in club

    # message 0 is for False, message 1 is for True
    messages = (
        f'Sorry {full_name}, your name is not on the list.',
        f'Congratulations {full_name}! You are now part of the club.'
    )

    # show the message
    display(messages[is_member], target='result')