from fastapi import APIRouter
from api.database.database import add_image, list_images
from api.models.responseModels import ResponseModel
from pkg.get_images import get_images

router = APIRouter(
    prefix="/images",
    tags=["images"],
)


@router.get("/downloadtoserver", response_description="Get images from subreddit to server")
async def downloadtoserver(subreddit: str = 'memes', image_limit: int = 10, order: str = "hot"):
    imagePaths = get_images(subreddit=subreddit,
                            image_limit=image_limit, order=order)

    # TODO optimize (maybe asyncio gather)
    for image in imagePaths:
        print(await add_image(image))

    print(await list_images())

    # TODO add error handling
    return ResponseModel(message=f"downloaded {image_limit} images to server from {subreddit}")


@router.get("/{image_idx}", response_description="Get images from subreddit")
async def image_idx(image_idx: int, subreddit: str = 'memes'):
    # TODO get path from db for the correct image
    x = await add_image()
    print(x)
    # return FileResponse(path=path)
    return ResponseModel(message="test")
