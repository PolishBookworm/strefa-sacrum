# wyszukiwanie parafii

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
from kivy.uix.button import Button

from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock

from wyszukiwanie.skrypciki import nazwa_parafii, liczba_rekordow
# from wyszukiwanie.algorytmdane import daj_wszystko_po_id, liczba_rekordow

from str_par import ScreenUnendlich

from search_box import RecycleLabel, SearchableRecycleView, SearchBox

Builder.load_file('str2.kv')

import config

# see editing_foreword.txt


class ScreenZwei(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()

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
        opcie = self.ids.menu.ids.opcie
        pudlo = self.ids.menu.ids.pudlo

        wys = Window.height - dp(48)
        y_position = self.height - dp(config.wysokosc_menu)

        opcie.height = wys
        lajout.height = wys
        pudlo.pos = (0, y_position)

class ParishList(SearchableRecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        n = liczba_rekordow(home=True)

        self.all_items = []
        for i in range(n):
            # tmp = daj_wszystko_po_id(i, home=True)
            # self.all_items.append((f"{tmp[0]} - {tmp[1]}",i))
            self.all_items.append((nazwa_parafii(i,home=True),i))

        self.update_data(self.all_items)  # Load all items initially

    # def update_data(self, items):
    #     """Update the RecycleView data dynamically."""
    #     if items is None:
    #         items = []  # Ensure items is always a list

    #     self.data = [{'text': item[0], 'id_parafii': item[1], 'index': idx} for idx, item in enumerate(items)]  # Correct data format

    #     self.refresh_from_data()  # Ensures UI updates dynamically
    #     self.refresh_from_layout()


    def filter_items(self, query):
        """Filter the list based on user input."""
        if not self.all_items:
            return

        query = query.strip().lower()  # Normalize input

        filtered = [item for item in self.all_items if query in item[0].lower()]

        self.update_data(filtered)  # Update UI with filtered results


class ParishSearchBox(SearchBox):
    hint = StringProperty()