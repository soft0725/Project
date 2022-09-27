from flask import Flask, render_template, request
from model import predict
import numpy as np

app = Flask(__name__)

@app.route('/')
def formpage():
    return render_template('mainpage.html')

@app.route('/resultpage',methods=['POST'])
def view():
    data1 = request.form['search1']
    data1 = float(data1)
    data2 = request.form['search2']
    data2 = float(data2)
    data3 = request.form['search3']
    data3 = float(data3)
    data4 = request.form['search4']
    data4 = float(data4)

    data = [data1, data2, data3, data4]

    return render_template('resultpage.html',data1=data1, data2=data2, data3=data3, data4=data4, result=predict(data))


if __name__ == "__main__":
    app.run()