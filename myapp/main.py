import requests 
from fastapi import FastAPI,Form,Request
from fastapi.responses import PlainTextResponse
from .db import AsyncSessionLocal
from .models import Person,select
import re
import os
from dotenv import load_dotenv
from .fsmmap import fsmblock

app=FastAPI()
load_dotenv()

access_token=os.getenv("access_token")
phone_no_id=os.getenv("phno")


async def send_msg(to:str ,msg:str)->dict:
    url = f"https://graph.facebook.com/v22.0/{phone_no_id}/messages"
    headers={
        "Authorization":f"Bearer {access_token}",
        "Content-Type":"application/json"
    }

    payload={
        "messaging_product":"whatsapp",
        "to":to,
        "type":"text",
        "text": {"body":msg}
    }


    response = requests.post(url,headers=headers,json=payload)


    if response.status_code==200:
        return{"status":"success","message_id":response.json()["messages"][0]["id"]}
    
    else:
        return{"status":"error","detail":response.text}


VERIFY_TOKEN = "12345"

@app.get("/webhook", response_class=PlainTextResponse)
def verify(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge
    return "Verification failed", 403



@app.post("/webhook")
async def get_msg(request : Request):
    try:
        data= await request.json()
        entry=data.get("entry",[])[0]
        change=entry.get("changes",[])[0]
        value=change.get("value",{})

        messages=value.get("messages")
        if not messages:
            return PlainTextResponse("No messages in payload", status_code=200)
        message = messages[0]
        sender = message.get("from")
        msg = message.get("text", {}).get("body", "")
        
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(Person).where(Person.ph_no==sender).with_for_update())
            pep=result.scalar()

            if not pep:
                pep=Person(ph_no=sender,step="start")
                session.add(pep)
                await session.flush()

            handler=fsmblock.get(pep.step)
            print(pep.step,handler)
            if handler:
                await handler(send_msg,msg,pep,sender,session)
            else:
                await send_msg(sender,"ohhh , invalid entry")

            await session.commit()


        return PlainTextResponse("Message received", status_code=200)
    except Exception as e:
        return PlainTextResponse(f"Error: {str(e)}", status_code=500)

