import itertools

"""Populate the script with all permutations"""
def generate_permutations(people):
    return list(itertools.permutations(people))

"""given a draw, check whether the draw is valid or not according to the rules that are in-use"""
def valid(people, draw):
    for i in range(len(people)):
        if people[i] == draw[i]:
            return False
        if people[i][0] == draw[i][0]:
            return False
    
    return True

def count_valid(people, permutations):
    valid_permutations = [p for p in permutations if valid(people, p)]
    return len(valid_permutations)

def main():
    people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]
    permutations = generate_permutations(people)

    valid_count = count_valid(people, permutations)

    print(f"Total permutations: {len(permutations)}")
    print(f"Valid permutations: {valid_count}")

if __name__ == "__main__":
    main()