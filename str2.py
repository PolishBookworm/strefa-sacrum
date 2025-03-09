# wyszukiwanie parafii

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
from kivy.uix.button import Button

from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock

from wyszukiwanie.algorytmdane import daj_wszystko_po_id, liczba_rekordow

from str_par import ScreenUnendlich

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


# class RecycleLabel(RecycleDataViewBehavior, Label):
class RecycleLabel(RecycleDataViewBehavior, Button):
    """ Custom Label for RecycleView items. """
    text = StringProperty("")  # Ensures text appears in labels
    id_parafii = NumericProperty()
    index = NumericProperty()

    def go_to_parish(self):
        # self.dismiss()
        app = App.get_running_app()
        sm = app.root
        name = f"par{self.id_parafii}"
        if not sm.has_screen(name):
            sm.add_widget(ScreenUnendlich(name=name, id_parafii=self.id_parafii))
        sm.current = name

    def on_row_index(self, instance, value):
        """ Dynamically change background color based on row index """
        if value % 2 == 0:
            self.background_color = 0, 0, 0, 0
        else:
            self.background_color = 0, 0, 0, .05



class SearchableRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self.set_viewclass, 0)

        # Make sure layout updates properly
        self.layout_manager = RecycleBoxLayout(orientation="vertical", spacing=0, size_hint_y=None)
        self.layout_manager.bind(minimum_height=self.layout_manager.setter("height"))
        self.add_widget(self.layout_manager)


        """Jak coś ma 3 linijki to zmienić 54dp na 66dp. Jak wygląda brzydko to napisać. MZ"""
        # Ensure items have a proper height
        self.layout_manager.default_size = None, "54dp"  # 40px height per item
        self.layout_manager.default_size_hint = 1, None  # Full width, fixed height


        # Initialize list of items
        # self.all_items = [
        #     'Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Mango', 'Orange', 'Peach'
        # ]

        n = liczba_rekordow(home=True)

        self.all_items = []
        for i in range(n):
            tmp = daj_wszystko_po_id(i, home=True)
            self.all_items.append((tmp[0],i))

        # tmp = [
        #     'Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Mango', 'Orange', 'Peach'
        # ]

        # self.all_items = []
        # for i in range(len(tmp)):
        #     self.all_items.append((tmp[i],i))

        self.update_data(self.all_items)  # Load all items initially


    def update_data(self, items):
        """Update the RecycleView data dynamically."""
        if items is None:
            items = []  # Ensure items is always a list

        self.data = [{'text': item[0], 'id_parafii': item[1], 'index': idx} for idx, item in enumerate(items)]  # Correct data format

        self.refresh_from_data()  # Ensures UI updates dynamically
        self.refresh_from_layout()


    def filter_items(self, query):
        """Filter the list based on user input."""
        if not self.all_items:
            return

        query = query.strip().lower()  # Normalize input

        filtered = [item for item in self.all_items if query in item[0].lower()]

        self.update_data(filtered)  # Update UI with filtered results


    def set_viewclass(self, dt):
        self.viewclass = "RecycleLabel"



class SearchBox(BoxLayout):

    def on_text(self, instance, value):
        """Update the search results when text changes."""
        self.ids.result_list.filter_items(value)


