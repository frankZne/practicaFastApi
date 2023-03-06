from fastapi import FastAPI


# swagger http://127.0.0.1:8000/docs

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)

app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}
# http://127.0.0.1:8000



@app.get("/")
async def url():
    return {"messagex": "Hello Worldx"}