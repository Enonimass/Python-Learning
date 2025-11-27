from flask import *
import datetime
import requests

app= Flask(__name__)



@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template('index.html', current_year = year)


@app.route("/guess/<name>")
def guess(name) :

    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    age_response = requests.get(age_url)
    age_data =  age_response.json()
    age = age_data['age']

    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender =gender_data['gender']

    return render_template('guess.html', my_name = name, my_age=age, my_gender= gender)

if __name__ == '__main__':
    app.run(debug=True)