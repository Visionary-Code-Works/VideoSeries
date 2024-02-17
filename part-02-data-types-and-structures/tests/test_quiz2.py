# test_quiz2.py

import unittest
from unittest.mock import patch
from ..quizzes import load_answers, run_quiz


class TestQuiz(unittest.TestCase):
    def test_load_answers(self):
        """Test that answers are correctly loaded from a file."""
        answers = load_answers("part-02-data-types-and-structures/quizzes/answers.json")
        self.assertIsInstance(answers, dict)
        self.assertTrue("1" in answers)
        self.assertEqual(answers["1"], 2)

    @patch('builtins.input', side_effect=["1", "2", "3", "4", "1", "2", "1", "1", "1", "3"])
    def test_run_quiz(self, mocked_input):
        """Test running the quiz with predetermined answers."""
        # Assuming your answers.json matches the correct answers exactly,
        # and you don't shuffle the questions or answers for this test.
        answers = load_answers("part-02-data-types-and-structures/quizzes/answers.json")
        with patch('builtins.print') as mocked_print:
            run_quiz(run_quiz, answers)
            self.assertIn("Your final score is 10/10", str(mocked_print.call_args_list[-1]))

# Additional tests can be created for other parts of the code as needed.

if __name__ == '__main__':
    unittest.main()
