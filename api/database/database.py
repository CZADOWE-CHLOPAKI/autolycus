import motor.motor_asyncio
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from ..config.config import MONGO_CONNECTION_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONNECTION_URL)
db = client.autolycus


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ImageModel(BaseModel):
    url: str = Field(...)
    image_path: str = Field(...)
    path: str = Field(...)


async def add_image(img: ImageModel):
    new_img = await db["images"].insert_one(jsonable_encoder(img))
    return new_img


async def list_images():
    imgs = await db["images"].find({}).to_list(1000)
    return imgs
#
# @app.get(
#     "/{id}", response_description="Get a single student", response_model=StudentModel
# )
# async def show_student(id: str):
#     if (student := await db["students"].find_one({"_id": id})) is not None:
#         return student
#
#     raise HTTPException(status_code=404, detail=f"Student {id} not found")
#
#
# @app.put("/{id}", response_description="Update a student", response_model=StudentModel)
# async def update_student(id: str, student: UpdateStudentModel = Body(...)):
#     student = {k: v for k, v in student.dict().items() if v is not None}
#
#     if len(student) >= 1:
#         update_result = await db["students"].update_one({"_id": id}, {"$set": student})
#
#         if update_result.modified_count == 1:
#             if (
#                 updated_student := await db["students"].find_one({"_id": id})
#             ) is not None:
#                 return updated_student
#
#     if (existing_student := await db["students"].find_one({"_id": id})) is not None:
#         return existing_student
#
#     raise HTTPException(status_code=404, detail=f"Student {id} not found")
#
#
# @app.delete("/{id}", response_description="Delete a student")
# async def delete_student(id: str):
#     delete_result = await db["students"].delete_one({"_id": id})
#
#     if delete_result.deleted_count == 1:
#         return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
#
#     raise HTTPException(status_code=404, detail=f"Student {id} not found")
