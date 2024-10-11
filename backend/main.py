from fastapi import FastAPI, staticfiles
from backend.database import models
from backend.database.database import engine
from backend.routers import post
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(post.router)


models.Base.metadata.create_all(engine)


app.mount("/images", staticfiles.StaticFiles(directory="images"), name="images")

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
