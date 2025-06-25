import kivy
kivy.require('2.3.0')
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
from kivy.clock import Clock

Builder.load_file('str5.kv')

import config

# see editing_foreword.txt


class ScreenFuenf(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()

    def skalibruj_to(self, dt):
        opis = self.ids.opis
        wypelniacz = self.ids.wypelniacz

        wys = Window.height - dp(48)

        if (wys - opis.height) < 0:
            wypelniacz.height = 0
        else:
            wypelniacz.height = wys - opis.height


    def karta(self, k):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'str%d' %k
        self.menu_wl = True
        self.menu_wi = 0

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

        Clock.schedule_once(self.skalibruj_to, 0)
