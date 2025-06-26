# wyszukiwanie Mszy

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

from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock
from kivy.uix.button import Button

# from wyszukiwanie.algorytmdane import daj_wszystko_po_id, liczba_rekordow
from wyszukiwanie.algorytmdane import daj_liste_mszy
from wyszukiwanie.skrypciki import nazwa_parafii

from str_par import ScreenUnendlich

from search_box import RecycleLabel, SearchableRecycleView, SearchBox

from kivy.uix.dropdown import DropDown # do wyboru rodzaju, todo


Builder.load_file('str1.kv')

import config


# see editing_foreword.txt


class ScreenEins(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()
    show_pow = BooleanProperty(True)

    def hide_powiadomienie(self):
        self.show_pow = False

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



class MassList(SearchableRecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        items = daj_liste_mszy(0000, home=True)
        self.all_items = []
        for item in items:
            res = []
            tmp = item.split(",")
            id_par = int(tmp[2])
            res.append(f"[b]{tmp[0][:-2]}:{tmp[0][-2:]}{tmp[1]}[/b] - {nazwa_parafii(id_par, home=True)}")
            res.append(id_par)
            self.all_items.append(res)
        # print(self.all_items)

        self.update_data(self.all_items)



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

        if ":" not in query:
            return

        query = query.strip().split(":")
        query = query[0] + query[1]
        query = int(query)
        
        items = daj_liste_mszy(query, home=True)
        filtered = []
        for item in items:
            res = []
            tmp = item.split(",")
            id_par = int(tmp[2])
            res.append(f"[b]{tmp[0][:-2]}:{tmp[0][-2:]}{tmp[1]}[/b] - {nazwa_parafii(id_par, home=True)}")
            res.append(id_par)
            filtered.append(res)

        self.update_data(filtered)  # Update UI with filtered results


class MassSearchBox(SearchBox):
    hint = StringProperty()
