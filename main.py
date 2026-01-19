import os
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

SECRET = os.getenv("TV_SECRET", "CHANGE_ME")

@app.get("/")
def home():
    return {"status": "ok", "msg": "TV → Render webhook running ✅"}

@app.post("/tvwebhook")
async def tvwebhook(req: Request):
    data = await req.json()

    if data.get("secret") != SECRET:
        raise HTTPException(status_code=401, detail="Invalid secret")

    print("✅ TradingView webhook received:", data)

    return {"status": "received", "data": data}
