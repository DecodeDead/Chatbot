from fastapi import FastAPI
import uvicorn
from routers import upload, chat

app = FastAPI()

app.include_router(upload.router)
app.include_router(chat.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)