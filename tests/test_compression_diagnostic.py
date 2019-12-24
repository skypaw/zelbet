import unittest

from uls import compression_diagnostic

h = 0.6
b = 0.3
a1 = a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43
f_ck = 50


class TestAsymmetric(unittest.TestCase):

    def test_5_10(self):
        """
            Test asymmetric reinforcement for N=5 kN, M=10 kNm
        """

        n_ed = 5.0
        m_ed = 10.0

        as_1 = 0.219840 * 10 ** -4
        as_2 = 1.80000 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_100_100(self):
        """
            Test asymmetric reinforcement for N=100 kN, M=100 kNm
        """

        n_ed = 100.0
        m_ed = 100.0

        as_1 = 3.102643 * 10 ** -4
        as_2 = 1.80000 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_1000_500(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=500 kNm
        """

        n_ed = 1000.0
        m_ed = 500.0

        as_1 = 17.95217 * 10 ** -4
        as_2 = 1.80000 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_1000_750(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 1000.00
        m_ed = 750.0

        as_1 = 29.879164 * 10 ** -4
        as_2 = 12.74813 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_3500_500(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 500.0

        as_1 = 4.025000 * 10 ** -4
        as_2 = 21.79357 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_3500_350(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 350.0

        as_1 = 4.025000 * 10 ** -4
        as_2 = 12.94635 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_300(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 300.0

        as_1 = 5.750000 * 10 ** -4
        as_2 = 26.74230 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_250(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 250.0

        as_1 = 5.750000 * 10 ** -4
        as_2 = 24.60759 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_225(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 225.0

        as_1 = 4.578443 * 10 ** -4
        as_2 = 23.49285 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_100(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 100.0

        as_1 = 12.95305 * 10 ** -4
        as_2 = 18.66734 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_25(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 25.0

        as_1 = 15.58093 * 10 ** -4
        as_2 = 17.00950 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)

    def test_5000_0(self):
        """
            Test asymmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 0.0

        as_1 = 16.32650 * 10 ** -4
        as_2 = 16.32655 * 10 ** -4

        n_rd, m_rd = compression_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(n_rd, n_ed, 0)
        self.assertAlmostEqual(m_rd, m_ed, 0)


if __name__ == '__main__':
    unittest.main()
