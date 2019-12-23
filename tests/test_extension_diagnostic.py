import unittest

from slupy import extension_diagnostic

h = 0.6
b = 0.3
a1 = a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43


class TestAsymmetricExtension(unittest.TestCase):

    def test_500_0(self):
        """
            Test asymmetric reinforcement for N=-500 kN, M=0 kNm
        """

        n_ed = 500.0
        m_ed = 0.0

        as_1 = 5.750034 * 10 ** -4
        as_2 = 5.750034 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)

        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_500_10(self):
        """
            Test asymmetric reinforcement for N=-500 kN, M=10 kNm
        """

        n_ed = 500.0
        m_ed = 10.0

        as_1 = 6.210037 * 10 ** -4
        as_2 = 5.290032 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_500_75(self):
        """
            Test asymmetric reinforcement for N=-500 kN, M=75 kNm
        """

        n_ed = 500.0
        m_ed = 75.0

        as_1 = 9.200055 * 10 ** -4
        as_2 = 2.300014 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_500_100(self):
        """
            Test asymmetric reinforcement for N=-500 kN, M=100 kNm
        """

        n_ed = 500.0
        m_ed = 100.0

        as_1 = 10.29313 * 10 ** -4
        as_2 = 1.800000 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_50_200(self):
        """
            Test asymmetric reinforcement for N=-50 kN, M=200 kNm
        """

        n_ed = 50.0
        m_ed = 200.0

        as_1 = 9.407365 * 10 ** -4
        as_2 = 1.800000 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_50_650(self):
        """
            Test asymmetric reinforcement for N=-50 kN, M=650 kNm
        """

        n_ed = 50.0
        m_ed = 650.0

        as_1 = 33.83880 * 10 ** -4
        as_2 = 1.800000 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_50_1000(self):
        """
            Test asymmetric reinforcement for N=-50 kN, M=1000 kNm
        """

        n_ed = 50.0
        m_ed = 1000.0

        as_1 = 53.45499 * 10 ** -4
        as_2 = 12.17093 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)

    def test_5_1500(self):
        """
            Test asymmetric reinforcement for N=-5 kN, M=1500 kNm
        """

        n_ed = 5.0
        m_ed = 1500.0

        as_1 = 75.937610 * 10 ** -4
        as_2 = 35.68857 * 10 ** -4

        n_rd, m_rd = extension_diagnostic.main(h, b, a1, a2, m_ed, n_ed, as_1, as_2, eta_bet, lambda_bet, f_cd)
        self.assertAlmostEqual(n_rd, n_ed, 1)
        self.assertAlmostEqual(m_rd, m_ed, 1)


if __name__ == '__main__':
    unittest.main()
