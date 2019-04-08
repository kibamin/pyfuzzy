import unittest
from pyfuzzy.mf import pimf


class PiMFTestCase(unittest.TestCase):
    def test_pimf_membership_function(self):
        self.assertEqual(pimf.pimf(0.0, [1.0, 4.0, 5.0, 10.0]), 0.0)
        self.assertEqual(pimf.pimf(1.0, [1.0, 4.0, 5.0, 10.0]), 0.0)
        self.assertEqual(pimf.pimf(4.0, [1.0, 4.0, 5.0, 10.0]), 1.0)
        self.assertEqual(pimf.pimf(5.0, [1.0, 4.0, 5.0, 10.0]), 1.0)
        self.assertEqual(pimf.pimf(10.0, [1.0, 4.0, 5.0, 10.0]), 0.0)
        self.assertEqual(pimf.pimf(3.0, [5.0, 10.0, 15.0, 20.0]), 0.0)
        self.assertEqual(pimf.pimf(5.0, [5.0, 10.0, 15.0, 20.0]), 0.0)
        self.assertEqual(pimf.pimf(10.0, [5.0, 10.0, 15.0, 20.0]), 1.0)
        self.assertEqual(pimf.pimf(21.0, [5.0, 10.0, 15.0, 20.0]), 0.0)
        self.assertEqual(pimf.pimf(15.0, [5.0, 10.0, 15.0, 20.0]), 1.0)


if __name__ == '__main__':
    unittest.main()

