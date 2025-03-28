import csv
import os
#id parafii to numer wiersza w którym ta parafia sie znajduje, numerujemy od 0

#wypisz wszystko o parafii, mając id parafii
def daj_wszystko_po_id(id_parafii, home=False):
    plik = "daneprzyklad.csv"
    if home: # to usuwa problem ze ścieżkami
        plik = os.path.join("wyszukiwanie",plik)

    csv_plikdwpid = csv.reader(open(plik, "r", encoding='utf-8'), delimiter=';')
    c_dwpid = -1 #counter_daj_wszystko_po_id
    for row in csv_plikdwpid:
        c_dwpid +=1
        if c_dwpid == id_parafii:
            if id_parafii!=0:
                return(row)
            else:
                return [row[0][1:]]+row[1:]

#znajdz msze na dana godzine
def daj_liste_mszy(godzina, home=False, tryb=0): # tryb: 0 - niedziela, 1 - nienakazane, 2 - dni powszednie
    plik = "posortowane.csv"
    if home: # to usuwa problem ze ścieżkami
        plik = os.path.join("wyszukiwanie",plik)

    csv_file = csv.reader(open(plik, "r", encoding='utf-8'), delimiter=';')
    lista_mszy = next(csv_file) # tu uwzględnić tryb
    return lista_mszy[binarprzejscie1(lista_mszy, godzina):]

def binarprzejscie1(arr, x):
    if x <= int(arr[0].split(',')[0]):
        return 0
    elif x > int(arr[-1].split(',')[0]):
        return len(arr)
    else:
        #print("wchodze tutaj")
        return binary_search(arr, 0, len(arr) - 1, x) + 1

def binary_search(arr, low, high, x):
    if high >= low or int(arr[high].split(',')[0]) == int(arr[low].split(',')[0]):
        mid = (high + low) // 2
        if int(arr[mid].split(',')[0]) < x and int(arr[mid + 1].split(',')[0]) >= x:
            return mid
        elif int(arr[mid].split(',')[0]) >= x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        if x >= int(arr[-1].split(',')[0]):
            return len(arr)
        else:
            return -1

# print(daj_liste_mszy(1700)) #ta linijka co wyjdzie to wszystkie msze gdzie dla mszy wiemy tak
#czy jest ona
#znajdz x na dana godzine, dla różańców, majówek i krótkich nabożeństw będzie całkowicie analogiczny algorytm
#dla adoracji i spowiedzi będzie się różnił tylko tym że sortujemy po godzinach zakończenia

#pokaz wspolnoty - nie robie bo to to samo co daj_wszystko_po_id[kolumnawspolnoty]
