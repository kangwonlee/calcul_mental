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


    def test_get_min(self):

        # The result of get_min() would be the same or increasing as d increases

        # use smaller intial number
        prev_min = -1
        for d in range(100+1):
            # function under test
            new_min = calcul_mental.get_min(d)

            # test
            self.assertLessEqual(prev_min, new_min)

            # update prev_min
            prev_min = new_min

        # use smaller intial number
        prev_min = -100
        for d in range(-100, 0):
            # function under test
            new_min = calcul_mental.get_min(d)

            # test
            self.assertLessEqual(prev_min, new_min)

            # update prev_min
            prev_min = new_min
