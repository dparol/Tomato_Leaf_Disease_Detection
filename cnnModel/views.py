from django.shortcuts import render, redirect
from .models import ImageUpload
from tensorflow.keras.models import load_model

# Create your views here.
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
# Keras
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


model_path = "C:\\Users\\hp\\Downloads\\tomato_leaf_disease_detection\\tomato_leaf_disease_detection\\TomatoLeaf_disease_detection\\cnnModel\\model_inception.h5"
model = load_model(model_path)



def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        new_upload = ImageUpload(image=image)
        new_upload.save()
        saved_img_path = new_upload.image.path

        disease_prediction=model_predict(saved_img_path,model)
        print(disease_prediction)
    uploads = ImageUpload.objects.all()
    
    return render(request, 'upload.html',{'uploads': uploads,'disease_prediction':disease_prediction})










def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="Bacterial_spot"
    elif preds==1:
        preds="Early_blight"
    elif preds==2:
        preds="Late_blight"
    elif preds==3:
        preds="Leaf_Mold"
    elif preds==4:
        preds="Septoria_leaf_spot"
    elif preds==5:
        preds="Spider_mites Two-spotted_spider_mite"
    elif preds==6:
        preds="Target_Spot"
    elif preds==7:
        preds="Tomato_Yellow_Leaf_Curl_Virus"
    elif preds==8:
        preds="Tomato_mosaic_virus"
    else:
        preds="Healthy"
       
   
   
    return preds
