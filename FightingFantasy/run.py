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

@app.route('/encounter')
def encounter():
    return render_template('encounter.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()