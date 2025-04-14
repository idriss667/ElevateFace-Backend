from app.models.schemas import User

def get_current_user() -> User:
    # À remplacer plus tard par une vraie authentification JWT
    return User(user_id="12345", subscription_plan="premium")
