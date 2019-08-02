import fractions
import itertools
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import easier_mental


class TestOperationBase(unittest.TestCase):

    def setUp(self):
        self.ob = easier_mental.OperationBase()

    def tearDown(self):
        del self.ob

    def test_init(self):
        self.assertIsInstance(self.ob.pick_list, (list, tuple, set))

        for except_this in self.ob.except_these:
            self.assertNotIn(except_this, self.ob.pick_list)

    def test_get_random_number(self):
        vut = self.ob.get_random_number()

        self.assertIsInstance(vut, int)
        self.assertGreaterEqual(vut, self.ob.min_number)
        self.assertLessEqual(vut, self.ob.max_number)


class TestCancelFraction(unittest.TestCase):

    def setUp(self):
        self.ob = easier_mental.CancelFraction()

    def tearDown(self):
        del self.ob

    def test_get_question(self):
        n_repeat = 1000

        for _ in itertools.repeat(None, n_repeat):
            xy = self.ob.get_question()

            self.assertEqual(2, len(xy))

            self.assertNotEqual(xy[0], xy[1])

    def test_get_question_string(self):
        result = self.ob.get_question_string()

        self.assertIsInstance(result, str)

        num_str, den_str = result.split('/')

        msg = '\n'.join([
            f"\nresult = {result}",
            f"question = {self.ob.question}"
        ])

        self.assertEqual(self.ob.question[0], int(num_str), msg=msg)
        self.assertEqual(self.ob.question[1], int(den_str), msg=msg)

    def test_eval_answer_no_space(self):
        num = 3
        den = 4
        input_str = f"{num}/{den}"

        result = self.ob.eval_answer(input_str)
        expected = fractions.Fraction(num, den)

        self.assertEqual(expected, result)

    def test_eval_answer_front_space(self):
        num = 3
        den = 4
        input_str = f"{num} /{den}"

        result = self.ob.eval_answer(input_str)
        expected = fractions.Fraction(num, den)

        self.assertEqual(expected, result)

    def test_eval_answer_both_spaces(self):
        num = 3
        den = 4
        input_str = f"{num} / {den}"

        result = self.ob.eval_answer(input_str)
        expected = fractions.Fraction(num, den)

        self.assertEqual(expected, result)

    def test_eval_answer_rear_space(self):
        num = 3
        den = 4
        input_str = f"{num}/ {den}"

        result = self.ob.eval_answer(input_str)
        expected = fractions.Fraction(num, den)

        self.assertEqual(expected, result)


if "__main__" == __name__:
    unittest.main()
