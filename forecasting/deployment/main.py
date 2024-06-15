import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model once when the server starts
model = load_model('bawang_merah_forecasting.h5')
time_step = 10
file_path = 'bawang_merah_mean.csv'  # Declare the file path in the program

def load_and_preprocess_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['tanggal'] = pd.to_datetime(data['tanggal'])
        data.set_index('tanggal', inplace=True)
        data = data.drop(columns=['no'])
        return data
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error loading data: {str(e)}")

def fit_scaler(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data['hrg'] = scaler.fit_transform(data['hrg'].values.reshape(-1, 1))
    return data, scaler

def get_future_steps(data, future_date):
    last_date = data.index[-1]
    future_steps = (future_date - last_date).days
    if future_steps <= 0:
        raise ValueError("The future date must be later than the last date in the dataset.")
    return future_steps

def generate_predictions(model, last_sequence, future_steps, time_step):
    for _ in range(future_steps):
        input_sequence = last_sequence.reshape((1, time_step, 1))
        next_prediction = model.predict(input_sequence)
        last_sequence = np.append(last_sequence[1:], next_prediction)[-time_step:]
    return next_prediction

def rescale_prediction(scaler, prediction):
    return scaler.inverse_transform(np.array(prediction).reshape(-1, 1))

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            if 'future_date' not in data:
                return jsonify({'error': "Invalid request data. 'future_date' is required."}), 400
            
            future_date_str = data['future_date']
            future_date = pd.to_datetime(future_date_str)
            
            # Load and preprocess data
            data = load_and_preprocess_data(file_path)
            
            # Fit the scaler with the original data
            data, scaler = fit_scaler(data)
            
            # Calculate the number of future steps
            future_steps = get_future_steps(data, future_date)
            
            # Extract the last sequence from the data
            last_sequence = data.values[-time_step:]
            
            # Generate predictions for the specified future steps
            final_prediction = generate_predictions(model, last_sequence, future_steps, time_step)
            
            # Rescale the final prediction back to the original scale
            final_prediction = rescale_prediction(scaler, final_prediction)
            
            # Return the final prediction
            return jsonify({'predicted_price': int(final_prediction[0, 0])})
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except Exception as e:
            return jsonify({'error': 'An error occurred during prediction: ' + str(e)}), 500
    
    return "OK"

if __name__ == "__main__":
    app.run(port=5000, debug=True)