import kivy
kivy.require('2.3.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.lang import Builder
from kivy import metrics
from kivy.metrics import dp
from kivy.core.window import Window

Builder.load_file('str1.kv')


#visit main.py, str0.py, str0.kv for editing foreword


class ScreenEin(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()

    wysokosc_opcji = StringProperty()
    szerokosc_opcji = StringProperty()
    wysokosc_menu = NumericProperty()

    czcionka = StringProperty()
    kolor_tekstu = ListProperty()
    kolor_tla = ListProperty()
    kolor_akcentu = ListProperty()

    s0_name = StringProperty()
    s1_name = StringProperty()
    s2_name = StringProperty()
    s3_name = StringProperty()
    s4_name = StringProperty()
    s5_name = StringProperty()
    s6_name = StringProperty()
    s7_name = StringProperty()


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
        y_position = self.height - dp(self.wysokosc_menu)

        opcie.height = wys
        lajout.height = wys
        pudlo.pos = (0, y_position)
