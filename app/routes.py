from flask import Blueprint, request, jsonify
from app.services import create_meal, list_meals, list_healthy_meals

routes = Blueprint("routes", __name__)

@routes.route("/meals", methods=["POST"])
def add_meal():
    data = request.json

    meal = create_meal(
        name=data["name"],
        calories=data["calories"],
        healthy=data["healthy"]
    )

    return jsonify(meal.to_dict()), 201


@routes.route("/meals", methods=["GET"])
def get_meals():
    meals = list_meals()
    return jsonify([meal.to_dict() for meal in meals])


@routes.route("/meals/healthy", methods=["GET"])
def get_healthy_meals():
    meals = list_healthy_meals()
    return jsonify([meal.to_dict() for meal in meals])
