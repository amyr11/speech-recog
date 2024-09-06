import requests
import speech_recognition
from gtts import gTTS
import os

def getresponse(prompt):
    url = "https://chatplm-api.onrender.com/chat"
    params = {
        "prompt": prompt
    }
    headers = {
        "api-key": "chatplm-api-bscs22"
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()["output"]


recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio)
output = getresponse(text)
speech = gTTS(text=output, lang='tl', slow=False)
speech.save("response.mp3")

print("[You]:")
print(text)
print()
print("[ChatPLM]:")
print(output)
os.system("afplay response.mp3")
