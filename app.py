from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

#from models import Scores
import models


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        hight_scores = models.Scores.query.order_by(desc(models.Scores.score)).first()
        return jsonify({'hight_scores': str(hight_scores.score)})
    if request.method == "POST":
        user_score = models.Scores.query.filter_by(user_id = request.json['user_id']).first()
        if user_score is None:
            new_score = models.Scores(user_id = request.json['user_id'], score = request.json['score'], timestamp = datetime.now())
            db.session.add(new_score)
            db.session.commit()
            return "201"
        user_score.score = request.json['score']
        db.session.commit()
        return "201"


if __name__ == '__main__':
    app.run()
