# coding=utf-8
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import json
import sys

creds = json.load(open('watson_credentials.json'))

text_to_speech = TextToSpeechV1(
    username=creds['username'],
    password=creds['password'],
    x_watson_learning_opt_out=True)  # Optional flag

voice = 'en-US_MichaelVoice'

def synthesise(text: str):
    with open(join(dirname(__file__), './t2s//output.wav'), 'wb') as audio_file:
        speech = text_to_speech.synthesize(text, accept='audio/wav', voice=voice)
        audio_file.write(speech)

if __name__ == '__main__':
    print(json.dumps(text_to_speech.voices(), indent=2))

    text = sys.argv[0]
    synthesise(text)
