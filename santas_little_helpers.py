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
    
    for i in range(len(params.people)):
        if not params.allow_draw_own_name and params.people[i] == draw[i]:
            return False
        if params.people[i][0] == draw[i][0] and not params.people[i] == draw[i]:
           return False
    
    return True