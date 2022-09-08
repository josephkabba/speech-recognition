import kivy
from kivy.app import App
from gui.screens.chatscreen import ChatScreen
kivy.require("1.10.1")


class SRMainApp(App):

    def __init__(self, sendMessage, **kwargs):
        super(**kwargs).__init__()
        self.sendMessage = sendMessage

    def build(self):
        self.chatscreen = ChatScreen(sendMessage=self.sendMessage)
        return self.chatscreen

    def getChatInstance(self):
        return self.chatscreen