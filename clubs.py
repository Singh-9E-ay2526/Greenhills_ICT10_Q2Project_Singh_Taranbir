# School Club Members: sets and set operators
from pyscript import document

# one set for each grade
grade_7 = {'Peter Parker', 'Gwen Stacy', 'Flash Thompson', 'Betty Brant'}
grade_8 = {'Miles Morales', 'Ned Leeds', 'Ganke Lee'}
grade_9 = {'Mary Jane Watson', 'Harry Osborn', 'Liz Allan', 'Cindy Moon'}
grade_10 = {'May Parker', 'Miguel Ohara', 'Jessica Drew'}

# master set: | combines the sets (union)
master_set = grade_7 | grade_8 | grade_9 | grade_10


def add_member(e):
    # use the master_set that is outside the function
    global master_set

    # get the first name and last name
    first = document.getElementById('first_name').value.strip()
    last = document.getElementById('last_name').value.strip()
    full_name = f'{first} {last}'.title().strip()

    # new member set (- removes the empty name if nothing was typed)
    new_member = {full_name} - {''}

    # add the new member to the master set
    master_set = master_set | new_member

    # names in alphabetical order, one per line
    names = '<br>'.join(sorted(master_set))

    # show the list and the total
    document.getElementById('result').innerHTML = (
        'All members:<br>'
        f'{names}<br>'
        f'Total members: {len(master_set)}'
    )