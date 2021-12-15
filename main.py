from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.app import MDApp

class ContentNavigationDrawer(MDBoxLayout):
    pass

class HomeScreen(Screen):
    pass


class FentyFilePreviewer(MDApp):

    #  Display Variables
    screen_manager = ObjectProperty()
    home_screen = ObjectProperty()
    files_screen = ObjectProperty()
    people_screen = ObjectProperty()
    settings_screen = ObjectProperty()

    def build(self):
        self.theme_cls.theme_style = "Dark"

        # Set up Screen Manager
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = NoTransition()

        # Set Up Screens
        self.home_screen = Builder.load_file('screens/HomeScreen.kv')

        # Loading main layout
        self.main_layout = Builder.load_file('main.kv')
        self.main_layout.add_widget(self.screen_manager)
        return self.main_layout

    # PAGE NAVIGATION GOES HERE
    def show_home_screen(self):
        if 'HomeScreen' not in self.screen_manager.screen_names:
            self.screen_manager.add_widget(HomeScreen(name='HomeScreen'))
        self.screen_manager.current = 'HomeScreen'
        print(self.screen_manager.current)

if __name__ == '__main__':
    FentyFilePreviewer().run()
