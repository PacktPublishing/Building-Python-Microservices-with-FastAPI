from flask import Flask

app = Flask(__name__)

from ch11_flask.api import schedule

if __name__ == '__main__':
    app.run()