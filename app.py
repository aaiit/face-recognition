import io
import json          
import base64          
import logging       
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

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
   
   # access other keys of json
   print(request.json['token'])

   result_dict = {'output': []}

   for i in range(10):
      result_dict["output"].append({"username":"coco","distance":33})


   return result_dict

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)