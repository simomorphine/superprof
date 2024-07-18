from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dropdown_choice = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(100), nullable=False)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    upload_id = db.Column(db.Integer, db.ForeignKey('upload.id'), nullable=False)

class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction_text = db.Column(db.String(200), nullable=False)
    upload_id = db.Column(db.Integer, db.ForeignKey('upload.id'), nullable=False)
