from fastapi import APIRouter, File, UploadFile

router = APIRouter()

docs = []

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    docs.append(content.decode('utf-8'))
    return {"filename": file.filename}
