import unittest
import calcul_mental


class testCalculMental(unittest.TestCase):
    def test_reset_doing_great(self):
        for d in range(1, 100):
            self.assertGreater(abs(d), abs(calcul_mental.reset_doing_great(d)))

        for d in range(-100, 0):
            self.assertGreater(abs(d), abs(calcul_mental.reset_doing_great(d)))
