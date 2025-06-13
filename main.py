import asyncio
from os import getenv

from mistralai import Mistral
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = getenv("TOKEN")
api_key = getenv("MISTRAL_API_KEY")

model = "mistral-large-latest"

client = Mistral(api_key=api_key)

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Я AI бот, который работает 24/7.")


@dp.message(lambda msg: msg.text)
async def mistral_ai(message: Message) -> None:
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": message.text,
            },
        ]
    )
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
