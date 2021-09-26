import json

expected = json.loads(
    """
{
    "result": [
        {"id": 1, "name": "task-1", "status": 0}
    ]
}
"""
)


def test_add_task(app):
    """Ensure a new user can be added to the database."""
    with app.test_client() as client:
        response = client.post(
            "/task",
            data=json.dumps(dict(name="task-1")),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert "task-1" in data["name"]
        assert 0 == data["status"]


def test_get_tasks(app):
    """Ensure a new user can be added to the database."""
    with app.test_client() as client:
        response = client.get(
            "/tasks",
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert expected == data


def test_update_task(app):
    """Ensure a new user can be added to the database."""
    with app.test_client() as client:
        response = client.put(
            "/task/1",
            data=json.dumps(dict(name="task-1-update", status=1)),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert "task-1-update" in data["name"]
        assert 1 == data["status"]


def test_delete_task(app):
    """Ensure a new user can be added to the database."""
    with app.test_client() as client:
        response = client.delete(
            "/task/1",
            content_type="application/json",
        )

        # data = json.loads(response.data.decode())
        assert response.status_code == 200
