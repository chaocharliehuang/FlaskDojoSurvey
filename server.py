from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def display_info():
    name = request.form['name']
    location = request.form['location']
    favlang = request.form['favlang']
    comment = request.form['comment']
    return render_template('user.html', name=name, location=location, favlang=favlang, comment=comment)

app.run(debug=True)