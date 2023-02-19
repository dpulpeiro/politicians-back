import uvicorn

from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "api.app:app",
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
    )
