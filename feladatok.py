# feladat.py

# 1. feladat
# Adottak nevek, ez a függvény bemenete: "Albert Gyula;Szucs Gyorgy Geza;Ban Bela;Kosa Gyula Gabor;Pataky Jozsef;Racz Dora Aliz;Vigh Eva;"
# Készítsen függvényt tobbnevuek_szama néven.
# Határozza meg, hány diáknak van egynél több keresztneve

def tobbnevuek_szama(nevek:str) -> int:
    return 0

# 2. feladat
# Adottak nevek, ez a függvény bemenete: "Albert Gyula;Szucs Gyorgy Geza;Ban Bela;Kosa Gyula Gabor;Pataky Jozsef;Racz Dora Aliz;Vigh Eva;"
# Írjon függvényt van_e_adott_keresztnevu néven
# A függvény bemeneti paramétere még a keresett string, amely egy keresztnevet tatralmaz.
# A függvény adjon vissza igazat, ha az adott keresztnévvel van név a nevek változóban.
def van_e_adott_keresztnevu(nevek:str, keresett:str)->bool:
    return False

# 3. feladat
# Egy vállalkozó megmérte, a hét melyik napján mennyi volt autójának fogyasztása: "5,4; 4,7; 6,2; 5,0; 5,4; 5,3; 5,6"
# Írjon függvényt legnagyobb_fogyasztas_napja amely meghatározza, hogy a hét hanyadik napján volt a fogyasztás a legnagyobb
# Ha nincs adat térjen vissza a None értékkel
# Feltételezheti, hogyha van adat, akkor a hét minden napjának adata helyesen van megadva

def legnagyobb_fogyasztas_napja(fogyasztasok:str)->float:
    return 0

# 4. feladat
# Egy csoportban félévkor a következő átlageredmények születtek: "3,4; 4,7; 4,2; 3,0; 3,4; 3,3; 3,6; 2,3; 3,9; 4,0"
# Írjon függvényt jelestanulok_szama néven amely megadja, hány jeles tanuló volt az osztályba
# Az a jeles tanuló, akinek átlaga 3,50 és 4,49 között van.

def jelestanulok_szama(felev:str)->float:
    return 0


