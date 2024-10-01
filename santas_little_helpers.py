import itertools

"""Populate the script with all permutations"""
def generate_permutations(people):
    return list(itertools.permutations(people))

"""Cycle through all of the permutations, returning the total number of valid permutations"""
def count_valid(people, permutations):
    valid_permutations = [p for p in permutations if valid(people, p)]
    return len(valid_permutations)

"""given a draw, check whether the draw is valid or not according to the rules that are in-use"""
def valid(people, draw):
    for i in range(len(people)):
        if people[i] == draw[i]:
            return False
        if people[i][0] == draw[i][0]:
            return False
    
    return True