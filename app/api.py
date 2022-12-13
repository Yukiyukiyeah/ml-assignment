from fastapi import APIRouter
from pydantic import BaseModel
from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer
from typing import List, Dict
import logging

router = APIRouter()

model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M', src_lang="en", tgt_lang="fr")
logging.info("finish loading model")

class Records(BaseModel):
  id: str
  text: str

class Payload(BaseModel):
  records: List[Records]
  fromLang: str = 'en'
  toLang: str = 'ja'

class Translation(BaseModel):
  payload: Payload

@router.post("/translation")
async def translation(translation: Translation):
    source_lang = translation.payload.fromLang
    target_lang = translation.payload.toLang
    records = translation.payload.records
    final_result = []
    for record in records:
      text = translate_helper(record.text, source_lang, target_lang)
      result = {"id": record.id, "text": text}
      final_result.append(result)
    return {"result": final_result}

def translate_helper(text, source_lang, target_lang):
    tokenizer.src_lang = source_lang
    model_inputs = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id(target_lang))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]
