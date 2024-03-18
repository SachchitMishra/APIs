def userEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "latest_usage":item["latest_usage"],
        "prev_usage":item["prev_usage"]
    }
def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]