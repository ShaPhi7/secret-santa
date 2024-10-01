import itertools

"""Populate the script with all permutations"""
def generate_permutations(people):
    return list(itertools.permutations(people))

"""Cycle through all of the permutations, returning the total number of valid permutations"""
def count_valid(params, permutations):
    valid_permutations = [p for p in permutations if validate_draw(params, p)]
    return len(valid_permutations)

"""given a draw, check whether the draw is valid or not according to the rules that are in-use"""
def validate_draw(params, draw):
    people = params.people

    for i in range(len(people)):
        person = people[i]
        drawn_name = draw[i]

        if not params.allow_draw_own_name and samePerson(person, drawn_name):
            return False
        if not params.allow_draw_family_member and familyMember(person, drawn_name):
            return False
        
    return True

def samePerson(person, other):
    return person == other

def familyMember(person, other):
    return person[0] == other[0] and not samePerson(person, other)