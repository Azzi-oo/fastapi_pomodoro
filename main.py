from fastapi import FastAPI
from handlers import router as routers


app = FastAPI()

for r in routers:
    app.include_router(r)