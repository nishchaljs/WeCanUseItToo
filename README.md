# Social Media Application for Specially Challenged

## Objective :   
Every person has an equal right to information and impairments shouldn’t restrict people from gaining this information. So, the main motive here is to make social media application, which is a source of information, more accessible to the blind,deaf and dumb. Provisions have to me made keeping in mind their difficulties and interests.

## Modules
### 1. Authentication using facial recognition
The image of the user is captured and verified with the existing images present in the database(images saved during sign up) using Haar Cascade OpenCV.
### 2. Video Transcription Using AI Speech Recognition  
Google Speech to text API is used to get real-time speech to text transcription of video posts, this will help the deaf and dumb to understand the video contents.  

### 3. Video Transcription To Sign Language Conversion - ISL Vocabulary  
The Video transcripts are further converted into ISL signlanguage using NLTK libs and dictionary based machine translation for catering to larger population of deaf and dumb  


### 4. Image Captioning and Audio Conversion using ANN and NLP  
The FLICKR_8K dataset was used. The various stages include 
a. Cleaning the caption data
b. Extracting features from images using VGG-16
c. Merging the captions and images
d. Building LSTM model for training
e. Predicting on test data
Further the text that is generated is converted to audio using google translate API. This helps the blind , to easily access the image.
### 5.Text based image and Audio conversion using OCR,Tesseract and NLP
Some images which are text based cannot be given image captions. Using OCR and Tesseract, this text is extracted. The text is further converted to audio using Google Translate API.

## STEPS TO RUN
1. Run App.ipynb in Nmit folder jupyter notebook to open the flask webapp  
2. Run main2.py in audio-to-signs folder to run the Audio to Sign Language - ISL module only
3. Run Transcription.py in Video_Transcription folder to run the Video to text transcription module only
4. Run "Image Captioning 8k.ipynb" in Image-Captioning folder to run the Image Caption generation module only
5. Run ocr.py to run the OCR to audio conversion module only
6. Run detector.py in Facia-Recognition folder to run facial recognition authentication module only

## IMAGES
<div class="row">
  <p>LOGIN PAGE</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/Login.png" alt="drawing" width="800"/>
  <br>
  <br>
  <br>
  <p>FACIAL RECOGNITION</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/Face.png" alt="drawing" width="800"/>
  <br>
    <br>
  <br>
  <p>HOME PAGE</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/Home.png" alt="drawing" width="800"/>
  <br>
    <br>
  <br>
  <p>IMAGE CAPTIONING</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/ImageCap.png" alt="drawing" width="800"/>
  <br>
    <br>
  <br>
  <p>OCR TO AUDIO</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/OCR.png" alt="drawing" width="800"/>
  <br>
    <br>
  <br>
  <p>AUDIO TO SIGN LANGUAGE</p>
<img src="https://github.com/nishchaljs/nmit2021/blob/main/Screenshots/SignLang.png" alt="drawing" width="800"/>
   </div>







