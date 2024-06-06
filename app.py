from flask import Flask, render_template, request
import requests
import pyrebase
import json

app = Flask(__name__)

# Firebase configuration
config = {
    "apiKey": "AIzaSyAO7iD2zmwoZ6LoYPj8RcwUVoIBmTaCeQs",
    "authDomain": "projectleman-f8032.firebaseapp.com",
    "projectId": "projectleman-f8032",
    "storageBucket": "projectleman-f8032.appspot.com",
    "messagingSenderId": "267953335885",
    "appId": "1:267953335885:web:aced570e05d90c69603604",
    "measurementId": "G-EERZZDL05H",
    "databaseURL": ""  # Add your Firebase database URL here
}

base_url = 'http://api.alquran.cloud/v1/page/2/quran-uthmani'
current_page = 1


def get_quran_data():
    response = requests.get(base_url)
    print(json.dumps(response.json(), indent=4))
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/home')
def homepage():
    global current_page
    quran_data = get_quran_data()
    return render_template('ayam.html', quran_data=quran_data)


@app.route('/next', methods=['POST'])
def next_page():
    global current_page
    current_page += 1
    return homepage()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.create_user_with_email_and_password(email, password)
            print("User created successfully:", user)
            return "User created successfully!"
        except Exception as e:
            error_message = e.args[1]
            return render_template('index.html', error=error_message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)