import os

#blok Z
# menu_wl = True
# menu_wi = 0
wysokosc_opcji = "48dp"
szerokosc_opcji = "160dp"
wysokosc_menu = 8 * 48 + 48  #8-> liczba podstron, *48->wysokość pojedyńczej opcji w dp, +48-> wysokość menu_button w dp
czcionka = os.path.join("resources","ChakraPetch-Regular.ttf")
# czcionka_bold = os.path.join("resources","ChakraPetch-Bold.ttf")
# czcionka_italic = os.path.join("resources","ChakraPetch-Italic.ttf")
# czcionka_bolditalic = os.path.join("resources","ChakraPetch-BoldItalic.ttf")
kolor_tekstu = [.2, .15686, .07059, 1]          #~czarny
kolor_tla = [.97, .97, .97, 1]                  #~biały
kolor_akcentu = [.79216, .64314, .31765, 1]     #złoty
kolor_informacyjny = [.97255, .97255, .62745, 1]   #żółty

s0_name = "Strona główna"
s1_name = "Znajdź Mszę"
s2_name = "Znajdź parafię"
s3_name = "Mapa diecezji"
s4_name = "Kalendarz liturgiczny"
s5_name = "O diecezji"
s6_name = "Sponsorzy i partnerzy"
s7_name = "O nas"
#koniec bloku Z

import kivy
kivy.require('2.3.0')
from kivy.core.text import LabelBase

LabelBase.register(name="czcionka", fn_regular=czcionka, fn_italic=os.path.join("resources","ChakraPetch-Italic.ttf"), fn_bold=os.path.join("resources","ChakraPetch-Bold.ttf"), fn_bolditalic=os.path.join("resources","ChakraPetch-BoldItalic.ttf"))
