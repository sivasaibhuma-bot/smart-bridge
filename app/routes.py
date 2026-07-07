from fastapi import APIRouter
from pydantic import BaseModel

from app.gemini import ask_gemini

router = APIRouter()


class Prompt(BaseModel):
    question: str
    type: str


@router.post("/generate")
async def generate(data: Prompt):

    prompt = data.question

    if data.type == "explain":
        prompt = "Explain in detail:\n\n" + prompt

    elif data.type == "quiz":
        prompt = "Generate a quiz about:\n\n" + prompt

    elif data.type == "summary":
        prompt = "Summarize:\n\n" + prompt

    elif data.type == "roadmap":
        prompt = "Create a learning roadmap for:\n\n" + prompt

    answer = ask_gemini(prompt)

    return {"response": answer}