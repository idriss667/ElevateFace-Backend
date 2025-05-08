from fastapi import APIRouter, HTTPException

router = APIRouter()

# Utilise la même DB mock que subscribe.py pour le moment
subscriptions_db = {
    "idriss67": "premium",
    "amin": "free"
}

@router.get("/get-user-plan/{user_id}")
def get_user_plan(user_id: str):
    if user_id not in subscriptions_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user_id,
        "plan": subscriptions_db[user_id]
    }
