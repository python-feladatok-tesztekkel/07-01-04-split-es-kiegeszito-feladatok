from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKeresetAdottKeresztnevet(TestCase):
    def test_feladat01(self):
        adatok = ""
        keresett = "Bela"
        aktualis = feladatok.van_e_adott_keresztnevu(adatok,keresett)
        elvart = False
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány van e "+ keresett+" keresztnevű a listában.")
    def test_feladat02(self):
        adatok = "Albert Gyula;Szucs Gyorgy;Ban Bela;Kosa Gabor;Pataky Jozsef;Racz  Aliz;Vigh Eva"
        keresett = "Gyula"
        aktualis = feladatok.van_e_adott_keresztnevu(adatok,keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány van e "+ keresett+" keresztnevű a listában.")
    def test_feladat03(self):
        adatok = "Albert Gyula;Szucs Gyorgy;Ban Bela;Kosa Gabor;Pataky Jozsef;Racz  Aliz;Vigh Eva"
        keresett = "Eva"
        aktualis = feladatok.van_e_adott_keresztnevu(adatok,keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány van e "+ keresett+" keresztnevű a listában.")
    def test_feladat04(self):
        adatok = "Albert Gyula;Szucs Gyorgy;Ban Bela;Kosa Gabor;Pataky Jozsef;Racz  Aliz;Vigh Eva"
        keresett = "Gabor"
        aktualis = feladatok.van_e_adott_keresztnevu(adatok,keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány van e "+ keresett+" keresztnevű a listában.")
    def test_feladat05(self):
        adatok = "Albert Gyula;Szucs Gyorgy;Ban Bela;Kosa Gabor;Pataky Jozsef;Racz  Aliz;Vigh Eva"
        keresett = "Marton"
        aktualis = feladatok.van_e_adott_keresztnevu(adatok,keresett)
        elvart = False
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány van e "+ keresett+" keresztnevű a listában.")