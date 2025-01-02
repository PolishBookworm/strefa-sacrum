import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label


class SacrumApp(App):

    def build(self):
        return Label(text="Strefa Sacrum")


if __name__ == '__main__':
    SacrumApp().run()