# ElevateFace Backend (FastAPI)
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

# Modèle Pydantic pour la réponse d'analyse
class AnalysisResult(BaseModel):
    face_shape: str
    attractiveness_score: Optional[float] = None
    improvement_tips: Optional[list[str]] = None
    fitness_advice: Optional[list[str]] = None
    calorie_intake: Optional[int] = None

# Simuler un utilisateur avec abonnement
class User(BaseModel):
    user_id: str
    subscription_plan: str

# Dépendance pour récupérer l'utilisateur (simulé ici)
def get_current_user() -> User:
    # Cette fonction serait remplacée par une authentification réelle
    return User(user_id="12345", subscription_plan="premium")

# Service pour l'analyse des visages
class FaceAnalysisService:
    @staticmethod
    def analyze_face(image_data: bytes, plan: str) -> AnalysisResult:
        # Logique d'analyse simplifiée (à remplacer par IA réelle)
        result = AnalysisResult(face_shape="Oval")

        if plan in ["basic", "advanced", "fitness", "premium"]:
            result.attractiveness_score = 8.5
        if plan in ["advanced", "fitness", "premium"]:
            result.improvement_tips = ["Hydratez votre peau", "Dormez suffisamment"]
        if plan in ["fitness", "premium"]:
            result.fitness_advice = ["Cardio régulier", "Exercices faciaux"]
        if plan == "premium":
            result.calorie_intake = 2200

        return result

# Endpoint propre et clair
@app.post("/analyze-face", response_model=AnalysisResult)
async def analyze_face_endpoint(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Format d'image non supporté.")

    image_data = await file.read()

    # Appel du service d'analyse du visage
    analysis_result = FaceAnalysisService.analyze_face(
        image_data=image_data,
        plan=current_user.subscription_plan
    )

    return analysis_result
