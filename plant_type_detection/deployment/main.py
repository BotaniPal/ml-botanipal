import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from urllib.parse import quote
import io
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify

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
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            image_bytes = file.read()
            tensor = transform_image(io.BytesIO(image_bytes))
            prediction = predict(tensor)
            data = {"prediction": prediction}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)