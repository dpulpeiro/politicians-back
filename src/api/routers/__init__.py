from fastapi import FastAPI

from api.routers import bulk, politicians, statistics


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(bulk.router)
    app.include_router(politicians.router)
    app.include_router(statistics.router)
    return app
