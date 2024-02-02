from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
  return {"Hello":"Beautiful", "Nice":"To see you"}