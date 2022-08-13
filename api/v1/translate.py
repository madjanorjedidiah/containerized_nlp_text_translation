from fastapi import APIRouter, HTTPException, status
from schemes.translate import TranslateItem
from transformers import T5Tokenizer, T5ForConditionalGeneration
import os


router = APIRouter()


class TranslateClass():


    def __init__(self, root_path=None, tokenizer=None, model=None):
        self.root_path = root_path
        self.tokenizer = tokenizer
        self.model = model


    def activate_token_model(self):
        self.root_path = os.path.abspath('')
        self.tokenizer = T5Tokenizer.from_pretrained(os.path.join(self.root_path, 't5-base'), local_files_only=True)
        self.model = T5ForConditionalGeneration.from_pretrained(os.path.join(self.root_path, 't5-base'), return_dict=True)
        return (self.tokenizer, self.model)


t5_base_instance = TranslateClass()
tokenizer, model = t5_base_instance.activate_token_model()


@router.post("/translate")
def translate_words(translate1: TranslateItem):
    try:
        word = perform_translation(translate1.source_language, translate1.destination_language, translate1.input_text)
    except Exception:
        raise HTTPException(status_code=404, detail='Language translation not yet available')
    return word


def perform_translation(source_language, destination_language, input_txt):
    input_ids = tokenizer(f"translate {source_language} to {destination_language}: " 
    + input_txt, return_tensors="pt").input_ids  # Batch size 1
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"translation": f"{decoded}", 'status': status.HTTP_200_OK}