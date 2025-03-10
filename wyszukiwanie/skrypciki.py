import os
try:
	from algorytmdane import daj_wszystko_po_id
except ModuleNotFoundError:
	from wyszukiwanie.algorytmdane import daj_wszystko_po_id

def nazwa_parafii(id_parafii, home=False):
	tmp = daj_wszystko_po_id(id_parafii, home=home)
	return f"{tmp[0]} - {tmp[1]}"

def liczba_rekordow(home=False):
    plik = "daneprzyklad.csv"
    if home: # to usuwa problem ze ścieżkami
        plik = os.path.join("wyszukiwanie",plik)
    with open(plik, 'r', encoding='utf-8') as f:
        lines = len(f.readlines())
        return lines