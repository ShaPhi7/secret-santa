import unittest
import secret_santa

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    def test_generate_permutations(self):
        permutations = secret_santa.generate_permutations(self.people)
        self.assertEqual(len(permutations), 5040) #7!

    def test_valid_draw(self):
        draw = ["A2", "B1", "B2", "C1", "C2", "C3", "A1"]
        self.assertTrue(secret_santa.valid(self.people, draw))

    def test_drawing_self_is_invalid(self):
        draw = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]
        self.assertFalse(secret_santa.valid(self.people, draw))

if __name__ == '__main__':
    unittest.main()