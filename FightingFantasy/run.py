from flask import Flask, render_template
import sqlite3

# configuration
DATABASE = '/tmp/fight.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()