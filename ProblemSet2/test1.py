import unittest
import ps2


class Test_ps2p1(unittest.TestCase):
    def test_ps2p1(self):
        (paid, balance) = ps2.ps2p1(4842.00, 0.2, 0.04)
        self.assertAlmostEqual(paid, 2040.64, delta=.5)
        self.assertAlmostEqual(balance, 3617.62, delta=.5)

    def test_ps2p2(self):
        self.assertAlmostEqual(ps2.ps2p2(3329, 0.2), 310)
        self.assertAlmostEqual(ps2.ps2p2(4773, 0.2), 440)
        self.assertAlmostEqual(ps2.ps2p2(3926, 0.2), 360)
        self.assertAlmostEqual(ps2.ps2p2(0, 0.2), 0)

    def test_ps2p3(self):
        self.assertAlmostEqual(ps2.ps2p3(320000, 0.20), 29157.09, places=2)
        self.assertAlmostEqual(ps2.ps2p3(999999, 0.18), 90325.03, places=2)


if __name__ == '__main__':
    unittest.main()
