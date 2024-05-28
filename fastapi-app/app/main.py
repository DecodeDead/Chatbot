import os
from fastapi import FastAPI
import uvicorn
from app.routers import upload, chat


port = process.env.PORT || 4000
app = FastAPI()
app.include_router(upload.router)
app.include_router(chat.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port)

