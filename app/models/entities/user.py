from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True, index=True)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
