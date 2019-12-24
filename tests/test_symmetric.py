import unittest

from uls import compression_symmetric

h = 0.6
b = 0.3
a1 = a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43
f_ck = 30


class TestSymmetric(unittest.TestCase):

    def test_5_10(self):
        """
            Test symmetric reinforcement for N=5 kN, M=10 kNm
        """

        n_ed = 5.0
        m_ed = 10.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 0.329204, 2)

    def test_100_100(self):
        """
            Test symmetric reinforcement for N=100 kN, M=100 kNm
        """

        n_ed = 100.0
        m_ed = 100.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 3.101074, 2)

    def test_1000_500(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=500 kNm
        """

        n_ed = 1000.0
        m_ed = 500.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 12.77754, 2)

    def test_1000_750(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 1000.00
        m_ed = 750.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 24.27754, 2)

    def test_3500_500(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 500.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 21.21958, 2)

    def test_3500_350(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 3500.0
        m_ed = 350.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 13.02856, 2)

    def test_5000_300(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 300.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 26.57117, 2)

    def test_5000_250(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 250.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 24.29538, 2)

    def test_5000_225(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 225.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 23.18530, 2)

    def test_5000_100(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 100.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 17.73990, 2)

    def test_5000_25(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 25.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 16.32285, 2)

    def test_5000_0(self):
        """
            Test symmetric reinforcement for N=1000 kN, M=750 kNm
        """

        n_ed = 5000.0
        m_ed = 0.0

        as1, as2 = compression_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 16.32285, 2)


if __name__ == '__main__':
    unittest.main()
