#!/usr/bin/env python3

import argparse
import queue
import sys
import sounddevice as sd

from vosk import Model, KaldiRecognizer

q = queue.Queue()

def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
args, remaining = parser.parse_known_args()
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
args = parser.parse_args(remaining)

def startSTT(printToScreen):
    try:
    
        device_info = sd.query_devices(args.device, "input")
        samplerate = int(device_info["default_samplerate"])

        model = Model(lang="en-us")

        with sd.RawInputStream(samplerate=samplerate, blocksize = 8000,
                dtype="int16", channels=1, callback=callback):

            rec = KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()[14:-3]
                    if result != "":
                        printToScreen(result)

    except KeyboardInterrupt:
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))