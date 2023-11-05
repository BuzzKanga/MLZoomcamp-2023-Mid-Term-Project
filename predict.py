# flask program that will serve the model

import pickle

from flask import Flask
from flask import request
from flask import jsonify

# load model and dv
input_file = 'model_reg.bin'

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# set-up flask app
app = Flask('car_price')

# crate path to predict function that responds to post function
@app.route('/predict', methods=['POST'])
def predict():
    car = request.get_json()

    X = dv.transform([car])
    y_pred = model.predict(X)[0]
    
    result = {
        'car_price': int(y_pred),
    }

    return jsonify(result)

# run car_price flask app 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
