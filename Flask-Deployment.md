# Flask Deployment

To run the project as a f;ask application, the following changes were made to the [predict.py](https://github.com/BuzzKanga/MLZoomcamp-2023-Mid-Term-Project/blob/main/predict.py) program

1. Flask librabries were imported:
   `from flask import Flask`
   
   `from flask import request`
   
   `from flask import jsonify`

2. Flask app defined:
   `app = Flask('car_price')`

3. Decorator added to function and /predict route defined
   `@app.route('/predict', methods=['POST'])`

4. Main initiates running of app and binds it to port 9696
   `  app.run(debug=True, host='0.0.0.0', port=9696)`
