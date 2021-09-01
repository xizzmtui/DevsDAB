import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_devz.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book.html')
def book_page():
    return render_template('book.html')


@app.route('/inquiry.html')
def inquiry_page():
    return render_template('inquiry.html')


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input_data = [int(x) for x in request.form.values()]

    new_input = np.array(input_data)
    new_input = new_input.reshape(1, -1)
    prediction = model.predict(new_input)

    return render_template('index.html', prediction_text='{}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
