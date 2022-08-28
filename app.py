from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:21300/flask_weight_data'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User_data(db.Model):
    __tablename__ = 'user_data'
    email = db.Column(db.String(120), primary_key=True)

    def __init__(self, email):
        self.email = email

class Weight_data(db.Model):
    __tablename__ = 'weight_data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), db.ForeignKey('user_data.email'))
    weigth = db.Column(db.Integer)

    def __init__(self, email, weight):
        self.email = email
        self.weight = weight

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method=='POST':
        email = request.form['email_name']
        weight = request.form['weight_data']
        return render_template('success.html')

if __name__ == '__main__':
    app.debug = True
    app.run()