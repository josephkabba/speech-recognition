import kivy
from kivy.app import App
from gui.screens.chatscreen import ChatScreen
from threading import Thread
kivy.require("1.10.1")


class SRMainApp(App):

    def __init__(self, sendMessage, function, **kwargs):
        super(**kwargs).__init__()
        self.sendMessage = sendMessage
        self.function = function
        self.async_start: Thread = None

    def putMessageInQueue(self, message):
        speak = lambda : self.sendMessage(message)
        thread = Thread(target=speak, daemon=True)
        if thread.is_alive():
            thread.join()
        thread.start()

    def build(self):
        self.chatscreen = ChatScreen(sendMessage=self.putMessageInQueue)
        return self.chatscreen

    def runSTT(self):
        printMessage = self.chatscreen.incoming_message
        self.function(printMessage)

    def on_start(self):
        self.async_start =  Thread(target=self.runSTT, daemon=True)
        self.async_start.start()