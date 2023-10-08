from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the trained model
model = None  # Load your trained model here

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = image.load_img(file, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalize the image

        # Make predictions
        predictions = model.predict(img)

        # Get the predicted class
        predicted_class = np.argmax(predictions)

        return jsonify({'class': predicted_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
