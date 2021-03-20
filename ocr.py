import pytesseract
import matplotlib.pyplot as plt
import cv2
import os
import win32com.client 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path=r"post.png"
# load the original image
image = cv2.imread(image_path)   

plt.figure(figsize=(10,10))
plt.imshow(image)

import requests
from pygame import mixer
from gtts import gTTS
ret,thresh1 = cv2.threshold(image,120,255,cv2.THRESH_BINARY)

# pytesseract image to string to get results
text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
print(text)


speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(text)

tts = gTTS(text)
tts.save('hello.mp3')
  # Load the popular external library
mixer.init()
os.system("mpg321 hello.mp3")
mixer.music.play()