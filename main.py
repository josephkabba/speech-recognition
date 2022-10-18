from gui.gui_main import SRMainApp
from stt.stt import startSTT
from tts.text_to_speech import TTS

if __name__ == '__main__':
    tts = TTS()
    UI = SRMainApp(tts.speak, startSTT)
    UI.run()