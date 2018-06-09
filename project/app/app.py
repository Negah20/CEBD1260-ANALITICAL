from flask import Flask, render_template, request  # TODO: install libraries
from sklearn.externals import joblib

app = Flask(__name__, static_url_path='/static/')
@app.route("/")
def main():
     return render_template('index.html')
    
@app.route('/predict_rides', methods = ['POST', 'GET'])
def predict_rides():

    # get the parameters
    hour = float(request.form['hour'])
    day = float(request.form['day'])
    month = float(request.form['month'])
    temperature = float(request.form['temperature'])
  
    # load the model and predict
    model = joblib.load('../../model/regression.pkl') # TODO: fix path to folder
    prediction = model.predict([[hour, day, month, temperature]])
    print(prediction)
    predicted_rides = prediction.round(1)[0]

    return render_template('results.html',
                           hour=int(hour),
                           day=int(day),
                           month=int(month),
                           temperature=int(temperature),
                           predicted_rides="{:,}".format(predicted_rides)
                           )

if __name__ == '__main__':
    app.run(debug=True)


