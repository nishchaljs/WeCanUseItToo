# nmit2021 - Social Media Application for Specially Challenged

## Objective :   
Every person has an equal right to information and impairments shouldn’t restrict people from gaining this information. So, the main motive here is to make social media application, which is a source of information, more accessible to the blind,deaf and dumb. Provisions have to me made keeping in mind their difficulties and interests.

## Modules
### 1. Video Transcription Using AI Speech Recognition  
Google Speech to text API is used to get real-time speech to text transcription of video posts, this will help the deaf and dumb to understand the video contents.  

### 2. Video Transcription To Sign Language Conversion - ISL Vocabulary  
The Video transcripts are further converted into ISL signlanguage using NLTK libs and dictionary based machine translation for catering to larger population of deaf and dumb  


### 3. Image Captioning and Audio Conversion using ANN and NLP  
The FLICKR_8K dataset was used. The various stages include 
a. Cleaning the caption data
b. Extracting features from images using VGG-16
c. Merging the captions and images
d. Building LSTM model for training
e. Predicting on test data
Further the text that is generated is converted to audio using google translate API. This helps the blind , to easily access the image.
### 4.Text based image and Audio conversion using OCR,Tesseract and NLP
Some images which are text based cannot be given image captions. Using OCR and Tesseract, this text is extracted. The text is further converted to audio using Google Translate API.
## To be done:  
### 5. Backend Integration





