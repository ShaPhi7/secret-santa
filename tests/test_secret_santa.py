from io import StringIO
import unittest
from unittest.mock import patch
import secret_santa

class TestSecretSanta(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'A2', 'B3', 'B4'])
    def test_main_people(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 24", output)
        self.assertIn("Valid permutations: 4", output)

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'B1', 'C1', '--allow-draw-own-name'])
    def test_main_draw_own_name(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 6", output)
        self.assertIn("Valid permutations: 6", output)

if __name__ == '__main__':
    unittest.main()