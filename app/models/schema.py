from pydantic import BaseModel
from typing import Optional

class AnalysisResult(BaseModel):
    face_shape: str
    attractiveness_score: Optional[float] = None
    improvement_tips: Optional[list[str]] = None
    fitness_advice: Optional[list[str]] = None
    calorie_intake: Optional[int] = None

class User(BaseModel):
    user_id: str
    subscription_plan: str

class SubscriptionRequest(BaseModel):
    plan: str  # "basic", "advanced", "fitness", "premium"

class SubscriptionResponse(BaseModel):
    user_id: str
    plan: str
    message: str

