import unittest
import calcul_mental


class testCalculMental(unittest.TestCase):

    def test_reset_doing_great(self):
        for d in range(1, 100):
            self.assertGreater(abs(d), abs(calcul_mental.reset_doing_great(d)))

        for d in range(-100, 0):
            self.assertGreater(abs(d), abs(calcul_mental.reset_doing_great(d)))

    def test_reset_all_level_params(self):
        for n in range(-10, 20 + 1):
            for x in range(-10, 20 + 1):
                for d in range(1, 100):
                    new_d, new_x, new_n = calcul_mental.reset_all_level_params(d, n, x)
                    self.assertGreater(abs(d), abs(new_d))
                    self.assertEqual(1, new_n)
                    self.assertEqual(9, new_x)

                for d in range(-100, 0):
                    new_d, new_x, new_n = calcul_mental.reset_all_level_params(d, n, x)
                    self.assertGreater(abs(d), abs(new_d))
                    self.assertEqual(1, new_n)
                    self.assertEqual(9, new_x)
