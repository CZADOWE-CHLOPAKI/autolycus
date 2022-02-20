import httpx as httpx
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from api.config.config import RANDOM_USER_SERVICE_URL
from api.database.database import retrieve_users, add_user, delete_user
from api.models.responseModels import ResponseModel, ErrorResponseModel, UserModel, Coordinates

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    return ResponseModel(users, "Users data retrieved successfully")


@router.delete("", response_description="User data deleted from the database")
async def delete_user_data(user_id: str):
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return ResponseModel(f"User with ID: {user_id} removed", "User deleted successfully")
    return ErrorResponseModel("An error occurred", 404, f"User with id {user_id} doesn't exist")


@router.post("/create-random", response_description="Create user")
async def create_user():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(RANDOM_USER_SERVICE_URL)
            if response.status_code != 200:
                return ErrorResponseModel("An error occurred", 404, f"Can't create user.")
            json = response.json()
            user_json_data = json['results'][0]

            latitude = float(user_json_data["location"]["coordinates"]["latitude"])
            longitude = float(user_json_data["location"]["coordinates"]["longitude"])

            # clamp coordinates to their limits
            latitude = max(-90.0, min(latitude, 90.0))
            longitude = max(-180.0, min(longitude, 80.0))

            user = UserModel(email=user_json_data["email"],
                             firstname=user_json_data["name"]["first"],
                             lastname=user_json_data["name"]["last"],
                             coordinates=Coordinates(
                                 lat=latitude,
                                 lng=longitude,
                             )
                             )

            new_user = await add_user(jsonable_encoder(user))
            return ResponseModel(new_user, "User added successfully.")
        except:
            return ErrorResponseModel("An error occurred", 404, f"Can't create user.")
