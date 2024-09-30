import unittest
import secret_santa

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.people = ["A1", "A2", "B1"]

    def test_generate_permutations(self):
        people = ["A1", "A2", "B1"]
        perms = secret_santa.generate_permutations(people)
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
        self.people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]
        permutations = secret_santa.generate_permutations(self.people)
        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        draw = ["A2", "B1", "A1"]
        self.assertTrue(secret_santa.valid(self.people, draw))

    def test_drawing_self_is_invalid(self):
        draw = ["A1", "B1", "A2"]
        self.assertFalse(secret_santa.valid(self.people, draw))

    def test_count_valid_permutations(self):
        permutations = secret_santa.generate_permutations(self.people)
        expected_valid_count = 2 # ('A2', 'B1', 'A1') and ('B1', 'A1', 'A2')
        
        count = secret_santa.count_valid(self.people, permutations)
        
        self.assertEqual(count, expected_valid_count) 

if __name__ == '__main__':
    unittest.main()