import numpy as np
import random
from flask import Flask
from flask import render_template
from model import model

app = Flask(__name__)

model1 = model(False)

#to render stuff to index.html
@app.route('/')
@app.route('/index')
def index():
    # assuming you are predicting 2 values from your ml model
    #class_name_val = random.sample(['Things that look like DVDs', 'The ghost of Groot', 'Erlic','Bus','hooli'],1)[0]
    #probability_val = int(random.sample([1,2,6,3,8,5],1)[0])/10

    predictions = model1.inference() 
    class_name_val = predictions[0]
    probability_val = predictions[1]
    real_val = predictions[2] 

    return render_template('index.html', class_name=class_name_val, probability=probability_val, real = real_val)

app.run(debug=True)