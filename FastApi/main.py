from fastapi import FastAPI


# swagger http://127.0.0.1:8000/docs

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
# http://127.0.0.1:8000



@app.get("/")
async def url():
    return {"messagex": "Hello Worldx"}