from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class SourceL(Enum):
	english = 'English'
	german = 'German'
	romanian = 'Romanian'
	french = 'French'



class TranslateItem(BaseModel):
	destination_language: str
	source_language: SourceL
	input_text: str

	class Config():
		orm_mode = True
		use_enum_values = True

