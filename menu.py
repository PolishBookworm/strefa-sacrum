import kivy
kivy.require('2.3.0')

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

import config

Builder.load_file('menu.kv')

class HamburgerMenu(FloatLayout):
    current_tab = NumericProperty()