from kivy.app import App
from kivy.uix.label import Label

class GrowthApp(App):
    def build(self):
        return Label(text='Growth Calculator Works!')

GrowthApp().run()
