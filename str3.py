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

    mapview = ObjectProperty(None)

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

    def add_markers(self):

        coords = []

        n = liczba_rekordow(home=True)

        for i in range(n):
            tmp = daj_wszystko_po_id(i, home=True)
            tmp = tmp[2]
            tmp = tmp.split(",")
            tmp = list(map(float,tmp))
            coords.append(tmp)

        for i in range(n):
            marker = ParishMarker(lat=coords[i][0],lon=coords[i][1], id_parafii=i)
            self.mapview.add_marker(marker)



class ParishPopup(Popup):
 
    nazwa_parafii = ObjectProperty(None)

    id_parafii = NumericProperty()

    def go_to_parish(self):
        self.dismiss()
        app = App.get_running_app()
        sm = app.root
        name = f"par{self.id_parafii}"
        if not sm.has_screen(name):
            sm.add_widget(ScreenUnendlich(name=name, id_parafii=self.id_parafii))
        sm.current = name

class ParishMarker(MapMarkerPopup):

    id_parafii = NumericProperty()

    def marker_popup(self):
        popup = ParishPopup(id_parafii=self.id_parafii)
        # popup = ParishPopup(czcionka=self.czcionka, kolor_tekstu=self.kolor_tekstu, kolor_tla=self.kolor_tla, kolor_akcentu=self.kolor_akcentu, id_parafii=self.id_parafii)
        tmp = daj_wszystko_po_id(self.id_parafii, home=True)[0]
        popup.nazwa_parafii.text = str(tmp)
        popup.open()