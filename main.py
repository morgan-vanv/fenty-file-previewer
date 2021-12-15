from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

class ContentNavigationDrawer(MDBoxLayout):
    pass


class FentyFilePreviewer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    FentyFilePreviewer().run()
