# Example backend for Project 1
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Project 1 Backend!'

if __name__ == '__main__':
    app.run(debug=True)
