import requests

string = ""

address = 'http://api.uberchord.com/v1/chords/'
chord = input('Enter a chord: ')
url = address + chord
json_data = requests.get(url).json()

for key in json_data:
    for value in key:
        if (value == 'strings'):
            fingering = (key.get(value))

for string in fingering:
    print(string)



