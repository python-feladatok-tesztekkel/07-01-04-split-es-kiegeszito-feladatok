from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestLegnagyobbFogyasztasNapja(TestCase):
    def test_feladat01(self):
        adatok = ""
        aktualis = feladatok.legnagyobb_fogyasztas_napja(adatok)
        elvart = None
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat02(self):
        adatok = "5,4; 4,7; 6,2; 5,0; 5,4; 5,3; 5,6"
        aktualis = feladatok.legnagyobb_fogyasztas_napja(adatok)
        elvart = 3
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat03(self):
        adatok = "7,4; 4,7; 6,2; 5,0; 5,4; 5,3; 5,6"
        aktualis = feladatok.legnagyobb_fogyasztas_napja(adatok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")
    def test_feladat04(self):
        adatok = "3,4; 4,7; 6,2; 5,0; 5,4; 5,3; 7,6"
        aktualis = feladatok.legnagyobb_fogyasztas_napja(adatok)
        elvart = 7
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány diáknak van több keresztneve")