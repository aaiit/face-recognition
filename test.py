# https://stackoverflow.com/questions/29104107/upload-image-using-post-form-data-in-python-requests
#  https://aws.amazon.com/fr/getting-started/hands-on/serve-a-flask-app/
import base64
import json
import requests

api = 'http://52.56.44.23:5000/test'
image_file = 'sample_image.jpg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "token": "2001234444424"})
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)