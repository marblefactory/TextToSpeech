from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


creds = json.load(open('s2t_creds.json'))

speech_to_text = SpeechToTextV1(
    username=creds['username'],
    password=creds['password'],
    x_watson_learning_opt_out=True)  # Optional flag

# print(json.dumps(speech_to_text.models(), indent=2))
#
# print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), './s2t/speech.wav'), 'rb') as audio_file:
    print('recognising')
    text = speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True, word_confidence=True)
    print(text['results'][0]['alternatives'][0]['transcript'])
