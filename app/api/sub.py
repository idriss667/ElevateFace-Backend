from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import SubscriptionRequest, SubscriptionResponse, User
from app.services.subscription_service import SubscriptionService
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/subscribe", response_model=SubscriptionResponse)
async def subscribe_user(
    subscription: SubscriptionRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        result = SubscriptionService.subscribe_user(
            user_id=current_user.user_id,
            plan=subscription.plan
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
