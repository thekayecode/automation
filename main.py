from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    body = await request.json()
    print("Received from Telegram:", body)
    return {"status": "ok"}
