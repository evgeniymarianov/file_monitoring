import requests  
import json

url = "http://localhost:8000/income/file"
files = {'uploaded_file': open('/home/evgen/AG9VnoDOXO0.jpg', 'rb')} 
r = requests.post(url, files=files)
print(r)
