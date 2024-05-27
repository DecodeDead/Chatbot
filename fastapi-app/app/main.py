import os
from fastapi import FastAPI
import uvicorn
from app.routers import upload, chat


app = FastAPI()
app.include_router(upload.router)
app.include_router(chat.router)


if __name__ == '__main__':
    port = int(os.environ.get("PORT",10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

