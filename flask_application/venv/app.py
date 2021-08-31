import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input_data = [float(x) for x in request.form.values()]

    new_input = np.array(input_data)
    new_input = new_input.reshape(1, -1)
    prediction = model.predict(new_input)

    return render_template('index.html', prediction_text='{}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
