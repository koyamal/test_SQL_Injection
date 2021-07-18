from flask import Flask, render_template, request
from thread_sqlite import select_injection

app = Flask(__name__)
app.secret_key = 'ast6S4DFbed3ds4Fs45aHfa'


@app.route('/')
def top():
    return render_template('index.html', data=[])

@app.route('/inputName', methods=['POST'])
def receiveName():
    injection = request.form.get('content', '')
    return render_template('index.html', data=select_injection(injection))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
