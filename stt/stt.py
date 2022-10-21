from vosk import Model, KaldiRecognizer
import pyaudio


def startSTT(printToScreen):
    try:
        model = model = Model(lang="en-us")
        reocgnizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()

        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

        stream.start_stream()

        printToScreen("Listening...")

        while True:
            data = stream.read(4096)
            if reocgnizer.AcceptWaveform(data):
                result = reocgnizer.Result()
                response = result[14:-3]
                
                if response != "":
                    printToScreen(response)

    except OSError as e:
        print(e)

    finally:
        stream.close()
