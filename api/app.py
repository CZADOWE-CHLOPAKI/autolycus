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
    from endpoints.user import router
    app.include_router(router)

    @app.get("/", tags=["Root"])
    async def read_root():
        return {"message": "For more API information go to /docs"}
