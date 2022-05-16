from fastapi import APIRouter

from api.database.database import add_image, list_images
from api.models.responseModels import ResponseModel

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


@router.get("/dupa", response_description="Get images from subreddit")
async def dupa1(image_idx: int, subreddit: str = 'memes'):
    # TODO get path from db for the correct image
    imgs = await list_images()
    print(imgs)
    # return FileResponse(path=path)
    return ResponseModel(message="test")


@router.get("/dupa/{n}", response_description="Get images from subreddit")
async def dupa2(n: int):
    # TODO get path from db for the correct image
    imgs = await list_images()
    print(imgs)
    # return FileResponse(path=path)
    return ResponseModel(message="test")


@router.get("/{image_idx}", response_description="Get images from subreddit")
async def image_idx(image_idx: int, subreddit: str = 'memes'):
    # TODO get path from db for the correct image
    x = await add_image()
    print(x)
    # return FileResponse(path=path)
    return ResponseModel(message="test")
