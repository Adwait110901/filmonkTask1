from fastapi import FastAPI ,Body
from fastapi.encoders import jsonable_encoder 
from models import UserSchema 
from database import add_user , get_Users 


app = FastAPI()

@app.get("/")
async def landing_page():
    return {"data":"welcome"}


@app.post("/postDetails")
async def postDetails(user : UserSchema = Body(...)):
    
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    
    return new_user

@app.get("/getDetails")
async def getDetails():
    users = await get_Users()
    if users:
        return {"data": users}
    return {"data":"no user in the db"}


# if __name__ == "__main__":
#     uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)    
