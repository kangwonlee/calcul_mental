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
