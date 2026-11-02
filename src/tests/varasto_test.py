import unittest

from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        # epävalidi tilavuus nollataan
        self.varasto_neg = Varasto(tilavuus=-1)
        # epävalidi alku_saldo
        self.varasto_alku_neg = Varasto(tilavuus=10, alku_saldo=-1)
        # varasto valmiiksi täynnä
        self.varasto_taysi = Varasto(tilavuus=10, alku_saldo=10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto_alku_neg.saldo, 0)

    def test_konstruktori_negatiiviselle_tilavuudelle(self):
        # Ohjelman logiikan mukaan (alku_saldo on suurempi kuin tilavuus)
        # konstruktori asettaa: self.saldo = tilavuus;
        self.assertAlmostEqual(self.varasto_neg.saldo, -1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_neg_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_tayteen_lisays_ei_muuta_saldoa(self):
        self.varasto_taysi.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto_taysi.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_neg_ottaminen_ei_ota_mitaan(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_liika_ottaminen_tyhjentaa_saldon(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_toString(self):
        vastaus = str(self.varasto_taysi)
        self.assertEqual(vastaus, "saldo = 10, vielä tilaa 0")
