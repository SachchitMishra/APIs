def userEntity(item)->dict:
    return{
        "id":str(item["_id"]),
        "num1":item["num1"],
        "num2":item["num2"],
        "sums":item["sums"]
    }
def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]

    