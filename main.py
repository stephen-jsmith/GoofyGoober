import json

FILENAME = 'secretkeys.json'

print('Hello World')

with open(FILENAME, 'r') as data:
    secretKeys = json.load(data)

print((secretKeys['secret_data']))