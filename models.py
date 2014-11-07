from datetime import datetime
from sqlalchemy import DateTime
from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    entry_type = db.Column(db.String(40))
    entry_text = db.Column(db.Text())
    created = db.Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, username, entry_type, entry_text):
        if None in [username, entry_type, entry_text]:
            raise ValidationError('One or more required fields are not '
                                  'defined')
        self.username = username
        self.entry_type = entry_type
        self.entry_text = entry_text

    def __repr__(self):
        return '<Entry %r>' % self.id


class ValidationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
