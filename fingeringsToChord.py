import requests

string = ""
fing = input('Enter fingerings: ')
address = 'http://api.uberchord.com/v1/chords?voicing='
for i in fing:
    if (i != ' '):
        string = string + i + "-"

url = address + string
json_data = requests.get(url).json()
string = string[:-1]

for key in json_data:
    for value in key:
        if(value == 'chordName'):
            final = (key.get(value))

print(final)