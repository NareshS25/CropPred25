from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('result_model.pkl', 'rb'))

app = Flask(__name__, template_folder='C:\\Users\\NARESH S\\OneDrive\\Desktop\\Apna\\Real\\template')




@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = float(request.form['a'])  # Convert to float
    data2 = float(request.form['b'])  # Convert to float
    data3 = float(request.form['c'])  # Convert to float
    data4 = float(request.form['d'])  # Convert to float
    data5 = float(request.form['e'])  # Convert to float
    data6 = float(request.form['f'])  # Convert to float
    data7 = float(request.form['g'])  # Convert to float

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('final.html', data=pred)



if __name__ == "__main__":
    app.run(debug=True)















