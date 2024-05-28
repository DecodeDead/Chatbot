from fastapi import APIRouter, File, UploadFile, HTTPException
from transformers import AutoTokenizer

router = APIRouter()

docs = []
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased") 

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode('utf-8')
    tokens = tokenizer.tokenize(text)
    if len(tokens) > 512:
        raise HTTPException(status_code=400,detail="Document exceeds the maximum token limit of 512.")
    docs.append(text)
    return {"filename": file.filename}
