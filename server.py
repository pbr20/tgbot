from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bot is running!"}

@app.get("/ping")
def ping():
    return {"status": "OK"}

if name == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
