#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import pipeline


# In[ ]:


model_name="sshleifer/distilbart-cnn-12-6"
tokenizer="sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization",model=model_name,tokenizer=tokenizer)


# In[ ]:


import serial
import speech_recognition as sr
# import spacy

# Initialize the serial port
ser = serial.Serial('COM3', 9600)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Load English language model for spaCy
# nlp = spacy.load("en_core_web_sm")

def speech_to_text():
    print("speak")
    data = ser.readline().decode().strip()
    print("Peak to Peak Amplitude:", data)

    # Perform speech recognition
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Listen for 5 seconds
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Summarize the recognized text
        # summary = summarize_text(text)
        # print("Summary:", summary)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.WaitTimeoutError:
        print("Timeout listening for speech")
    except TimeoutError:
        print("Timeout listening for speech")
    return text

def summarize_text(text):
    #print(text)
    #print(len(text))
    length=len(text)//6
    #print(length)
    min=len(text)//9
    # print(min)
    summary = summarizer(text, max_length=length, min_length=min, do_sample=False)
    
    return summary

if __name__ == "__main__":
    # Convert speech to text
    recognized_text = speech_to_text()
    if recognized_text:
        print("Original Text:", recognized_text)
        
        # Summarize text
        summarized_text = summarize_text(recognized_text)
        print("Summarized Text:", summarized_text)


# In[ ]:




