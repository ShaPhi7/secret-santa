import argparse
from santas_little_helpers import draw

def main():
    parser = argparse.ArgumentParser(description='Given a list of players, the program will compute the total number of valid permutations given the ruleset required.')
    parser.add_argument(
        '-p', '-P', '--people', 
        nargs='+', 
        default=("A1", "A2", "B1", "B2", "C1", "C2", "C3"),
        help='Each person hould be of the from A#, where the first letter indicates the family they belong to. (e.g., A1 A2 B1 C1).'
    )
    parser.add_argument(
        '-O', '--allow-draw-own-name',
        action='store_true',
        help='Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).'
    )
    parser.add_argument(
        '-F', '--allow-draw-family-member', 
        action='store_true',
        help='Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).'
    )
    parser.add_argument(
        '-2', '--second-draw',
        action='store_true',
        help='Permutations shown for a second draw with the extra rule that nobody can have the same name they drew in the first draw (the results of which are not known, other than the fact that they were valid).'
    )
    parser.add_argument(
        '-V', '--verbose',
        action='store_true',
        help='Prints out the permutations, in addition to the counts.'
    )

    args = parser.parse_args()

    params = Parameters(args.people,
                        args.allow_draw_own_name,
                        args.allow_draw_family_member,
                        args.second_draw,
                        args.verbose)
    print(params)
    draw(params)

class Parameters:
    def __init__(self, people,
                 allow_draw_own_name=False,
                 allow_draw_family_member=False,
                 second_draw=False,
                 verbose=False,
                 previous_draw=None):
        self.people = people
        self.allow_draw_own_name = allow_draw_own_name
        self.allow_draw_family_member = allow_draw_family_member
        self.second_draw = second_draw
        self.verbose = verbose
        self.previous_draw = previous_draw
    def __str__(self):
        return (f"Parameters:\n"
                f"  People: {self.people}\n"
                f"  Allow draw own name: {self.allow_draw_own_name}\n"
                f"  Allow draw family member: {self.allow_draw_family_member}\n"
                f"  Second draw: {self.second_draw}\n"
                f"  Verbose: {self.verbose}\n")
if __name__ == "__main__":
    main()