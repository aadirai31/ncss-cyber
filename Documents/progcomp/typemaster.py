# list of all the pokemon types
TYPES = [
    'Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison',
    'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark',
    'Steel', 'Fairy'
    ]

# table of the effectiveness of each attacking type against each defending type
EFFECTIVENESS = {
    'Normal': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 0.5, 'Ghost': 0.0, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Fire': {'Normal': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1.0, 'Grass': 2.0, 'Ice': 2.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 2.0, 'Rock': 0.5, 'Ghost': 1.0, 'Dragon': 0.5, 'Dark': 1.0, 'Steel': 2.0, 'Fairy': 1.0},
    'Water': {'Normal': 1.0, 'Fire': 2.0, 'Water': 0.5, 'Electric': 1.0, 'Grass': 0.5, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 2.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 2.0, 'Ghost': 1.0, 'Dragon': 0.5, 'Dark': 1.0, 'Steel': 1.0, 'Fairy': 1.0},
    'Electric': {'Normal': 1.0, 'Fire': 1.0, 'Water': 2.0, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 0.0, 'Flying': 2.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 0.5, 'Dark': 1.0, 'Steel': 1.0, 'Fairy': 1.0},
    'Grass': {'Normal': 1.0, 'Fire': 0.5, 'Water': 2.0, 'Electric': 1.0, 'Grass': 0.5, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 0.5, 'Ground': 2.0, 'Flying': 0.5, 'Psychic': 1.0, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 1.0, 'Dragon': 0.5, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Ice': {'Normal': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1.0, 'Grass': 2.0, 'Ice': 0.5, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 2.0, 'Flying': 2.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 2.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Fighting': {'Normal': 2.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 2.0, 'Fighting': 1.0, 'Poison': 0.5, 'Ground': 1.0, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 0.0, 'Dragon': 1.0, 'Dark': 2.0, 'Steel': 2.0, 'Fairy': 0.5},
    'Poison': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 2.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 0.5, 'Ground': 0.5, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 0.5, 'Ghost': 0.5, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 0.0, 'Fairy': 2.0},
    'Ground': {'Normal': 1.0, 'Fire': 2.0, 'Water': 1.0, 'Electric': 2.0, 'Grass': 0.5, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 2.0, 'Ground': 1.0, 'Flying': 0.0, 'Psychic': 1.0, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 2.0, 'Fairy': 1.0},
    'Flying': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 0.5, 'Grass': 2.0, 'Ice': 1.0, 'Fighting': 2.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 2.0, 'Rock': 0.5, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Psychic': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 2.0, 'Poison': 2.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 0.5, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 0.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Bug': {'Normal': 1.0, 'Fire': 0.5, 'Water': 1.0, 'Electric': 1.0, 'Grass': 2.0, 'Ice': 1.0, 'Fighting': 0.5, 'Poison': 0.5, 'Ground': 1.0, 'Flying': 0.5, 'Psychic': 2.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 0.5, 'Dragon': 1.0, 'Dark': 2.0, 'Steel': 0.5, 'Fairy': 0.5},
    'Rock': {'Normal': 1.0, 'Fire': 2.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 2.0, 'Fighting': 0.5, 'Poison': 1.0, 'Ground': 0.5, 'Flying': 2.0, 'Psychic': 1.0, 'Bug': 2.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 1.0},
    'Ghost': {'Normal': 0.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 2.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 2.0, 'Dragon': 1.0, 'Dark': 0.5, 'Steel': 1.0, 'Fairy': 1.0},
    'Dragon': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 2.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 0.0},
    'Dark': {'Normal': 1.0, 'Fire': 1.0, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 0.5, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 2.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 2.0, 'Dragon': 1.0, 'Dark': 0.5, 'Steel': 1.0, 'Fairy': 0.5},
    'Steel': {'Normal': 1.0, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 1.0, 'Ice': 2.0, 'Fighting': 1.0, 'Poison': 1.0, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 2.0, 'Ghost': 1.0, 'Dragon': 1.0, 'Dark': 1.0, 'Steel': 0.5, 'Fairy': 2.0},
    'Fairy': {'Normal': 1.0, 'Fire': 0.5, 'Water': 1.0, 'Electric': 1.0, 'Grass': 1.0, 'Ice': 1.0, 'Fighting': 2.0, 'Poison': 0.5, 'Ground': 1.0, 'Flying': 1.0, 'Psychic': 1.0, 'Bug': 1.0, 'Rock': 1.0, 'Ghost': 1.0, 'Dragon': 2.0, 'Dark': 2.0, 'Steel': 0.5, 'Fairy': 1.0}
    }

def damage(attacker, defender):
    """ If 'attacker' pokemon attacks 'defender' pokemon, this method returns
    the damage dealt. For example:

    >>> damage('Water', 'Fire')
    2.0
    >>> damage('Ice', 'Steel')
    0.5
    >>> damage('Normal', 'Ghost')
    0.0
    """
    return EFFECTIVENESS[attacker][defender]

difference = 0

for i, type1 in enumerate(TYPES):
    for n, type2 in enumerate(TYPES):
        difference = float(damage(TYPES[i], TYPES[n])) - float(damage(TYPES[n] - TYPES[i]))
        print(difference)

