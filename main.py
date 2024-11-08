from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from dependencies import Container
from api.v1.endpoints import router as api_v1_router
from config import get_settings

settings = get_settings()


container = Container()

app = FastAPI(
    title=settings.PROJECT_NAME,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_v1_router, prefix=settings.API_V1_STR)

# Wire container
container.wire(packages=["."])

@app.on_event("startup")
async def startup_event():
    init_db()
