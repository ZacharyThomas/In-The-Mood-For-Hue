import requests
import json

def main():
    api_key = get_key()
    if ( api_key == "YOUR_KEY_HERE") : 
        print "Fill in your keys.txt properly doge." 
        return 
    
    img_url = "http://1.images.comedycentral.com/images/shows/nightly_show/videos/season_2/02042/ns_02_042_03.jpg"
    emotion_response = get_emotions(api_key, img_url)
    print emotion_response

def get_key(): 
    with open("keys.txt", "r") as keys:
        keysJson = json.loads(keys.read())
        return keysJson['key']        
        
def get_emotions(api_key, img_as_binary):
    request_url = "https://api.projectoxford.ai/emotion/v1.0/recognize"
    img_url = "http://1.images.comedycentral.com/images/shows/nightly_show/videos/season_2/02042/ns_02_042_03.jpg"
    
    headers = {
        'content-type' : 'application/json',
        'Ocp-Apim-Subscription-Key' : api_key
    }
    payload = { "url": img_url}

    response = requests.post(request_url, data=json.dumps(payload), headers=headers)
    return response.json()

if __name__ == '__main__':
    main()
