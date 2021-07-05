from flask import Flask
from flask import Flask, request, jsonify, render_template
from gpt3 import gpt3Response
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    inputs = [x for x in request.form.values()]
    response = gpt3Response(inputs)
    idea = response['choices'][0]['text'][1:]
    return render_template('index.html', prediction_text="Startup Idea: {}".format(idea))

if __name__ == '__main__':
    app.run(debug=True)
