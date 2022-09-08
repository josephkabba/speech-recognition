from gui.gui_main import SRMainApp
from stt.mic_vad_streaming import startSTTModal
from tts.text_to_speech import TTS
from threading import Thread


if __name__ == '__main__':
    tts = TTS()
    UI = SRMainApp(tts.speak)

    # chat = UI.getChatInstance()
    incoming_message = lambda text: print(text)
    mlRunner = lambda  : startSTTModal(incoming_message)

    thread1 = Thread(target=mlRunner)
    thread1.start()

    UI.run()
