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


from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.clock import Clock

Builder.load_file('str2.kv')

import config

# see editing_foreword.txt


class ScreenZwei(Screen):

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


class RecycleLabel(RecycleDataViewBehavior, Label):
    """ Custom Label for RecycleView items. """
    text = StringProperty("")  # Ensures text appears in labels

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     print("hi")


class SearchableRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self.set_viewclass, 0)

        # Make sure layout updates properly
        self.layout_manager = RecycleBoxLayout(orientation="vertical", spacing=5, size_hint_y=None)
        self.layout_manager.bind(minimum_height=self.layout_manager.setter("height"))
        self.add_widget(self.layout_manager)

        # Ensure items have a proper height
        self.layout_manager.default_size = None, 40  # 40px height per item
        self.layout_manager.default_size_hint = 1, None  # Full width, fixed height

        # Initialize list of items
        self.all_items = [
            'Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Mango', 'Orange', 'Peach'
        ]

        # print(f"DEBUG: Initial items → {self.all_items}")  # Debugging print

        self.update_data(self.all_items)  # Load all items initially

    def update_data(self, items):
        """Update the RecycleView data dynamically."""
        if items is None:
            items = []  # Ensure items is always a list

        self.data = [{'text': item} for item in items]  # Correct data format

        # print(f"DEBUG: Updating data → {self.data}")  # Debugging print

        self.refresh_from_data()  # Ensures UI updates dynamically

    def filter_items(self, query):
        """Filter the list based on user input."""
        if not self.all_items:
            # print("ERROR: self.all_items is empty!")  # Debugging print
            return

        query = query.strip().lower()  # Normalize input

        filtered = [item for item in self.all_items if query in item.lower()]

        # print(f"DEBUG: Filtering for '{query}' → Found: {filtered}")  # Debugging print

        self.update_data(filtered)  # Update UI with filtered results

    def set_viewclass(self, dt):
        self.viewclass = "RecycleLabel"
        # print(f"DEBUG (delayed): viewclass = {self.viewclass}")  # Should print "RecycleLabel"


class SearchBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Search bar
        self.search_input = TextInput(hint_text='Search...', size_hint_y=None, height=40)
        self.search_input.bind(text=self.on_text)
        self.add_widget(self.search_input)

        # Search results list
        self.result_list = SearchableRecycleView()
        self.add_widget(self.result_list)

    def on_text(self, instance, value):
        """Update the search results when text changes."""
        self.result_list.filter_items(value)
