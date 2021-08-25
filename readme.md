# FaceRecognition Insta Api

Find the similar faces among our scrapped accounts.

The scrapped accounts can be found in this google drive 
https://drive.google.com/drive/folders/1HJCZuuWvIAPd6uIISs4Q6M4KYRl7UqBO?usp=sharing


Getting started

```python
POST http://52.56.44.23:5000/test
```


Your request should contain : 
- image encoded in base 64
- k represent the lenght of the output result (top k most similar )

example : 
```python
{
	'image': "/9j/4AAQSkZJRgABAQAAAQABAAD/7QCEUGhvdG9zaG9wIDMuMAA4QklNBAQwYTAwMGE3MDAxMDAwMDVlMDMwMDAwNDMwNjAwMDBlNDA2MDAwMDZmMDcwMDAwMGZjMGMwMDAwYWQwZDAwMDA1OTBlMDAwMGUwMTMwMDAwAP/bAEMABgQFBgUKFA4PDBAXFBgYFxQWFhodJR8aGyMcFhYgLCAjJicpKikZHy0wLSgwJSgpKP/aFhooKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgAlgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAAIDBQYBBwj/xAAAAAAAAgMBBAX/2gAMAwEAAhADEAAAAZ/QvN/SGmm9aYoJcybXCQTYyEmHzYZ",
	'token': "9989ZR9Z0RZ9",
	'k': 10
}
```

The api server will extract the faces from the received image, then will take only the first one to be our searching target. 

The response includes a persistent score and usernames along with appended attributes:

