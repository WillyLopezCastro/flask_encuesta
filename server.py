from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = '131313'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    languaje = request.form['languaje']
    comment = request.form['comment']

    session['ninja'] = {
        'name': name,
        'location': location,
        'languaje': languaje,
        'comment': comment,
    }
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/inicio', methods=['GET'])
def inicio():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)