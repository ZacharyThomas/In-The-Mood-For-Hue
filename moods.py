import requests
import json

def main():
    with open("key.txt", "r") as keys:
        keysJson = json.loads(keys.read())
        key = keysJson['key']        
    print key


if __name__ == '__main__':
    main()
