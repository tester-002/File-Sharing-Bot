import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def coderzarena() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "🄲🄾🄳🄴🅁🅉 ΛЯΣПΛ",
            api_id=int(os.environ.get("APP_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: "),
            device_model="coderzarena Veresion 3"
    ) as coderzarena:
        print("\n <i> processing...</i>")
        coderzarena.storage.SESSION_STRING_FORMAT=">B?256sQ?"
        await coderzarena.send_message(
            "me", f"<b>@coderzarena User Session</b>\n\n<code>{await coderzarena.export_session_string()}</code>\n\n<i>Keep this Safe and Not share anyone</i>")
        print("Done!, Check your Saved Message for String Session!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(coderzarena())
