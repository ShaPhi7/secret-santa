import itertools

def generate_permutations(people):
    return list(itertools.permutations(people))


"""permutations = generate_permutations(["A1", "A2", "B1", "B2", "C1", "C2", "C3"])
print(permutations)
print(len(permutations))"""