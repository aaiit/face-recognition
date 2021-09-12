Api integration of Finding the similar faces among our scrapped accounts.


Before deploying, a steps should be done:
- [x] Scrapping users usernames & their media images & detecting and cropping faces and saving them. [kaggle notebook](https://www.kaggle.com/aithammadiabdellatif/instagram-follower-scraper-extract-faces-4)
- [x] Calculate faces embedding and saving them as pickle file. [kaggle notebook](https://www.kaggle.com/aithammadiabdellatif/27851-embending)




# Getting started

```python
POST http://52.56.44.23:5000/test
```


Your request should contain : 
- image encoded in base 64
- k anything for the moment
- token anything for the moment

## Example : 

```python
{
	'image': "/9j/4AAQSkZJRgABAQAAAQABAAD/7QCEUGhvdG9zaG9wIDMuMAA4QklNBAQwYTAwMGE3MDAxMDAwMDVlMDMwMDAwNDMwNjAwMDBlNDA2MDAwMDZmMDcwMDAwMGZjMGMwMDAwYWQwZDAwMDA1OTBlMDAwMGUwMTMwMDAwAP/bAEMABgQFBgUKFA4PDBAXFBgYFxQWFhodJR8aGyMcFhYgLCAjJicpKikZHy0wLSgwJSgpKP/aFhooKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgAlgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAAIDBQYBBwj/xAAAAAAAAgMBBAX/2gAMAwEAAhADEAAAAZ/QvN/SGmm9aYoJcybXCQTYyEmHzYZ",
	'token': "9989ZR9Z0RZ9",
	'k': 10
}
```

The api server will extract the faces from the received image, then will take only the first one to be our searching target(for the moment). 

The response includes a  scores and usernames of similar faces:

## Example response output: 
```python
{'users': [[0.024950975782138334, 'kentuckyweapon'], [0.026814208155325495, 'oliver8269'], [0.0324375883373996, 'bantengmerah__'], [0.04298306801568262, 'gany.di'], [0.049299241610240435, 'bantengmerah__'], [0.05290855386010046, 'mp5juiceman'], [0.05889903765995597, 'theyforcedmetheyhardcore'], [0.06250896244452195, 'nazinibba69'], [0.06429998815571769, 'srh_95'], [0.06828424681018239, 'shellabella1213']]}
```

# Testing from Python 
```python
import base64
import json
import requests

api = 'http://52.56.44.23:5000/test'
image_file = 'image2.jpg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "token": "******","k" : 10})

print(payload)

response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()     
    print(data["user"])       
except requests.exceptions.RequestException:
    print(response.text)
```
