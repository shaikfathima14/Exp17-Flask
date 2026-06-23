from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Welcome to Flask API!"

@app.route('/about')
def about():
    return "This is Experiment 17"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)