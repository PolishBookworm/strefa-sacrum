# wyszukiwanie parafii

import kivy
kivy.require('2.3.1')
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock
from kivy.app import App

# from wyszukiwanie.algorytmdane import daj_wszystko_po_id, liczba_rekordow

from str_par import ScreenUnendlich

Builder.load_file('search_box.kv')

import config

# see editing_foreword.txt

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
            self.background_color = 0, 0, 0, .035



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


    def update_data(self, items):
        """Update the RecycleView data dynamically."""
        if items is None:
            items = []  # Ensure items is always a list

        self.data = [{'text': item[0], 'id_parafii': item[1], 'index': idx} for idx, item in enumerate(items)]  # Correct data format

        self.refresh_from_data()  # Ensures UI updates dynamically
        self.refresh_from_layout()


    # def filter_items(self, query):
    #     """Filter the list based on user input."""
    #     if not self.all_items:
    #         return

    #     query = query.strip().lower()  # Normalize input

    #     filtered = [item for item in self.all_items if query in item[0].lower()]

    #     self.update_data(filtered)  # Update UI with filtered results


    def set_viewclass(self, dt):
        self.viewclass = "RecycleLabel"



class SearchBox(BoxLayout):

    def on_text(self, instance, value):
        """Update the search results when text changes."""
        self.ids.result_list.filter_items(value)
