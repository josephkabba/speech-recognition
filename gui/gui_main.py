import kivy
from kivy.app import App
from gui.screens.chatscreen import ChatScreen


class SRMainApp(App):
    def build(self):
        return ChatScreen()


def startUI(app = SRMainApp()):
    app.run()