#!/bin/sh

echo "Hello World welcome to AIDA software (Debian)"
echo ""
echo "Installation squence initialized..."

sudo apt-get update -y

if ! command -v git &> /dev/null
then
    echo "Git not found"
    echo "Installing git..."
    sudo apt-get install git -y
fi

echo ""

if ! command -v python3 &> /dev/null
then
    echo "Python3 not found"
    echo "Installing python3..."
    sudo apt-get install python3.7
    sudo apt install python3-pip
fi

if ! command -v wget &> /dev/null
then
    echo "wget not found"
    echo "Installing wget..."
    sudo apt install wget
fi


git clone https://github.com/josephkabba/speech-recognition.git

cd speech-recognition

sudo apt-get install libasound-dev portaudio19-dev libportaudio2 python-pyaudio libportaudiocpp0


echo ""
echo "Installing modals"
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

mkdir models

mv deepspeech-0.9.3-models.tflite models/deepspeech-0.9.3-models.tflite
mv deepspeech-0.9.3-models.scorer models/deepspeech-0.9.3-models.scorer