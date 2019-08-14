import fractions
import itertools
import os
import re
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
        n_repeat = 5

        for _ in itertools.repeat(None, n_repeat):
            xy = self.ob.get_question()

            self.assertEqual(2, len(xy))

            self.assertNotEqual(xy[0], xy[1])

            msg_range = ("\n"
                f"{self.ob.min_number ** 2} <= xy = {xy} <= {self.ob.max_number ** 2}"
                )

            self.assertLessEqual(xy[0], self.ob.max_number ** 2, msg=msg_range)

            self.assertGreaterEqual(xy[0], self.ob.min_number ** 2, msg=msg_range)

            self.assertLessEqual(xy[1], self.ob.max_number ** 2, msg=msg_range)

            self.assertGreaterEqual(xy[1], self.ob.min_number ** 2, msg=msg_range)

    def test_get_question_string(self):
        result = self.ob.get_question_string()

        self.assertIsInstance(result, str)

        found = re.findall (r"\s+(\d+)\s+-+\s+(\d+)\s", result, re.M)

        self.assertTrue(found, f"\nresult = {result}\nfound = {found}")

        num_str, den_str = found[0]

        msg = '\n'.join([
            f"\nresult = {repr(result)}",
            f"question = {self.ob.question}"
        ])

        self.assertEqual(self.ob.question[0], int(num_str), msg=msg)
        self.assertEqual(self.ob.question[1], int(den_str), msg=msg)

    def test_eval_answer_no_space(self):
        num = 3
        den = 4
        input_str = f"{num}/{den}"

        result = self.ob.eval_answer(input_str)

        self.assertIsInstance(result, (list, tuple))

        expected_fraction = fractions.Fraction(num, den)
        expected = expected_fraction.numerator, expected_fraction.denominator,

        self.assertSequenceEqual(expected, result)

    def test_eval_answer_front_space(self):
        num = 3
        den = 4
        input_str = f"{num} /{den}"

        result = self.ob.eval_answer(input_str)

        self.assertIsInstance(result, (list, tuple))

        expected_fraction = fractions.Fraction(num, den)
        expected = expected_fraction.numerator, expected_fraction.denominator,

        self.assertSequenceEqual(expected, result)

    def test_eval_answer_both_spaces(self):
        num = 3
        den = 4
        input_str = f"{num} / {den}"

        result = self.ob.eval_answer(input_str)

        self.assertIsInstance(result, (list, tuple))

        expected_fraction = fractions.Fraction(num, den)
        expected = expected_fraction.numerator, expected_fraction.denominator,

        self.assertSequenceEqual(expected, result)

    def test_eval_answer_rear_space(self):
        num = 3
        den = 4
        input_str = f"{num}/ {den}"

        result = self.ob.eval_answer(input_str)

        self.assertIsInstance(result, (list, tuple))

        expected_fraction = fractions.Fraction(num, den)
        expected = expected_fraction.numerator, expected_fraction.denominator,

        self.assertSequenceEqual(expected, result)

    def test_is_answer_correct_correct(self):
        num = 3
        den = 4
        pick = 5

        self.ob.question = (num * pick, den * pick)

        correct_answer = fractions.Fraction(num, den)
        correct_answer_str = str(correct_answer)

        result = self.ob.is_answer_correct(correct_answer_str)

        self.assertTrue(result)

    def test_is_answer_correct_incorrect_den(self):
        num = 3
        den = 4
        pick = 5

        self.ob.question = (num * pick, den * pick)

        incorrect_answer = fractions.Fraction(num, den + 1)
        incorrect_answer_str = str(incorrect_answer)

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)

    def test_is_answer_correct_incorrect_num_den(self):
        num = 3
        den = 4
        pick = 5

        self.ob.question = (num * pick, den * pick)

        incorrect_answer = fractions.Fraction(num + 1, den + 1)
        incorrect_answer_str = str(incorrect_answer)

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)

    def test_is_answer_correct_incorrect_num_den_multiplied(self):
        num = 3
        den = 4
        pick = 5

        self.ob.question = (num * pick, den * pick)

        incorrect_answer_str = f"{num * 2} / {den * 2}"

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)

    def test_is_answer_correct_incorrect_num(self):
        num = 3
        den = 4
        pick = 5

        self.ob.question = (num * pick, den * pick)

        incorrect_answer = fractions.Fraction(num - 1, den)
        incorrect_answer_str = str(incorrect_answer)

        self.assertIn('/', incorrect_answer_str)

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)

    def test_is_answer_correct_just_enter(self):
        null_str = f""

        result = self.ob.is_answer_correct(null_str)

        self.assertFalse(result)


class TestMul(unittest.TestCase):

    def setUp(self):
        self.ob = easier_mental.Mul()

    def tearDown(self):
        del self.ob

    def test_get_question_mul(self):
        n_repeat = 5

        history = set()

        for _ in itertools.repeat(None, n_repeat):
            xy = tuple(self.ob.get_question())

            self.assertEqual(2, len(xy))

            history.add(xy)

        self.assertGreaterEqual(len(history), n_repeat - 1)

    def test_get_question_string(self):
        result = self.ob.get_question_string()

        self.assertIsInstance(result, str)

        num_str, den_str = result.split('*')

        msg = '\n'.join([
            f"\nresult = {result}",
            f"question = {self.ob.question}"
        ])

        self.assertEqual(self.ob.question[0], int(num_str), msg=msg)
        self.assertEqual(self.ob.question[1], int(den_str), msg=msg)

    def test_eval_answer_no_space(self):
        num = 3
        input_str = f"{num}"

        result = self.ob.eval_answer(input_str)
        expected = num

        self.assertEqual(expected, result)

    def test_eval_answer_front_space(self):
        num = 3
        input_str = f" {num}"

        result = self.ob.eval_answer(input_str)
        expected = num

        self.assertEqual(expected, result)

    def test_is_answer_correct_just_enter(self):
        null_str = f""

        result = self.ob.is_answer_correct(null_str)

        self.assertFalse(result)

    def test_is_answer_correct_correct(self):
        a = 3
        b = 4

        self.ob.question = (a, b)

        correct_answer = a * b
        correct_answer_str = str(correct_answer)

        result = self.ob.is_answer_correct(correct_answer_str)

        self.assertTrue(result)

    def test_is_answer_correct_incorrect_den(self):
        a = 3
        b = 4

        self.ob.question = (a, b)

        incorrect_answer = a * (b + 1)
        incorrect_answer_str = str(incorrect_answer)

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)


class TestDiv(unittest.TestCase):

    def setUp(self):
        self.ob = easier_mental.Div()

    def tearDown(self):
        del self.ob

    def test_get_question(self):
        n_repeat = 1000

        for _ in itertools.repeat(None, n_repeat):
            xy = self.ob.get_question()

            self.assertEqual(2, len(xy))

    def test_get_question_div(self):
        n_repeat = 5

        history = set()

        for _ in itertools.repeat(None, n_repeat):
            xy = tuple(self.ob.get_question())

            self.assertEqual(2, len(xy))

            self.assertNotIn(xy, history)

            history.add(xy)

    def test_get_question_string(self):
        result = self.ob.get_question_string()

        self.assertIsInstance(result, str)

        num_str, den_str = result.split('/')

        msg = '\n'.join([
            f"\nresult = {result}",
            f"question = {self.ob.question}"
        ])

        self.assertEqual(self.ob.question[0] * self.ob.question[1], int(num_str), msg=msg)
        self.assertEqual(self.ob.question[1], int(den_str), msg=msg)

    def test_eval_answer_no_space(self):
        num = 3
        input_str = f"{num}"

        result = self.ob.eval_answer(input_str)
        expected = num

        self.assertEqual(expected, result)

    def test_eval_answer_front_space(self):
        num = 3
        input_str = f" {num}"

        result = self.ob.eval_answer(input_str)
        expected = num

        self.assertEqual(expected, result)

    def test_is_answer_correct_correct(self):
        a = 3
        b = 4

        self.ob.question = (a, b)

        correct_answer = a
        correct_answer_str = str(correct_answer)

        result = self.ob.is_answer_correct(correct_answer_str)

        self.assertTrue(result)

    def test_is_answer_correct_incorrect_den(self):
        a = 3
        b = 4

        self.ob.question = (a, b)

        incorrect_answer = (a + 1)
        incorrect_answer_str = str(incorrect_answer)

        result = self.ob.is_answer_correct(incorrect_answer_str)

        self.assertFalse(result)

    def test_is_answer_correct_just_enter(self):
        null_str = f""

        result = self.ob.is_answer_correct(null_str)

        self.assertFalse(result)


if "__main__" == __name__:
    unittest.main()
