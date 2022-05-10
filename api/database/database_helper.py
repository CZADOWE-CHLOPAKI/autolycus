def user_helper(user) -> dict:
    return {
        "id": str(user['_id']),
        "firstname": user['firstname'],
        "lastname": user['lastname'],
        "email": user['email'],
        "coordinates": user["coordinates"]
    }
