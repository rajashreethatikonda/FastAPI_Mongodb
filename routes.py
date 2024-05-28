from fastapi import APIRouter, HTTPException
from models import User
from bson import ObjectId
from config.db import conn

user_router = APIRouter()

@user_router.get("/")
async def get_all_users():
    try:
        users = [user for user in conn.local.users.find()]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving users")

@user_router.get("/{user_id}")
async def get_user(user_id: str):
    try:
        user = conn.local.users.find_one({"_id": ObjectId(user_id)})
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving user")

@user_router.post("/")
async def create_user(user: User):
    try:
        user_data = user.dict()
        user_id = conn.local.users.insert_one(user_data).inserted_id
        return {"user_id": str(user_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating user")

@user_router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    try:
        conn.local.users.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating user")

@user_router.delete("/{user_id}")
async def delete_user(user_id: str):
    try:
        result = conn.local.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 1:
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error deleting user")
