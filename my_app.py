from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import json
from flask import Flask, request, app, jsonify, render_template, url_for

app = Flask(__name__)

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

    #return jsonify({'class': predicted_class_name})

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    model1 = load_model("ws_new.keras")
    classname = predict_class(image_path, model1)
    return render_template("index.html", prediction_text="Categorized waste {}".format(classname))


if __name__ == "__main__":
    app.run(debug=True)
