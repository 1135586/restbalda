from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

#from models import Scores
import models

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/', methods=['GET'])
def hello():
    score = models.Scores(user_id = 'Lololo', score = 1232, timestamp = datetime.now())
    db.session.add(score)
    db.session.commit()
    return "Hi Man!"


#@app.route('/', methods=['GET'])
#def hello():
#    return "Hi Man!"


@app.route('/scores/', methods=['GET', 'POST'])
def scores():
    #if request.method == "POST":
    return jsonify({'tasks': tasks})


#@app.route('/scores/', methods=['GET'])
#def scores():
#    return jsonify({'tasks': tasks})


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
