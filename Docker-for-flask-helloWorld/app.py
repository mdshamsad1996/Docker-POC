from flask import Flask,current_app

app = Flask(__name__)
@app.route('/hello')
def hello():
    current_app.logger.info('hello world test log')
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
