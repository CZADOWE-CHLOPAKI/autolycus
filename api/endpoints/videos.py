from fastapi import APIRouter

from api.models.responseModels import ResponseModel

router = APIRouter(
    prefix="/videos",
    tags=["users"],
)


@router.post("", response_description="Create video from subreddit")
async def get_users(subreddit: str):
    return ResponseModel(message=f"Successfully created video from: {subreddit}")
