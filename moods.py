import requests
import json
import numpy as np
import cv2
import sys
import base64

def main():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    api_key = get_key()
    if ( api_key == "YOUR_KEY_HERE") : 
        print "Fill in your keys.txt properly doge." 
        return 
    
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    rval, frame = vc.read()
    
    count=0
    while True and count<10:
        
        if frame is not None:   
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            
            if len(faces)>0:
                cv2.imwrite("img"+str(count)+".jpg", frame)

                rfile = open("img"+str(count)+".jpg", "r")
                filehex = rfile.read()
                #fileb64 = base64.b64encode(filehex)
                print sys.getsizeof(filehex)
                emotion_response = get_emotions(api_key, filehex)
                print emotion_response
                count+=1


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
 
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
    #payload = { img_url}

    response = requests.post(request_url, data=img_as_binary, headers=headers)
    return response.json()

if __name__ == '__main__':
    main()
