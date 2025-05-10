from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask! now cicd should work and this is the change from another dev"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
