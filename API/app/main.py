from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from app.services.liefecycletasks import StartupManager
from app.dependencies import password_utils_instance
from app.routers import auth

# Initialize the FastAPI app
app = FastAPI(
    title="CoupleFlow API",
    description="An API for managing shared tasks, budgets, and more.",
    version="1.0.0",
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    StartupManager.init();
    yield # App Logic
    StartupManager.dispose();


# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "API is running smoothly 🚀"}
