from kivy.app import App
from kivy.uix.button import Button

class testAPP(App):
    def build(self):
        return Button(text="Hi Joseph")


testAPP().run()