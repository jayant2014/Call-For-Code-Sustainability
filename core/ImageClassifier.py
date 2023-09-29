import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Function to classify waste type
def classify_waste(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    predictions = model.predict(x)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    return decoded_predictions[0][1]  # Get the top predicted class

# Example usage
image_path = 'path_to_waste_image.jpg'
predicted_class = classify_waste(image_path)
print(f'Predicted waste type: {predicted_class}')
