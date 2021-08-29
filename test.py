import base64
import json
import requests

api = 'http://52.56.183.210:5000/test'
image_file = 'test/test.jpg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "token": "******","k" : 1000})

# print(payload)

response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json() 
    l = []    
    for i in data["results"]:
        print(i[0],i[1])   
        l.append(i[1])
    print(l.index("zouaine_youssef"))  
except requests.exceptions.RequestException:
    print(response.text)