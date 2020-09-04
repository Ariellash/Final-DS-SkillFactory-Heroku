import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)


@app.route('/predict', methods=['POST'])
def pred_func():
    validator = request.get_json()
    df = pd.read_json(validator, orient='records')[:1].values
    price = np.exp(model.predict(df)[0])

    return jsonify({'Price': str(price)})