import kivy
kivy.require('2.3.1')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import NoTransition

from str0 import ScreenNull
from str1 import ScreenEin
from str2 import ScreenZwei
from str3 import ScreenDrei
from str4 import ScreenVier
from str5 import ScreenFuenf
from str6 import ScreenSechs
from str7 import ScreenSieben

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_wl = True
        self.menu_wi = 0
        self.wysokosc_opcji = "48dp"
        self.szerokosc_opcji = "144dp"
        self.wysokosc_menu = 8 * 48 + 48  #pilnować mnożkina przy zmianie liczby opcji
        self.kolor_tekstu = [.2, .15686, .07059, 1]
        self.kolor_tla = [.97, .97, .97, 1]
        self.kolor_akcentu = [.79216, .64314, .31765, 1]


    def build(self):
        sm = ScreenManager(transition=NoTransition())

        sm.add_widget(ScreenNull(
            name='str0',
            menu_wl = self.menu_wl, menu_wi = self.menu_wi,
            wysokosc_opcji = self.wysokosc_opcji,
            szerokosc_opcji = self.szerokosc_opcji,
            wysokosc_menu = self.wysokosc_menu,
            kolor_tekstu = self.kolor_tekstu,
            kolor_tla = self.kolor_tla,
            kolor_akcentu = self.kolor_akcentu))

        sm.add_widget(ScreenEin(
            name='str1',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenZwei(
            name='str2',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenDrei(
            name='str3',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenVier(
            name='str4',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenFuenf(
            name='str5',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenSechs(
            name='str6',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.add_widget(ScreenSieben(
            name='str7',
            menu_wl=self.menu_wl, menu_wi=self.menu_wi,
            wysokosc_opcji=self.wysokosc_opcji,
            szerokosc_opcji=self.szerokosc_opcji,
            wysokosc_menu=self.wysokosc_menu,
            kolor_tekstu=self.kolor_tekstu,
            kolor_tla=self.kolor_tla,
            kolor_akcentu=self.kolor_akcentu))

        sm.current = 'str0'
        return sm

if __name__ == '__main__':
    MyApp().run()
