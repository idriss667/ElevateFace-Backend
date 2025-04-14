class SubscriptionService:
    ALLOWED_PLANS = {"basic", "advanced", "fitness", "premium"}

    @staticmethod
    def subscribe_user(user_id: str, plan: str):
        if plan not in SubscriptionService.ALLOWED_PLANS:
            raise ValueError(f"Le plan '{plan}' n'existe pas frérot.")

        # Logique réelle à remplacer : sauvegarder dans ta DB
        # (simulation)
        print(f"Utilisateur {user_id} abonné au plan {plan} 💥")

        return {
            "user_id": user_id,
            "plan": plan,
            "message": f"Abonnement '{plan}' activé avec succès !"
        }