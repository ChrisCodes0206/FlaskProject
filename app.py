# Don't forget to run the env
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('scaling.html')

@app.route('/scaling')
def scaling_page():
    return render_template('scaling.html')

@app.route('/addition')
def addition_page():
    return render_template('addition.html')

if __name__ == "__main__":
    app.run(debug=True)