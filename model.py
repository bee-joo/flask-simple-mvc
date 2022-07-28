from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):

    __tablename__ = "clients"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(80), nullable=False)
    post_index = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(150), nullable=False)
  
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
