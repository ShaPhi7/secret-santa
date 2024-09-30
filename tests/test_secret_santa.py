import unittest
from secret_santa import generate_permutations

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    def test_generate_permutations(self):
        permutations = generate_permutations(self.people)
        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        draw = ["A2", "B1", "B2", "C1", "C2", "C3", "A1"]
        self.assertTrue(valid(self.people, draw))

    def test_drawing_self_is_invalid(self):
        draw = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]
        self.assertFalse(valid(self.people, draw))

if __name__ == '__main__':
    unittest.main()