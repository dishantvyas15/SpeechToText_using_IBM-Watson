from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

# url_s2t = "enter-the-url-of-your-IBM-Watson-SpeechToText-api"
# iam_apikey_s2t = "enter-the-key-of-your-IBM-Watson-SpeechToText-api"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
# print(s2t)

# filename = 'filename.mp3'

with open(filename, mode="rb") as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

# print(response.result)
print('\n')
print(json_normalize(response.result['results'], "alternatives"))
print('\n')
