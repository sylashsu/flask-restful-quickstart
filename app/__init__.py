#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
import os

from flask import Flask
from flask import jsonify

basedir = os.path.abspath(os.path.dirname(os.pardir))


def create_app(config=None):

    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["DEBUG"] = True
    elif config == "TEST":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(
            basedir, "tasks.db"
        )
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_ECHO"] = True
        app.config["DEBUG"] = True
        app.config["TEST"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(
            basedir, "tasks.db"
        )

    @app.before_first_request
    def create_tables():
        from app.db import db

        db.init_app(app)
        db.create_all()

    @app.route("/ping", methods=["GET"])
    def ping_pong():
        return jsonify({"status": "Success", "message": "pong!"}), 200

    return app
