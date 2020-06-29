from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

from config import TOKEN
import buttons as btn

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)
days: int = 0


@dispatcher.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Just press 1️⃣ to count your days!\nType /help if need my help.", reply_markup=btn.markup)


@dispatcher.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Ahahahaaa... LOL!")


@dispatcher.message_handler(text='1️⃣')
async def button_plus_handler(msg: types.Message, counter=[0]):
    counter[0] += 1
    await msg.answer("Day: " + counter[0].__str__() + " of 14")
    if counter[0] == 13:
        await msg.answer("The next day is last for those lenses.")
    if counter[0] == 14:
        counter[0] = 0
        await msg.answer("Time to change your lenses!\nCounter has been reset!")


@dispatcher.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Please, use /start")


if __name__ == '__main__':
    executor.start_polling(dispatcher)
