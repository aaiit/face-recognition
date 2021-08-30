import io
import json          
import base64          
import logging       
import numpy as np
from PIL import Image
from extract_faces import extract
from vggmodel import get_embending
from flask import Flask, request, jsonify, abort
import cv2
import pickle

app = Flask(__name__)

def distance(emb1, emb2):return np.sum(np.square(emb1 - emb2))



f= open('cool.pickle', 'rb') 
a, b = pickle.load(f)

prin("The len of faces in the database : ", len(a))
@app.route("/test", methods=['POST'])
def hello_insta():
   # print(request.json)     
   if not request.json or 'image' not in request.json: 
     abort(400)
       
   # get the base64 encoded string
   im_b64 = request.json['image']

   # convert it into bytes  
   img_bytes = base64.b64decode(im_b64.encode('utf-8'))

   # convert bytes data to PIL Image object
   img = Image.open(io.BytesIO(img_bytes))

   # PIL image object to numpy array
   img_arr = np.asarray(img)   
   
   print('img shape', img_arr.shape)

   # process your img_arr here  
   # extract faces
   faces = extract(img_arr)

   # Calculate embending
   embendings = [ get_embending(f) for f in faces]
   print("embendings",len(embendings))
   print(embendings[0].shape)


   # Calculate the distace
   d = sorted([ [distance(em,embendings[0]),user] for em,user in zip(b,a)])

   # get topk
   k = int(request.json["k"])
   topk = d[:k]
   # access other keys of json
   # print(request.json['token'])

   result_dict = {'results': topk,"status":"Done"}


   return result_dict

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)