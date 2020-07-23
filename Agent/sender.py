import requests  
import json
import csv

def send(file):
    url = "http://localhost:8000/income/file"
    files = {'uploaded_file': open('{}'.format(file), 'rb')} 
    r = requests.post(url, files=files)
    print(r)
    if str(r) == '<Response [200]>':
        return 'Complete'
    else:
        return 'Something wrong'
