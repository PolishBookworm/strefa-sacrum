# mapa diecezji

import kivy
kivy.require('2.3.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.lang import Builder
from kivy import metrics
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle

from kivy_garden.mapview import MapView, MapMarkerPopup

from wyszukiwanie.algorytmdane import daj_wszystko_po_id, liczba_rekordow

from str_par import ScreenUnendlich

import config

Builder.load_file('str3.kv')

# see editing_foreword.txt


class ScreenDrei(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()

    # wysokosc_opcji = StringProperty()
    # szerokosc_opcji = StringProperty()
    # wysokosc_menu = NumericProperty()

    # czcionka = StringProperty()
    # kolor_tekstu = ListProperty()
    # kolor_tla = ListProperty()
    # kolor_akcentu = ListProperty()

    # s0_name = StringProperty()
    # s1_name = StringProperty()
    # s2_name = StringProperty()
    # s3_name = StringProperty()
    # s4_name = StringProperty()
    # s5_name = StringProperty()
    # s6_name = StringProperty()
    # s7_name = StringProperty()

    mapview = ObjectProperty(None)

    # popup = ObjectProperty(None)

    def karta(self, k):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'str%d' %k

    def wlacznik_menu(self, widget):
        if widget.state == "normal":
            self.menu_wl = True
            self.menu_wi = 0
        else:
            self.menu_wl = False
            self.menu_wi = 1

    def on_size(self, *args):
        lajout = self.ids.lajout
        opcie = self.ids.opcie
        pudlo = self.ids.pudlo

        wys = Window.height - dp(48)
        y_position = self.height - dp(config.wysokosc_menu)

        opcie.height = wys
        lajout.height = wys
        pudlo.pos = (0, y_position)

        self.add_markers()

    # def marker_popup(self, lat, lon):
    #     popup = ParishPopup(czcionka=self.czcionka, kolor_tekstu=self.kolor_tekstu, kolor_tla=self.kolor_tla, kolor_akcentu=self.kolor_akcentu)
    #     popup.open()

    def add_markers(self):

        coords = []

        n = liczba_rekordow(home=True)

        for i in range(n):
            tmp = daj_wszystko_po_id(i, home=True)
            tmp = tmp[2]
            tmp = tmp.split(",")
            tmp = list(map(float,tmp))
            coords.append(tmp)

        # for lat, lon in coords:
        #     marker = ParishMarker(lat=lat,lon=lon, czcionka=self.czcionka, kolor_tekstu=self.kolor_tekstu, kolor_tla=self.kolor_tla, kolor_akcentu=self.kolor_akcentu)
        #     self.mapview.add_marker(marker)

        # for i in range(n):
        #     marker = ParishMarker(lat=coords[i][0],lon=coords[i][1], id_parafii=i, czcionka=self.czcionka, kolor_tekstu=self.kolor_tekstu, kolor_tla=self.kolor_tla, kolor_akcentu=self.kolor_akcentu)
        #     self.mapview.add_marker(marker)

        for i in range(n):
            marker = ParishMarker(lat=coords[i][0],lon=coords[i][1], id_parafii=i)
            self.mapview.add_marker(marker)



class ParishPopup(Popup):
    # czcionka = StringProperty()
    # kolor_tekstu = ListProperty()
    # kolor_tla = ListProperty()
    # kolor_akcentu = ListProperty()

    nazwa_parafii = ObjectProperty(None)

    id_parafii = NumericProperty()

    def go_to_parish(self):
        self.dismiss()
        app = App.get_running_app()
        sm = app.root
        sm.add_widget(ScreenUnendlich(name='par', id_parafii=self.id_parafii))
        # sm.add_widget(ScreenUnendlich(name='par', id_parafii=self.id_parafii, **kwargs))
        sm.current = 'par'

class ParishMarker(MapMarkerPopup):
    # czcionka = StringProperty()
    # kolor_tekstu = ListProperty()
    # kolor_tla = ListProperty()
    # kolor_akcentu = ListProperty()

    id_parafii = NumericProperty()

    def marker_popup(self):
        popup = ParishPopup(id_parafii=self.id_parafii)
        # popup = ParishPopup(czcionka=self.czcionka, kolor_tekstu=self.kolor_tekstu, kolor_tla=self.kolor_tla, kolor_akcentu=self.kolor_akcentu, id_parafii=self.id_parafii)
        tmp = daj_wszystko_po_id(self.id_parafii, home=True)[0]
        popup.nazwa_parafii.text = str(tmp)
        popup.open()