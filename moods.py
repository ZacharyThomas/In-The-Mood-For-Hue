import requests
import json
import numpy as np
import cv2
import sys
import base64
import serial

def main():
    
    
    api_key = get_key()
    if ( api_key == "YOUR_KEY_HERE") : 
        print "Fill in your keys.txt properly doge." 
        return 
    
    vc = cv2.VideoCapture(0)
    
   
    is_detected,hexfile = detect_face_frames(vc)
    
    while not is_detected:
        is_detected,hexfile = detect_face_frames(vc)
    
    emotion_response = get_emotions(api_key, hexfile)

    send_emotion(emotion_response)

def detect_face_frames(vc):    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rval, frame = vc.read()
    if frame is not None:   
        rval, frame = vc.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        if len(faces)>0:
            cv2.imwrite("img.jpg", frame)
            rfile = open("img.jpg", "r")
            filehex = rfile.read()
            return (True,filehex)
        else: 
            return (False,None)
    else:
        return (False,None)
 
def get_key(): 
    with open("keys.txt", "r") as keys:
        keysJson = json.loads(keys.read())
        return keysJson['key']        
        
def get_emotions(api_key, img_as_binary):
    request_url = "https://api.projectoxford.ai/emotion/v1.0/recognize"
    img_url = "http://1.images.comedycentral.com/images/shows/nightly_show/videos/season_2/02042/ns_02_042_03.jpg"
    
    headers = {
        'content-type' : 'application/octet-stream',
        'Ocp-Apim-Subscription-Key' : api_key
    }

    response = requests.post(request_url, data=img_as_binary, headers=headers)
    return get_max(response.json())
    
def get_max(resp):
    emotion_scores = resp[0]['scores']
    return max(emotion_scores.iterkeys(), key=(lambda key: emotion_scores[key]))
    
def send_emotion(emotion):
    print "Emotion: " + emotion
    ser = serial.Serial('/dev/cu.usbmodem1421', 9600)    
    if(emotion == "anger"):
        ser.write('a'.encode())
    elif(emotion == "neutral"):
        ser.write('n'.encode())
    elif(emotion == "sadness"):
        ser.write('s'.encode())
    elif(emotion == "disgust"):
        ser.write('d'.encode())
    elif(emotion == "contempt"):
        ser.write('c'.encode())
    elif(emotion == "fear"):
        ser.write('f'.encode())
    elif(emotion == "happiness"):
        ser.write('h'.encode())
    elif(emotion == "surprise"):
        ser.write('x'.encode())


        
    print "We did it! :)"

if __name__ == '__main__':
    main()
