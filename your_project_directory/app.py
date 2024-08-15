from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # Handle the form data securely
    print(f"Username: {username}, Password: {password}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
