# from fastapi.responses import FileResponse
from fastapi import APIRouter
from api.database.database import add_user
from api.models.responseModels import ResponseModel
# from api.database.database import add_user

# from pkg.get_images import get_images as get_images_from_subreddit
router = APIRouter(
    prefix="/images",
    tags=["images"],
)


@router.get("/downloadtoserver", response_description="Get images from subreddit to server")
async def downloadtoserver(subreddit: str = 'memes', image_limit: int = 10, order: str = "hot"):
    # imagePaths = get_images_from_subreddit(subreddit=subreddit,
    #    image_limit=image_limit, order=order)

    # TODO ssave image paths in db
    # TODO add error handling
    return ResponseModel(message=f"downloaded {image_limit} images to server from {subreddit}")


@router.get("/{image_idx}", response_description="Get images from subreddit")
async def image_idx(image_idx: int, subreddit: str = 'memes'):
    # TODO get path from db for the correct image
    # print(image_idx)
    # path = ''
    await add_user({"dupa": 'janek'})
    # return FileResponse(path=path)
    return ResponseModel(message="test")
