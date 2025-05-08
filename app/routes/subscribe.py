from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SubscribeRequest(BaseModel):
    user_id: str
    plan: str  # "free", "basic", "premium", "ultimate"

subscriptions_db = {}  # à remplacer par la DB plus tard

@router.post("/subscribe")
def subscribe_user(data: SubscribeRequest):
    if data.plan not in ["free", "basic", "premium", "ultimate"]:
        raise HTTPException(status_code=400, detail="Invalid plan")
    
    subscriptions_db[data.user_id] = data.plan
    return {"status": "success", "user_id": data.user_id, "plan": data.plan}
