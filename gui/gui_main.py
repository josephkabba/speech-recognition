import kivy
from kivy.app import App
from kivy.uix.label import Label


class SRMain(App):
    def build(self):
        return Label(text='Hello World')


def startUI(app = SRMain()):
    app.run()