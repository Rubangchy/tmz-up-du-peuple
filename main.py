from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='Test minimal', font_size=40)

TestApp().run()