from fastapi import FastAPI
from app.api.face import router as face_router
from app.api.subscription import router as subscription_router


app = FastAPI(title="ElevateFace API")

# Inclure tes routes
app.include_router(face_router, prefix="/api", tags=["Face Analysis"])
app.include_router(subscription_router, prefix="/api", tags=["Subscription"])


@app.get("/")
async def root():
    return {"status": "ElevateFace API is running!"}

@app.get("/")
async def root():
    return {"status": "ElevateFace API est lancé !"}