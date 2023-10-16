from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model

model = "model/ws_new.keras"
image_path = "paper15.jpg"
class_names = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']

def predict_class(image_path, model):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize the image

    # Make predictions
    predictions = model.predict(img)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class]
    return predicted_class_name

model1 = load_model("ws_new.keras")
print(predict_class(image_path, model1))