from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
qa_pipeline = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")

def get_answer(question, context):
    inputs = tokenizer(question, context, return_tensors="pt")
    with torch.no_grad():
        outputs = qa_pipeline(**inputs)
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits)
    print(question)
    print(context)
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end+1]))
    return answer
