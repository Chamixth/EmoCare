from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'home')

@app.route("/doctor")
def doctor():
    return render_template('doctor.html')

@app.route("/patient")
def patient():
    return render_template('patient.html')


# To run this code in the command prompt write : python flaskpage.py
if __name__ == '__main__':
    app.run(debug = True)