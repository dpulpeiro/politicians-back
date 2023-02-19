from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routers import register_routers
from config import settings

app = FastAPI(
    title="Politicians API",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routers(app)
