import unittest
from santas_little_helpers import validate_draw, generate_permutations, compute_valid, samePerson, familyMember
from secret_santa import Parameters

class TestSantasLittleHelpers(unittest.TestCase):

    def setUp(self):
        self.three_people = ["A1", "B1", "C1"]
        self.four_people = ["A1", "A2", "B1", "C1"]
        self.seven_people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    def test_generate_permutations(self):
        perms = generate_permutations(self.three_people)
        expected_perms = [
            ('A1', 'B1', 'C1'),
            ('A1', 'C1', 'B1'),
            ('B1', 'A1', 'C1'),
            ('B1', 'C1', 'A1'),
            ('C1', 'A1', 'B1'),
            ('C1', 'B1', 'A1')
        ]
        
        self.assertEqual(perms, expected_perms)

    def test_generate_permutations_count(self):
        permutations = generate_permutations(self.seven_people)

        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        params = Parameters(people=self.four_people)
        draw = ["C1", "B1", "A1", "A2"]

        self.assertTrue(validate_draw(params, draw))

    def test_drawing_self_is_invalid(self):
        params = Parameters(people=self.three_people)
        draw = ["A1", "C1", "B1"]

        self.assertFalse(validate_draw(params, draw))

    def test_drawing_family_is_invalid(self):
        params = Parameters(people=self.four_people)
        draw = ["A2", "B1", "C1", "A1"] # A1 has drawn A2

        self.assertFalse(validate_draw(params, draw))

    def test_same_name_as_prev_draw_invalid(self):
        previous_draw = ["B1", "C1", "A1"]
        draw = ["B1", "C1", "A1"]
        params = Parameters(people=self.three_people, previous_draw=previous_draw)
        
        self.assertFalse(validate_draw(params, draw, previous_draw))

    def test_different_name_as_prev_draw_valid(self):
        previous_draw = ["B1", "C1", "A1"]
        draw = ["C1", "A1", "B1"]
        params = Parameters(people=self.three_people, previous_draw=previous_draw)
        
        self.assertTrue(validate_draw(params, draw, previous_draw))

    def test_count_valid_permutations(self):
        params = Parameters(people=self.four_people)
        permutations = generate_permutations(params.people)

        expected_valid_count = 4
        valid = compute_valid(params, permutations)
        
        self.assertEqual(len(valid), expected_valid_count) 

    def test_same_person(self):
        person = "A1"
        other = "A1"

        self.assertTrue(samePerson(person, other))

    def test_not_same_person(self):
        person = "A1"
        other = "A2"

        self.assertFalse(samePerson(person, other))

    def test_family_member(self):
        person = "A1"
        other = "A2"
        
        self.assertTrue(familyMember(person, other))

    def test_not_family_member(self):
        person = "A1"
        other = "B1"

        self.assertFalse(familyMember(person, other))