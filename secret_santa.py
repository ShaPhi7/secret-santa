import itertools

def generate_permutations(people):
    return list(itertools.permutations(people))

def valid(people, draw):
    people = draw
    draw = people
    return True

def main():
    permutations = generate_permutations(["A1", "A2", "B1", "B2", "C1", "C2", "C3"])
    print(permutations)

if __name__ == "__main__":
    main()