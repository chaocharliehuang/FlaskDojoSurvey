from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def display_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form['favlang']
    session['comment'] = request.form['comment']
    
    if len(session['name']) < 1:
        flash('Name cannot be blank!')
        return redirect('/')
    if len(session['comment']) < 1:
        flash('Comment cannot be blank!')
        return redirect('/')
    if len(session['comment']) > 120:
        flash('Comment must be shorter than 120 characters!')
        return redirect('/')

    return render_template('user.html')

app.run(debug=True)