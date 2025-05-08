from fastapi import FastAPI
from app.routes.analyze_face import router as analyze_router
from app.routes.subscribe import router as subscribe_router
from app.routes.get_user_plan import router as plan_router

app = FastAPI(title="ElevateFace API")

# Inclure les routers (une seule fois chacun)
app.include_router(analyze_router, prefix="/api", tags=["Face Analysis"])
app.include_router(subscribe_router, prefix="/api", tags=["Subscription"])
app.include_router(plan_router, prefix="/api", tags=["Get Plan"])

@app.get("/")
async def root():
    return {"status": "ElevateFace API est lancé !"}
