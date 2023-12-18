from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from model import result

app = FastAPI()


class Sentence(BaseModel):
    sentence: str


@app.post("/predict")
async def root(sen: Sentence):
    prediction = result(sen.sentence)

    response = {
        'prediction': prediction.split('Answer:')[-1]
    }
    return response
