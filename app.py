from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()

def homepage():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            pclass = int(request.form.get('pclass'))
            sex = request.form.get('sex')
            age = float(request.form['age'])
            sibsp = int(request.form['sibsp'])
            parch = int(request.form['parch'])
            fare = float(request.form['fare'])
        
            sex_one = ['female', 'male']
            sex_list = []
            for i in sex_one:
                if sex == i:
                    a = 1
                    sex_list.append(a)
                else:
                    a = 0
                    sex_list.append(a)

            li = [pclass, age, sibsp, parch, fare]
            li = li + sex_list
            model = pickle.load(open('titanic_one.pickle', 'rb'))
            result = model.predict([li])

            if result == 1:
                new_data = "Person is Survived"
            else:
                new_data = "Person is Not Survived"

            return render_template('result.html', data=new_data)

        except Exception as e:
            print('Exception is ', e)
            return "something is going wrong"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)