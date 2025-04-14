from app.models.schemas import AnalysisResult

class FaceAnalysisService:
    @staticmethod
    def analyze_face(image_data: bytes, plan: str) -> AnalysisResult:
        """
        Analyse l'image du visage selon le plan d'abonnement.
        Tu peux remplacer la logique par de l'IA plus tard (DeepFace, Mediapipe, etc.).
        """

        # Simule la reconnaissance de forme du visage
        result = AnalysisResult(face_shape="Oval")  # <- à remplacer par algo réel plus tard

        # Analyse selon le plan d'abonnement
        if plan in ["basic", "advanced", "fitness", "premium"]:
            result.attractiveness_score = 8.5

        if plan in ["advanced", "fitness", "premium"]:
            result.improvement_tips = [
                "Hydrate ta peau frérot 💧",
                "Dors minimum 7h par nuit 🛌",
                "Évite les sucres rapides 🍭"
            ]

        if plan in ["fitness", "premium"]:
            result.fitness_advice = [
                "Cardio 3x par semaine 🏃‍♂️",
                "Renforcement facial 10 min/jour 💪😮",
            ]

        if plan == "premium":
            result.calorie_intake = 2200  # Valeur personnalisée possible plus tard

        return result
