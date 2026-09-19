from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from app.routers.recommendations import router as recommendations_router
except ImportError:
    from routers.recommendations import router as recommendations_router

app = FastAPI(
    title="FitFlow AI Service",
    description="Microservice providing machine learning recommendations and flow analysis for FitFlow.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendations_router)

@app.get("/")
def read_root():
    return {
        "service": "FitFlow AI Service",
        "status": "online",
        "docs": "/docs",
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "healthy": True,
    }
