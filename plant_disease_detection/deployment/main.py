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

model = keras.models.load_model('plants_disease_model.h5')

def transform_image(pillow_image):
    image = Image.open(pillow_image)
    img = image.resize((150,150))
    img = img.convert('RGB')
    img = np.array(img) / 255.0  # Normalisasi
    img_array = np.expand_dims(img, axis=0)
    return img_array

def predict(x):
    class_names = {
        0: 'Apple Scab',
        1: 'Apple Black Rot',
        2: 'Apple Cedar Rust',
        3: 'Apple Healthy',
        4: 'Blueberry Healthy',
        5: 'Cherry Powdery Mildew',
        6: 'Cherry Healthy',
        7: 'Corn Cercospora Leaf Spot Gray Leaf Spot',
        8: 'Corn Common rust',
        9: 'Corn Northern Leaf Blight',
        10: 'Corn Healthy',
        11: 'Grape Black Rot',
        12: 'Grape Esca (Black Measles)',
        13: 'Grape Leaf blight (Isariopsis Leaf Spot)',
        14: 'Grape Healthy',
        15: 'Orange Haunglongbing (Citrus Greening)',
        16: 'Peach Bacterial_spot',
        17: 'Peach Healthy',
        18: 'Pepper,_Bell Bacterial Spot',
        19: 'Pepper,_Bell Healthy',
        20: 'Potato Early Blight',
        21: 'Potato Late Blight',
        22: 'Potato Healthy',
        23: 'Raspberry Healthy',
        24: 'Soybean Healthy',
        25: 'Squash Powdery Mildew',
        26: 'Strawberry Leaf Scorch',
        27: 'Strawberry Healthy',
        28: 'Tomato Bacterial Spot',
        29: 'Tomato Early Blight',
        30: 'Tomato Late Blight',
        31: 'Tomato Leaf Mold',
        32: 'Tomato Septoria Leaf Spot',
        33: 'Tomato Spider Mites Two-spotted Spider Mite',
        34: 'Tomato Target Spot',
        35: 'Tomato Tomato Yellow Leaf Curl Virus',
        36: 'Tomato Mosaic Virus',
        37: 'Tomato Healthy'}
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

