# Zakładki:
0. Strona główna
1. Wyszukiwarka mszy (wg godziny)
2. Wyszukiwarka parafii (wg nazwy)
3. Mapa diecezji
4. Kalendarz liturgiczny diecezji
5. O diecezji
6. Sponsorzy i partnerzy
7. O nas

8. Podstrona każdej parafii -- jako jedna strona, która przyjmuje argument: jaka parafia i wyświetla odpowiednio (nie zakładka) (trzeba dodać)

# O czym warto nie zapomnieć:
- [ ] przejrzeć licencje: kivy, mapview (MIT), https://www.openstreetmap.org/copyright, ...
- [ ] buildozer.spec jak będziemy paczkować (jakie moduły w pythonie; potrzebne permissions np. gps, internet; package.domain; ...)
- [ ] https://kivy.org/doc/stable/api-kivy.app.html#pause-mode
- [ ] disclaimer (sprawdzić aktualność, bo chodzi o syntezę)
- [ ] dodać podstronę dla danych parafii
- [ ] ogarnąć polskie znaki w danych - solve: do open dać: `encoding='utf-8'`
- [ ] ścieżki plików w wyszukiwanie/

# Maybe
- [ ] set map to user location

# Weird stuff for later
- [ ] global constants

# working on it
- [ ] WARNING: running xinput against an Xwayland server. See the xinput man page for details
- [ ] [WARNING] Deprecated property "<BooleanProperty name=allow_stretch>" of object "<str3.ParishMarker object at 0x7a8ba8b8ca60>" was accessed, it will be removed in a future version
- [ ] [WARNING] Deprecated property "<BooleanProperty name=keep_ratio>" of object "<str3.ParishMarker object at 0x7a8ba8b8ca60>" was accessed, it will be removed in a future version
