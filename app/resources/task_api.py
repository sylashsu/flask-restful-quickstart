#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
from flasgger import swag_from
from flask import Response
from flask_restful import reqparse
from flask_restful import Resource

from app.models.task import TaskModel
from app.util.logz import create_logger


class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    parser.add_argument(
        "name", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument("status", type=bool)

    def __init__(self):
        self.logger = create_logger()

    # @swag_from('/app/docs/task/get.yml', methods=['GET'])
    def get(self, id):
        task = TaskModel.find_by_id(id)
        self.logger.info(f"returning Task: {task.json()}")
        if task:
            return task.json()
        return {"message": "Task not found"}, 404

    @swag_from("/app/docs/task/delete.yml", methods=["DELETE"])
    def delete(self, id):
        task = TaskModel.find_by_id(id)
        if task:
            task.delete_from_db()
            return Response(status=200, mimetype="application/json")
        else:
            return {
                "message": "An task with id '{}' not exists.".format(id)
            }, 400

    @swag_from("/app/docs/task/put.yml", methods=["PUT"])
    def put(self, id):
        # Create or Update
        self.logger.info(f"parsed args: {Task.parser.parse_args()}")
        data = Task.parser.parse_args()
        task = TaskModel.find_by_id(id)

        if task is None:
            return {
                "message": "An task with id '{}' not exists.".format(id)
            }, 400
        else:
            task.name = data["name"]
            task.status = data["status"]

        task.save_to_db()

        return task.json()


class Tasks(Resource):
    def __init__(self):
        self.logger = create_logger()

    @swag_from("/app/docs/task/post.yml", methods=["POST"])
    def post(self):
        self.logger.info(f"parsed args: {Task.parser.parse_args()}")
        data = Task.parser.parse_args()
        name = data["name"]

        if TaskModel.find_by_name(name):
            return {
                "message": "An task with name '{}' already exists.".format(name)
            }, 400
        task = TaskModel(name, False)

        try:
            task.save_to_db()
        except Exception as e:
            self.logger.error("Save task fail: {0}".format(e))
            return {"message": "An error occurred inserting the task."}, 500
        return task.json(), 201


class TaskList(Resource):
    def __init__(self):
        self.logger = create_logger()

    @swag_from("/app/docs/tasks/get.yml", methods=["GET"])
    def get(self):
        return {"result": [item.json() for item in TaskModel.query.all()]}
