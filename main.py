from fastapi import FastAPI, Request
from whatsapp import send_message
from conversation import handle_message

app = FastAPI()


VERIFY_TOKEN = "mi_token_verificacion"


@app.get("/webhook")
async def verify(mode: str=None, challenge: str=None, verify_token: str=None):

    if verify_token == VERIFY_TOKEN:
        return int(challenge)

    return "error"


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    try:

        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        text = message["text"]["body"]

        sender = message["from"]

        response = handle_message(sender, text)

        send_message(sender, response)

    except:
        pass

    return {"status":"ok"}