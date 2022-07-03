import datetime
import config
import logging

from aiogram import Bot, Dispatcher, executor, types

#log level
logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    today = datetime.datetime.now()
    bday = datetime.datetime(2022, 7, 6)
    st = ''
    raznitsa = str(bday - today)
    if raznitsa.find('day')!=-1:
        day = raznitsa[:raznitsa.find(' ')]
    if day=='2':
        st = st+'2 дня'
    elif day =='1':
        st = st+'1 день'
    raznitsa = raznitsa[raznitsa.find(',')+2:]
    st = st+' ' + raznitsa[:raznitsa.find(':')] + ' часов'
    raznitsa=raznitsa[raznitsa.find(':')+1:]
    st = st + ' ' + raznitsa[:raznitsa.find(':')] + ' минут'
    raznitsa=raznitsa[raznitsa.find(':')+1:]
    st = st + ' ' + raznitsa[:raznitsa.find('.')] + ' секунд'
    await message.answer('До дня рождения принцески осталось ' + st)

# run long-polling
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=False)