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

Builder.load_file('str0.kv')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Editing foreword (more in main.py, str0.kv):
    # >Owszem, mogę w pythonie robić multiline comments ale bardziej
    #mi się w Pycharmie podoba kolor tych hashtagowych, oraz wiem,
    #że mogę zmienić to w ustawieniach ale mi się nie chce

    # >Aplikację uruchamiamy z /main.py/

    # >Wygląd podstrony X definiujemy w /strX.kv/
    #a jej funkcje w /strX.py/

    # >Wprowadzając zmienną wspólną dla większości podstron
    #definiujemy ją w /main.py/ zgodnie z poradnikiem w /main.py/

    # >By dodać/usunąć podstronę X zobacz poradnik w /str0.kv/

    # >Dla strony X w //strX.py\class ScreenX// powinny znajdować się wszystkie
    #zmienne z //main.py\class StrefaSacrumApp\def build\sm.add_widget(ScreenX)//
    #z odpowiednią właściwością (Property)

    # >Funkcje /def karta/, /def wlacznik_menu/ oraz /def on_size/
    #w /class ScreenX/ są niezbędne do prawidłowego funkcjonowania
    #podstrony więc ich nie dotykamy

    # >Rekomenduje się dodawanie funkcji w /class ScreenX/ po funkcji /def on_size/
    #oraz zmiennych ogólnych w /class ScreenX/ przed funkcją /def karta/

    # >Jakby coś mocno nie chciało działać to mówić

#Dziękuję za uwagę, MZ
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class ScreenNull(Screen):

    menu_wl = BooleanProperty()
    menu_wi = NumericProperty()

    wysokosc_opcji = StringProperty()
    szerokosc_opcji = StringProperty()
    wysokosc_menu = NumericProperty()

    czcionka = StringProperty()
    kolor_tekstu = ListProperty()
    kolor_tla = ListProperty()
    kolor_akcentu = ListProperty()

    s0_name = StringProperty()
    s1_name = StringProperty()
    s2_name = StringProperty()
    s3_name = StringProperty()
    s4_name = StringProperty()
    s5_name = StringProperty()
    s6_name = StringProperty()
    s7_name = StringProperty()

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
        y_position = self.height - dp(self.wysokosc_menu)

        opcie.height = wys
        lajout.height = wys
        pudlo.pos = (0, y_position)
