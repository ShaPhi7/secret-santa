import argparse
from santas_little_helpers import generate_permutations, count_valid

def main():
    parser = argparse.ArgumentParser(description='Given a list of players, the program will compute the total number of valid permutations given the ruleset required.')
    parser.add_argument(
        '--people', 
        nargs='+', 
        default=["A1", "A2", "B1", "B2", "C1", "C2", "C3"],
        help='Each person hould be of the from A#, where the first letter indicates the family they belong to. (e.g., A1 A2 B1 C1).'
    )
    parser.add_argument(
        '--allow-draw-own-name', 
        action='store_true',
        help='Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).'
    )
    parser.add_argument(
        '--allow-draw-family-member', 
        action='store_true',
        help='Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).'
    )

    args = parser.parse_args()

    permutations = generate_permutations(args.people)

    params = Parameters(args.people,
                        args.allow_draw_own_name,
                        args.allow_draw_family_member)

    valid_count = count_valid(params, permutations)

    print(f"Total permutations: {len(permutations)}")
    print(f"Valid permutations: {valid_count}")

class Parameters:
    def __init__(self, people,
                 allow_draw_own_name=False,
                 allow_draw_family_member=False):
        self.people = people
        self.allow_draw_own_name = allow_draw_own_name
        self.allow_draw_family_member = allow_draw_family_member

if __name__ == "__main__":
    main()