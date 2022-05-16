from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config.config import ALLOW_ORIGINS


def create_app():
    api_app = FastAPI()

    api_app.add_middleware(
        CORSMiddleware,
        allow_origins=[ALLOW_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return api_app


app = create_app()


@app.on_event("startup")
def register_routes():
    from endpoints.videos import router as video_router
    app.include_router(video_router, prefix="/api")
    from endpoints.images import router as image_router
    app.include_router(image_router, prefix="/api")

    @app.get("/", tags=["Root"])
    async def read_root():
        return {"message": "For more API information go to /docs"}
