import unittest
from santas_little_helpers import valid, generate_permutations, count_valid

class TestSantasLittleHelpers(unittest.TestCase):

    def setUp(self):
        self.three_people = ["A1", "A2", "B1"]
        self.four_people = ["A1", "A2", "B1", "C1"]
        self.seven_people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    def test_generate_permutations(self):
        perms = generate_permutations(self.three_people)
        expected_perms = [
            ('A1', 'A2', 'B1'),
            ('A1', 'B1', 'A2'),
            ('A2', 'A1', 'B1'),
            ('A2', 'B1', 'A1'),
            ('B1', 'A1', 'A2'),
            ('B1', 'A2', 'A1')
        ]
        self.assertEqual(perms, expected_perms)

    def test_generate_permutations_count(self):
        permutations = generate_permutations(self.seven_people)
        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        draw = ["C1", "B1", "A1", "A2"]
        self.assertTrue(valid(self.four_people, draw))

    def test_drawing_self_is_invalid(self):
        draw = ["A1", "B1", "A2"]
        self.assertFalse(valid(self.three_people, draw))

    def test_drawing_family_is_invalid(self):
        draw = ["A2", "B1", "C1", "A1"] # A1 has drawn A2
        self.assertFalse(valid(self.four_people, draw))

    def test_count_valid_permutations(self):
        permutations = generate_permutations(self.four_people)
        expected_valid_count = 4 # ('A2', 'B1', 'A1') and ('B1', 'A1', 'A2')
        
        count = count_valid(self.four_people, permutations)
        
        self.assertEqual(count, expected_valid_count) 
