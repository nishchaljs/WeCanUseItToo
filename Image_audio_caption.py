import pytesseract
import matplotlib.pyplot as plt
import cv2
import os
import win32com.client 

r = requests.post(
                    "https://api.deepai.org/api/densecap",
                    files={
                        'image': open(r'C:\Users\nishc_omjn2ty\OneDrive\Desktop\Nmit\Nmit\images\feedPhoto.jpg', 'rb'),
                    },
                    headers={'api-key': '5a639662-a646-4656-8536-355046329996'}
                )
                print(r.json()['output']['captions'][0]['caption'])
                text = r.json()['output']['captions'][0]['caption']
                tts = gTTS((r.json()['output']['captions'][0]['caption']))
                tts.save('hello.mp3')
                speaker = win32com.client.Dispatch("SAPI.SpVoice")
                speaker.Speak(text)