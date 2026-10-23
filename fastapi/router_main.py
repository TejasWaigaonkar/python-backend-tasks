from fastapi import FastAPI
from fastapi_new.students import router

app = FastAPI()
app.include_router(router)