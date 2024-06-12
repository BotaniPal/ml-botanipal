import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from urllib.parse import quote
import io
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify
model = keras.models.load_model('C:/Users/Ghifary/OneDrive/Documents/Kuliah/BANGKIT/Deploy/plants_disease_model.h5')

def transform_image(pillow_image):
    image = Image.open(pillow_image)
    img = image.resize((150,150))
    img = img.convert('RGB')
    img = np.array(img) / 255.0  # Normalisasi
    img_array = np.expand_dims(img, axis=0)
    return img_array  # Kembalikan img_array setelah semua transformasi dilakukan

def predict(x):
    class_names = {
        0: 'Apple scab',
        1: 'Apple Black Rot',
        2: 'Apple Ceda Rust',
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
