# -*- coding: utf-8 -*-
from app import app, db


class Users(db.Model):
    tablename = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    fullname = db.Column(db.String(255))

    def __repr__(self):
        return '<User: {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def delete(self):
        db.session.delete(self)
        db.session.commit()