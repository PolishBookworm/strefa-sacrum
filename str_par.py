import kivy

kivy.require('2.3.0')
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
from kivy.clock import Clock

from wyszukiwanie.algorytmdane import daj_wszystko_po_id

Builder.load_file('str_par.kv')

import config


# see editing_foreword.txt


class ScreenUnendlich(Screen):
    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()
    show_pow = BooleanProperty(True)

    id_parafii = NumericProperty()

    nazwa_parafii_label = ObjectProperty(None)
    dane_label = ObjectProperty(None)

    def skalibruj_to(self, dt):
        zaw = self.ids.zawiadomienie_o_falszerstwie
        lab1 = self.ids.nazwa_parafii_label
        lab2 = self.ids.dane_label
        wypelniacz = self.ids.wypelniacz

        wys = Window.height - dp(48)

        if (wys - zaw.height - lab1.height - lab2.height) < 0:
            wypelniacz.height = 0
        else:
            wypelniacz.height = wys - zaw.height - lab1.height - lab2.height

    def hide_powiadomienie(self):
        self.show_pow = False
        self.on_size()

    def karta(self, k):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.current = 'str%d' % k
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
        opcie = self.ids.menu.ids.opcie
        pudlo = self.ids.menu.ids.pudlo

        wys = Window.height - dp(48)
        y_position = self.height - dp(config.wysokosc_menu)

        opcie.height = wys
        lajout.height = wys
        pudlo.pos = (0, y_position)

        self.set_data()


    def set_data(self):
        data = daj_wszystko_po_id(self.id_parafii, home=True)
        self.nazwa_parafii_label.text = f"{data[0]} - {data[1]}"

        # tmp = ""
        # for datum in data[2:]:
        #     tmp += datum + '\n'
        tmp = f"""
[b]Msze Święte w niedziele i święta nakazane:[/b]
{data[3]}
[b]Msze Święte w święta nienakazane (zniesione):[/b]
???
[b]Msze Święte w dni powszednie:[/b]
{data[5]}
[b]Godziny adoracji Naświętszego Sakramentu:[/b]
{data[7]}
[b]Godziny spowiedzi świętej:[/b]
{data[9]}
[b]Godziny majówek: (inne nabożeństwa???)[/b]
{data[11]}
[b]Grupy duszpasterskie w parafii:[/b]
{data[13]}

{data[14]}
"""
        self.dane_label.text = tmp

        Clock.schedule_once(self.skalibruj_to, 0)