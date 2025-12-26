import json
from app.main import create_app
from app.database import db

def setup_app():
    app = create_app(testing=True)
    client = app.test_client()

    with app.app_context():
        db.create_all()

    return app, client


def test_create_meal():
    app, client = setup_app()

    response = client.post(
        "/meals",
        data=json.dumps({
            "name": "Rice and Beans",
            "calories": 400,
            "healthy": True
        }),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.json["name"] == "Rice and Beans"


def test_list_meals():
    app, client = setup_app()

    response = client.get("/meals")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_list_healthy_meals():
    app, client = setup_app()

    response = client.get("/meals/healthy")
    assert response.status_code == 200
