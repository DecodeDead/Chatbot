from fastapi import APIRouter
from app.models import QuestionModel
from app.qa_model import get_answer
from app.utils import preprocess_text
from .upload import docs

router = APIRouter()

@router.post("/chat/")
async def chat(question_model: QuestionModel):
    user_query = question_model.question
    response = chatbot_response(user_query)
    return {"response": response}

def chatbot_response(user_query):
    try:
        preprocessed_query = preprocess_text(user_query)
        response = get_answer(preprocessed_query, docs[0])  # Use the first document for context
    except Exception as e:
        response = f"Error: {str(e)}"
    return response
