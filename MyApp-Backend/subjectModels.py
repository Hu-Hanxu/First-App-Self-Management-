from database import db

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjectname = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(100), nullable=False)

    def __init__(self, subjectname, deadline, ):
        self.subjectname = subjectname
        self.deadline = deadline