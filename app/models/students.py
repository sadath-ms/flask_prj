from app.extensions import db

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    grades = db.Column()
    marks = db.Column()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    roll_num = db.Column()
    name = db.Column()
    marks = db.Column()

