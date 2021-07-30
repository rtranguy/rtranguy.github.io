from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort, redirect, url_for
from flask import Flask, flash, redirect, render_template, request, url_for
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('nyc_model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('main2.html')


@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')


@app.route('/convertcsv.htm')
def comment_summary():
    return render_template('convertcsv.htm')

@app.route('/nyc_decisiontree2.html')
def nyc_decisiontree2():
  return render_template('nyc_decisiontree2.html')

@app.route('/gmap_plot.html')
def gmap_plot():
  return render_template('gmap_plot.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('main2.html', prediction_text='Predicted rent : $ {} per day.'.format(output) )


if __name__ == '__main__':
    app.run(debug=True)
