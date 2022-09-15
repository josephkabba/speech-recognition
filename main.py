from gui.gui_main import SRMainApp
from stt.mic_vad_streaming import startSTTModal
from tts.text_to_speech import TTS

if __name__ == '__main__':
    tts = TTS()
    UI = SRMainApp(tts.speak, startSTTModal)
    UI.run()