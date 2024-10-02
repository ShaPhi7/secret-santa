import itertools

def draw(params):
    
    permutations = generate_permutations(params.people)
    
    valid_permutations = compute_valid(params, permutations)
    params.previous_draw = valid_permutations
    verbose = params.verbose
    if params.second_draw:
        fully_valid_permutations = compute_valid(params, permutations)
        log("Total permutations (first draw)", permutations, verbose)
        log("Valid permutations (first draw)", valid_permutations, verbose)
        print(f"Total possibilities (second draw): {len(permutations)*len(valid_permutations)}")
        log("Valid possibilities (second draw)", fully_valid_permutations, verbose)
        print(f"Total permutations: {len(permutations)**2}")
    else:
        log("Total permutations", permutations, verbose)
        log("Valid permutations", valid_permutations, verbose)

def log(label, permutations, verbose):
    print(f"{label}: {len(permutations)}")
    print(f"{label}: {permutations}\n" if verbose else "", end = "")

"""Populate the script with all permutations"""
def generate_permutations(people):
    return list(itertools.permutations(people))

"""Cycle through all of the permutations, returning the total number of valid permutations"""
def compute_valid(params, permutations):
    
    valid_permutations = []

    if params.previous_draw:
        for prev_draw in params.previous_draw:
            for p in permutations:
                if validate_draw(params, p, prev_draw):
                    valid_permutations.append(set((tuple(p), tuple(prev_draw))))
    else:
        valid_permutations = [p for p in permutations if validate_draw(params, p)]
    return valid_permutations

"""given a draw, check whether the draw is valid or not according to the rules that are in-use"""
def validate_draw(params, draw, prev_draw=None):
    people = params.people

    for i in range(len(people)):
        person = people[i]
        drawn_name = draw[i]

        if not params.allow_draw_own_name and samePerson(person, drawn_name):
            return False
        if not params.allow_draw_family_member and familyMember(person, drawn_name):
            return False
        if prev_draw and sameAsPreviousDraw(drawn_name, prev_draw[i]):
            return False
        
    return True

def samePerson(person, other):
    return person == other

def familyMember(person, other):
    return person[0] == other[0] and not samePerson(person, other)

def sameAsPreviousDraw(this_draw, prev_draw):
    return this_draw == prev_draw