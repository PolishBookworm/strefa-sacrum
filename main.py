import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import NoTransition

from str0 import ScreenNull
from str1 import ScreenEins
from str2 import ScreenZwei
from str3 import ScreenDrei
from str4 import ScreenVier
from str5 import ScreenFuenf
from str6 import ScreenSechs
from str7 import ScreenSieben

import os

# see editing_foreword.txt

class StrefaSacrumApp(App):

    def build(self):
        sm = ScreenManager(transition=NoTransition()) #jest to po to by podstrony były fajne

        kwargs = {"menu_wl": True, "menu_wi": 0}

        sm.add_widget(ScreenNull(name='str0',**kwargs))
        sm.add_widget(ScreenEins(name='str1',**kwargs))
        sm.add_widget(ScreenZwei(name='str2',**kwargs))
        sm.add_widget(ScreenDrei(name='str3',**kwargs))
        sm.add_widget(ScreenVier(name='str4',**kwargs))
        sm.add_widget(ScreenFuenf(name='str5',**kwargs))
        sm.add_widget(ScreenSechs(name='str6',**kwargs))
        sm.add_widget(ScreenSieben(name='str7',**kwargs))

        sm.current = 'str0'
        return sm

if __name__ == '__main__':
    StrefaSacrumApp().run()