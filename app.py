from flask import Flask

app = Flask(__name__)

api = Flask('api')


@api.route('/')
def index():
    return "WORKING"

if __name__ == '__main__':
    app.run(debug=True)
