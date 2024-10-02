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

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'A2', 'A3', '--allow-draw-family-member'])
    def test_main_draw_family_member(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 6", output)
        self.assertIn("Valid permutations: 2", output)

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'A2', 'A3', '--allow-draw-own-name', '--allow-draw-family-member'])
    def test_main_draw_own_and_family_member(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 6", output)
        self.assertIn("Valid permutations: 6", output)
        
    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'B1', 'C1', '--second-draw'])
    def test_main_second_draw(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations (first draw): 6", output)
        self.assertIn("Valid permutations (first draw): 2", output)
        self.assertIn("Total possibilities (second draw): 12", output)
        self.assertIn("Valid possibilities (second draw): 2", output)
        self.assertIn("Total permutations: 36", output)

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'B1', 'C1', '-V'])
    def test_main_verbose_first(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations: 6", output)
        self.assertIn("Total permutations: [('A1', 'B1', 'C1'), ('A1', 'C1', 'B1'), ('B1', 'A1', 'C1'), ('B1', 'C1', 'A1'), ('C1', 'A1', 'B1'), ('C1', 'B1', 'A1')]", output)
        self.assertIn("Valid permutations: 2", output)
        self.assertIn("Valid permutations: [('B1', 'C1', 'A1'), ('C1', 'A1', 'B1')]", output)

    @patch('sys.stdout', new_callable=StringIO)  # Capture print output
    @patch('sys.argv', new=['main.py', '--people', 'A1', 'B1', 'C1', '--second-draw', '--verbose'])
    def test_main_verbose_second(self, mock_stdout):
        secret_santa.main()
        output = mock_stdout.getvalue()
        self.assertIn("Total permutations (first draw): 6", output)
        self.assertIn("Total permutations (first draw): [('A1', 'B1', 'C1'), ('A1', 'C1', 'B1'), ('B1', 'A1', 'C1'), ('B1', 'C1', 'A1'), ('C1', 'A1', 'B1'), ('C1', 'B1', 'A1')]", output)
        self.assertIn("Valid permutations (first draw): 2", output)
        self.assertIn("Valid permutations (first draw): [('B1', 'C1', 'A1'), ('C1', 'A1', 'B1')]", output)
        self.assertIn("Total possibilities (second draw): 12", output)
        self.assertIn("Valid possibilities (second draw): 2", output)
        self.assertIn("Valid possibilities (second draw): [{('B1', 'C1', 'A1'), ('C1', 'A1', 'B1')}, {('B1', 'C1', 'A1'), ('C1', 'A1', 'B1')}]", output)
        self.assertIn("Total permutations: 36", output)

if __name__ == '__main__':
    unittest.main()