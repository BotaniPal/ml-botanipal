import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from urllib.parse import quote
import io
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, storage
import requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'backend-nodejs-tes.appspot.com'
})

model = keras.models.load_model('plants_type_model.h5')

def transform_image(pillow_image):
    image = Image.open(pillow_image)
    img = image.resize((150,150))
    img = img.convert('RGB')
    img = np.array(img) / 255.0  # Normalisasi
    img_array = np.expand_dims(img, axis=0)
    return img_array  # Kembalikan img_array setelah semua transformasi dilakukan

def predict(x):
    class_names = {
        0: 'Apple',
        1: 'Bell Pepper',
        2: 'Cabbage',
        3: 'Carrot',
        4: 'Cauliflower',
        5: 'Corn',
        6: 'Grape',
        7: 'Peanut',
        8: 'Peper chili',
        9: 'Potato',
        10: 'Shallot',
        11: 'Soybeans',
        12: 'Strawberry',
        13: 'Tomato'}
    cnn_predictions = model.predict(x)
    label0 = np.argmax(cnn_predictions)
    predicted_class_name = class_names[label0]
    return predicted_class_name

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file_url = request.json.get('file_url')
        if not file_url:
            return jsonify({"error": "no file URL provided"})

        try:
            # Download the image from the provided URL
            response = requests.get(file_url)
            if response.status_code != 200:
                return jsonify({"error": "unable to download image from URL"})

            image_bytes = io.BytesIO(response.content)
            tensor = transform_image(image_bytes)
            prediction = predict(tensor)
            timestamp = datetime.now().isoformat()

            data = {
                "prediction": prediction,
                "image_url": file_url,
                "timestamp": timestamp,
            }
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)