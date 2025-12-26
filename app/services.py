from app.database import db
from app.models import Meal

def create_meal(name: str, calories: int, healthy: bool):
    meal = Meal(name=name, calories=calories, healthy=healthy)
    db.session.add(meal)
    db.session.commit()
    return meal

def list_meals():
    return Meal.query.all()

def list_healthy_meals():
    return Meal.query.filter_by(healthy=True).all()
