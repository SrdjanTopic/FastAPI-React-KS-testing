import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from routers.users import router as user_router
from security.auth import router as auth_router

load_dotenv('.env')

app = FastAPI()


# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# --------AUTHOR endpoints---------------
app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "hello world"}
