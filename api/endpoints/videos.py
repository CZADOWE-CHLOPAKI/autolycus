from fastapi import APIRouter

from api.models.responseModels import ResponseModel
from pkg.create_video import create_video as create_video_from_memes

router = APIRouter(
    prefix="/videos",
    tags=["videos"],
)


@router.post("/create", response_description="Create video from subreddit")
async def create_video(subreddit: str, image_limit: int = 10, order: str = "hot"):
    create_video_from_memes(subreddit=subreddit, image_limit=image_limit, order=order)
    return ResponseModel(message=f"Successfully created video from: {subreddit}")
