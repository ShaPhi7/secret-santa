import unittest
from secret_santa import generate_permutations

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        self.people = ["A1", "A2", "B1", "B2", "C1", "C2", "C3"]

    def test_generate_permutations(self):
        permutations = generate_permutations(self.people)
        self.assertEqual(len(permutations), 5040); #7!

if __name__ == '__main__':
    unittest.main()