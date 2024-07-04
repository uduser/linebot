import os
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage
from pydantic import BaseModel

line_bot_api = LineBotApi('nMNiuEQTihA4MwQ+jmOuuVEBzTlkaN1vy9wKNJ0HB1wwZwqmqS/eo8U5ULj0HuhyrPdiPIi2pBwZwn0kcR6Fj1na02k1MWyR3ZRFijOi+4iuBmdrLZPw/1JkjXj1tdZxamhkX/h7shKF+uZUNsfeVwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6025c873a456c88e7401e7ec4da89d23')

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback():
    return {"message": "Hello LINE!"}

@router.post("/line2")
async def callback():
    return {"message": "Hello LINE2!"}


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    # Judge condition
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id='6136', sticker_id='10551379')
    )
