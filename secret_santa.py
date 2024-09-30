import itertools

"""Populate the script with all permutations"""
def generate_permutations(people):
    return list(itertools.permutations(people))

"""given a draw, check whether the draw is valid or not according to the rules that are in-use"""
def valid(people, draw):
    for i in range(len(people)):
        if people[i] == draw[i]:
            return False
    return True

def main():
    permutations = generate_permutations(["A1", "A2", "B1", "B2", "C1", "C2", "C3"])
    print(permutations)

if __name__ == "__main__":
    main()