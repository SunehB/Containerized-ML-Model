#Flask app
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to the Iris Classification API!</h1>
    <p>This API uses a RandomForestClassifier to predict the species of an Iris plant, based on it's measurements given in the Iris dataset</p>
    <h2>The Iris Dataset</h2>
    <p>The Iris dataset is a famous dataset in machine learning, and contains the measurements for three species of Iris flowers:</p>
    <p>To use this API, send a POST request to <code>/predict</code> with the following JSON structure:</p>
    <ul>
        <li><strong>Setosa</strong> (Class 0)</li>
        <li><strong>Versicolor</strong> (Class 1)</li>
        <li><strong>Virginica</strong> (Class 2)</li>
    </ul>

    <h2>The Input Features</h2>
    <p>The input to the model consists of four measurements of a flower:</p>
    <ul>
        <li><strong>Sepal length</strong> (in cm)</li>
        <li><strong>Sepal width</strong> (in cm)</li>
        <li><strong>Petal length</strong> (in cm)</li>
        <li><strong>Petal width</strong> (in cm)</li>
    </ul>
    <h2>How to Use the API</h2>
    <p>To get a prediction, send a POST request to the <code>/predict</code> endpoint with the following JSON structure:</p>
    <pre>
    {
        "input": [5.1, 3.5, 1.4, 0.2]
    }
    </pre>
    <p>Where the numbers represent the sepal and petal measurements (length and width). The model will predict the species of the flower (0 for Setosa, 1 for Versicolor, 2 for Virginica).</p>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
    # Get data from POST request
        data = request.get_json(force=True)
        # Convert data into numpy array
        input_data = np.array(data['input']).reshape(1, -1)
        # Make prediction
        prediction = model.predict(input_data)
        # Return prediction as JSON
        return jsonify({'prediction': int(prediction[0])})
    else: 
        return "Use a POST request with JSON input to get predictions."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
