from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def counter():
    if 'number' in session:
        session ['number'] = session['number']+1
    else:
        session ['number'] = 1
    return render_template("counter.html")
@app.route('/counter', methods = ['POST'])
def count_up():
    session ['number'] = session['number']+1
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session ['number'] = 0
    return redirect('/')
app.run(debug = True)
