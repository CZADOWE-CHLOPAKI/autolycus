from fastapi import APIRouter
from fastapi.responses import FileResponse

from pkg.config import config as pkg_config
from pkg.create_video import create_video as create_video_from_memes

router = APIRouter(
    prefix="/videos",
    tags=["videos"],
)


@router.post("/create", response_description="Create video from subreddit")
async def create_video(subreddit: str, image_limit: int = 10, order: str = "hot"):
    create_video_from_memes(subreddit=subreddit,
                            image_limit=image_limit, order=order)
    return FileResponse(pkg_config.ProjectPaths.OUTPUT_VIDEO_MP4)
