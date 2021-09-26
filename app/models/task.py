#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from app.db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def json(self):
        return {"id": self.id, "name": self.name, "status": int(self.status)}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all_tasks(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
