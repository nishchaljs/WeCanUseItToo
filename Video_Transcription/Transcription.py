import cv2 
import numpy as np 
import time
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import _thread
import speech_recognition as sr 
import moviepy.editor as mp


# In[20]:


AUDIO_FILE = r"sample.mp4"
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(AUDIO_FILE)
clip = mp.VideoFileClip(AUDIO_FILE) 
clip.audio.write_audiofile(r"converted.wav")
print("AUDIO_FILE obtained")


# # Video Transciption

# In[21]:


def print_time(result): 
    for i in range(len(result)):
        if(result[i] in arr):
                ImageAddress = r'letters\\' + result[i]+'.jpg'
                ImageItself = Image.open(ImageAddress)
                ImageNumpyFormat = np.asarray(ImageItself)
                ImageNumpyFormat = cv2.resize(ImageNumpyFormat,(224,224))
                cv2.imshow('signs', ImageNumpyFormat)
                cv2.waitKey(200)
        else:
                cv2.waitKey(200)
                continue

arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")
   
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file")

i= time.perf_counter()
x = 0
   
# Read until video is completed 
while(cap.isOpened()):
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True: 
   
    # Display the resulting frame
    frame = cv2.resize(frame,(512,512))
    cv2.imshow('Frame', frame)
    j = time.perf_counter()
    if(j-i > x):
        with audio as source:
            audio_file = r.record(source, duration=30, offset = x)
        result = r.recognize_google(audio_file)
        _thread.start_new_thread(print_time, (result,) )
        print(result)
        x+=30
   
    # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows() 


# In[ ]:




