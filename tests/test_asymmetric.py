import unittest

from uls import compression_asymmetric

h = 0.6
b = 0.3
a1 = a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43
f_ck = 30


class TestAsymmetric(unittest.TestCase):

    def test_5_10(self):
        """
            Test asymmetric reinforcement for N=5 kN, M=10 kNm
        """

        n_ed = 5.0
        m_ed = 10.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 0.219840, 1)
        self.assertAlmostEqual(as2, 1.80000, 1)

    def test_100_100(self):
        """
            Test asymmetric reinforcement for N=100 kN, M=100 kNm
        """

        n_ed = 100.0
        m_ed = 100.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 3.102643, 2)
        self.assertAlmostEqual(as2, 1.80000, 2)

    def test_1000_500(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=500 kNm
        """

        n_ed = 1000.0
        m_ed = 500.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 17.95217, 2)
        self.assertAlmostEqual(as2, 1.80000, 2)

    def test_1000_750(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 1000.00
        m_ed = 750.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 29.879164, 2)
        self.assertAlmostEqual(as2, 12.74813, 2)

    def test_3500_500(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 500.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 4.025000, 2)
        self.assertAlmostEqual(as2, 21.79357, 2)

    def test_3500_350(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 350.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 4.025000, 2)
        self.assertAlmostEqual(as2, 12.94635, 2)

    def test_5000_300(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 300.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 5.750000, 2)
        self.assertAlmostEqual(as2, 26.74230, 2)

    def test_5000_250(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 250.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 5.750000, 2)
        self.assertAlmostEqual(as2, 24.60759, 2)

    def test_5000_225(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 225.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 4.578443, 2)
        self.assertAlmostEqual(as2, 23.49285, 2)

    def test_5000_100(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 100.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 12.95305, 2)
        self.assertAlmostEqual(as2, 18.66734, 2)

    def test_5000_25(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 25.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 15.58093, 2)
        self.assertAlmostEqual(as2, 17.00950, 2)

    def test_5000_0(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 0.0

        as1, as2 = compression_asymmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, 16.32650, 2)
        self.assertAlmostEqual(as2, 16.32655, 2)


if __name__ == '__main__':
    unittest.main()
