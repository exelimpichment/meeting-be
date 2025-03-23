from fastapi import FastAPI
from .routes import user_routes

# Initialize the FastAPI app
app = FastAPI(
    title="meeting-be API",
    description="API for managing meetings",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


app.include_router(user_routes.router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the meeting-be API"}


@app.on_event("startup")
async def startup_event():

    print("Application starting...")


@app.on_event("shutdown")
async def shutdown_event():

    print("Application shutting down...")
