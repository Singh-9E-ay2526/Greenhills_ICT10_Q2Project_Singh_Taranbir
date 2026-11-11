# Element Checker: non-metals
from pyscript import document

# list of symbols
symbols = [
    'H', 'He', 'C', 'N', 'O', 'F', 'Ne', 'P', 'S',
    'Cl', 'Ar', 'Se', 'Br', 'Kr', 'I', 'Xe', 'Rn'
]

# list of tuples: (name, atomic number, atomic mass)
info = [
    ('Hydrogen', 1, 1.008), ('Helium', 2, 4.0026),
    ('Carbon', 6, 12.011), ('Nitrogen', 7, 14.007),
    ('Oxygen', 8, 15.999), ('Fluorine', 9, 18.998),
    ('Neon', 10, 20.180), ('Phosphorus', 15, 30.974),
    ('Sulfur', 16, 32.06), ('Chlorine', 17, 35.45),
    ('Argon', 18, 39.948), ('Selenium', 34, 78.971),
    ('Bromine', 35, 79.904), ('Krypton', 36, 83.798),
    ('Iodine', 53, 126.904), ('Xenon', 54, 131.293),
    ('Radon', 86, 222)
]

# dictionary: symbol -> (name, number, mass)
non_metals = dict(zip(symbols, info))


def search_element(e):
    # get the symbol typed by the user
    typed = document.getElementById('symbol').value.strip()
    symbol = typed.capitalize()

    # get the details (empty if the symbol is not found)
    name, number, mass = non_metals.get(symbol, ('', '', ''))

    # True if the symbol is in the dictionary, False if not
    found = symbol in non_metals

    # message 0 is for False, message 1 is for True
    messages = (
        f'{typed} does not exist in the non-metals list.',
        f'Element Symbol: {symbol}<br>'
        f'Element Name: {name}<br>'
        f'Atomic Number: {number}<br>'
        f'Atomic Mass: {mass}'
    )

    # show the message
    document.getElementById('output').innerHTML = messages[found]