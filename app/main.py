from fastapi import FastAPI
import api
import uvicorn

app = FastAPI()

app.include_router(api.router)

@app.get('/')
async def root():
  return {"result": "人生はチョコレートの箱のようなものだ。"}
  
# @app.post("/translation")
# def translation(text: str,source_language: str,  target_language: str):
#     return {"result": "人生はチョコレートの箱のようなものだ。"}

if __name__ == "__main__":
  uvicorn.run("main:app", port=8000, reload=True)