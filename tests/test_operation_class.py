import itertools
import unittest

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
