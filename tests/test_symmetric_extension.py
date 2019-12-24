import unittest

from uls import extension_symmetric

h = 0.6
b = 0.3
a1 = a2 = 0.05
eta_bet = 1.0
lambda_bet = 0.8
f_cd = 21.43
f_ck = 30


class TestSymmetricExtension(unittest.TestCase):

    def test_500_0(self):
        """
            Test symmetric reinforcement for N=-500 kN, M=0 kNm
        """

        n_ed = 500.0
        m_ed = 0.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 5.750034, 2)

    def test_500_10(self):
        """
            Test symmetric reinforcement for N=-500 kN, M=10 kNm
        """

        n_ed = 500.0
        m_ed = 10.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 6.136741, 2)

    def test_500_75(self):
        """
            Test symmetric reinforcement for N=-500 kN, M=75 kNm
        """

        n_ed = 500.0
        m_ed = 75.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 8.906260, 2)

    def test_500_100(self):
        """
            Test symmetric reinforcement for N=-500 kN, M=100 kNm
        """

        n_ed = 500.0
        m_ed = 100.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 10.04298, 2)

    def test_50_200(self):
        """
            Test symmetric reinforcement for N=-50 kN, M=200 kNm
        """

        n_ed = 50.0
        m_ed = 200.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 9.409347, 2)

    def test_50_650(self):
        """
            Test symmetric reinforcement for N=-50 kN, M=650 kNm
        """

        n_ed = 50.0
        m_ed = 650.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 30.14430, 2)

    def test_50_1000(self):
        """
            Test symmetric reinforcement for N=-50 kN, M=1000 kNm
        """

        n_ed = 50.0
        m_ed = 1000.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 46.29033, 2)

    def test_5_1500(self):
        """
            Test symmetric reinforcement for N=-5 kN, M=1500 kNm
        """

        n_ed = 5.0
        m_ed = 1500.0

        as1, as2 = extension_symmetric.main(h, b, a1, a2, m_ed, n_ed, eta_bet, lambda_bet, f_cd, f_ck)
        self.assertAlmostEqual(as1, as2, 1)
        self.assertAlmostEqual(as1, 68.83768, 2)


if __name__ == '__main__':
    unittest.main()
