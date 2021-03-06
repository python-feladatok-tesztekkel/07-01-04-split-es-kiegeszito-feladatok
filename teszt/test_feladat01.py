from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTobbnevuek(TestCase):
    def test_feladat01(self):
        adatok = ""
        aktualis = feladatok.tobbnevuek_szama(adatok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat02(self):
        adatok = "aaaa aaaa aaaa;bbbbb bbbbb;ccccc cccc"
        aktualis = feladatok.tobbnevuek_szama(adatok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat03(self):
        adatok = "aaaa aaaa;bbbbb bbbbb;ccccc cccc cccccc"
        aktualis = feladatok.tobbnevuek_szama(adatok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat04(self):
        adatok = "aaaa aaaa aaaaaaaa;bbbbb bbbbb;ccccc cccc cccccc;dddddddd dddddd dddddd;eeeeee;ffffffff fffffff ffffff;ggggg"
        aktualis = feladatok.tobbnevuek_szama(adatok)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")