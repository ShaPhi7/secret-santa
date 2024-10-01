from io import StringIO
import unittest
from unittest.mock import patch
import secret_santa

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.three_people = ["A1", "A2", "B1"]
        self.four_people = ["A1", "A2", "B1", "C1"]
        self.seven_people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'A2', 'B3', 'B4'])
    def test_main_with_people(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 24", output)
        self.assertIn("Valid permutations: 4", output)

    def test_generate_permutations(self):
        perms = secret_santa.generate_permutations(self.three_people)
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
        permutations = secret_santa.generate_permutations(self.seven_people)
        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        draw = ["C1", "B1", "A1", "A2"]
        self.assertTrue(secret_santa.valid(self.four_people, draw))

    def test_drawing_self_is_invalid(self):
        draw = ["A1", "B1", "A2"]
        self.assertFalse(secret_santa.valid(self.three_people, draw))

    def test_drawing_family_is_invalid(self):
        draw = ["A2", "B1", "C1", "A1"] # A1 has drawn A2
        self.assertFalse(secret_santa.valid(self.four_people, draw))

    def test_count_valid_permutations(self):
        permutations = secret_santa.generate_permutations(self.four_people)
        expected_valid_count = 4 # ('A2', 'B1', 'A1') and ('B1', 'A1', 'A2')
        
        count = secret_santa.count_valid(self.four_people, permutations)
        
        self.assertEqual(count, expected_valid_count) 

if __name__ == '__main__':
    unittest.main()