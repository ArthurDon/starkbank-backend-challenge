from fastapi import FastAPI
import logging

from controllers.webhook_controller import router as webhook_router

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(webhook_router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}