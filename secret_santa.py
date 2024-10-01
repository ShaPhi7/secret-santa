import argparse
from santas_little_helpers import generate_permutations, count_valid

def main():
    parser = argparse.ArgumentParser(description='Given a list of players, the program will compute the total number of valid permutations given the ruleset required.')
    parser.add_argument(
        '--people', 
        nargs='+', 
        default=["A1", "A2", "B1", "B2", "C1", "C2", "C3"],
        help='Each person hould be of the from A#, where the first letter indicates the family they belong to. (e.g., A1 A2 B1 C1)'
    )

    args = parser.parse_args()

    permutations = generate_permutations(args.people)
    valid_count = count_valid(args.people, permutations)

    print(f"Total permutations: {len(permutations)}")
    print(f"Valid permutations: {valid_count}")

if __name__ == "__main__":
    main()