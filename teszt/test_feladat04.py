from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestJelesTanulok(TestCase):
    def test_feladat01(self):
        adatok = ""
        aktualis = feladatok.jelestanulok_szama(adatok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diák eredménye jeles")
    def test_feladat02(self):
        adatok = "3,4; 4,7; 4,2; 3,0; 3,4; 3,3; 3,6; 2,3; 3,9; 4,0"
        aktualis = feladatok.jelestanulok_szama(adatok)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diák eredménye jeles")
    def test_feladat03(self):
        adatok = "3,4; 2,7; 2,2; 2,0; 2,4; 2,3; 2,6; 2,3; 2,9; 5,0"
        aktualis = feladatok.jelestanulok_szama(adatok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diák eredménye jeles")
    def test_feladat04(self):
        adatok = "4,3; 2,7; 2,2; 2,0; 2,4; 2,3; 2,6; 2,3; 2,9; 5,0"
        aktualis = feladatok.jelestanulok_szama(adatok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diák eredménye jeles")
    def test_feladat05(self):
        adatok = "3,4; 2,7; 2,2; 2,0; 2,4; 2,3; 2,6; 2,3; 2,9; 4,0"
        aktualis = feladatok.jelestanulok_szama(adatok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diák eredménye jeles")