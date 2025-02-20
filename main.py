import kivy
kivy.require('2.3.1')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import NoTransition

from str0 import ScreenNull
from str1 import ScreenEins
from str2 import ScreenZwei
from str3 import ScreenDrei
from str4 import ScreenVier
from str5 import ScreenFuenf
from str6 import ScreenSechs
from str7 import ScreenSieben

import os


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Editing foreword (more in str0.py, str0.kv):
    # >Owszem, mogę w pythonie robić multiline comments ale bardziej
    #mi się w Pycharmie podoba kolor tych hashtagowych, oraz wiem,
    #że mogę zmienić to w ustawieniach ale mi się nie chce

    # >Aplikację uruchamiamy z /main.py/

    # >Zmienne w /#blok Z/ w //class StrefaSacrumApp\def __init__// są niezbędne do prawidłowego
    #funkcjonowania wszystkich podstron więc ich nie dotykamy

    # >Wygląd podstrony X definiujemy w /strX.kv/
    #a jej funkcje w /strX.py/

    # >Wprowadzając zmienną Y wspólną dla większości podstron:
        #Definiujemy ją w //class StrefaSacrumApp\def __init__// jako self.Y = wartość
        #Dla każdej podstrony X używającej zmiennej Y:
            #W //strX.py\class ScreenX// definiujemy pustą zmienną Y z odpowiednią właściwością (Property)
            #W //main.py\class StrefaSacrumApp\def build\sm.add_widget(ScreenX) dodajemy: Y = self.Y
        #Gratulacle! Zmienna jest gotowa do użytku w strX.py jako self.Y oraz w strX.kv jako root.Y

    # >By dodać/usunąć podstronę X zobacz poradnik w /str0.kv/

    # >Jakby coś mocno nie chciało działać to mówić

#Dziękuję za uwagę, MZ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class StrefaSacrumApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #blok Z
        self.menu_wl = True
        self.menu_wi = 0
        self.wysokosc_opcji = "48dp"
        self.szerokosc_opcji = "144dp"
        self.wysokosc_menu = 8 * 48 + 48  #8-> liczba podstron, *48->szerokość pojedyńczej opcji w dp, +48-> szerokość menu_button w dp
        self.czcionka = os.path.join("resources","ChakraPetch-Regular.ttf")
        self.kolor_tekstu = [.2, .15686, .07059, 1]
        self.kolor_tla = [.97, .97, .97, 1]
        self.kolor_akcentu = [.79216, .64314, .31765, 1]

        self.s0_name = "Strona główna"
        self.s1_name = "Znajdź Mszę"
        self.s2_name = "Znajdź parafię"
        self.s3_name = "Kalendarz liturgiczny diecezji"
        self.s4_name = "O diecezji"
        self.s5_name = "Sponsorzy i partnerzy"
        self.s6_name = "O nas"
        self.s7_name = "<parafie>" # to trzeba będzie usunąć z menu, ale na razie mi się nie chce, zrobimy to jak ogarniemy kod
        #koniec bloku Z


    def build(self):
        sm = ScreenManager(transition=NoTransition()) #jest to po to by podstrony były fajne

        sm.add_widget(ScreenNull(
            name='str0',
            menu_wl = self.menu_wl, menu_wi = self.menu_wi,
            wysokosc_opcji = self.wysokosc_opcji,
            szerokosc_opcji = self.szerokosc_opcji,
            wysokosc_menu = self.wysokosc_menu,
            czcionka = self.czcionka,
            kolor_tekstu = self.kolor_tekstu,
            kolor_tla = self.kolor_tla,
            kolor_akcentu = self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenEins(
            name='str1',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenZwei(
            name='str2',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenDrei(
            name='str3',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenVier(
            name='str4',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenFuenf(
            name='str5',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenSechs(
            name='str6',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.add_widget(ScreenSieben(
            name='str7',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            czcionka=self.czcionka,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu,

            s0_name = self.s0_name,
            s1_name = self.s1_name,
            s2_name = self.s2_name,
            s3_name = self.s3_name,
            s4_name = self.s4_name,
            s5_name = self.s5_name,
            s6_name = self.s6_name,
            s7_name = self.s7_name,))

        sm.current = 'str0'
        return sm

if __name__ == '__main__':
    StrefaSacrumApp().run()