from database import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __init__(self, name, time, location):
        self.name = name
        self.time = time
        self.location = location
