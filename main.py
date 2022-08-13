from core.config import api_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware




description = """TextTranslationApp API for tet translations. 🚀
	## Root
	You can **read aboout the documentation of the application here.**.
	## API
	The api has only one post which is a post to get the texts tranlated.
	You will be able to:
	* **Translate text from English to 3 other languages.
	* **These languages are as follows:
		Romanian, French and German.
"""

app = FastAPI(title="TextTranslationApp",
    description=description,
    version="0.1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Jedidiah Madjanor",
        "url": "https://github.com/madjanorjedidiah",
        "email": "jmadjanor6@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


@app.get("/")
async def root():
    return RedirectResponse('/docs')


app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

