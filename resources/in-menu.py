from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    returns 'Hello %s!' % name

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
