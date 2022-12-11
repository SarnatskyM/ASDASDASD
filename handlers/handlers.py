import re
from aiogram import types
from aiogram.types import message, reply_keyboard
from aiogram.dispatcher.filters import Text
from soupsieve import match
from config import *
from loader import dp, bot
from requests import *
import pkg.hltv as hltv
import time
import datetime
from keyboards.top import TopKeyboard,Start

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
   await message.reply(f"Приветствую тебя! {message.from_user.full_name}", reply_markup=Start)

@dp.message_handler(Text(equals='Топ'))
async def send_allmatch(message: types.Message):
   await message.answer('Выберите необходимый вам топ', reply_markup=TopKeyboard)

@dp.message_handler(Text(equals='Назад'))
async def send_allmatch(message: types.Message):
   await message.answer("Вернулись назад",reply_markup=Start)


@dp.message_handler(Text(equals='Топ 5'))
async def send_allmatch(message: types.Message):
   five = hltv.top5teams()
   output ='Топ 5 команд HLTV\n'
   for place,team in enumerate(five):
      output+=f'{place+1} - {team}\n'
   await message.reply(output,reply=False)


@dp.message_handler(Text(equals='Топ игроки'))
async def send_allmatch(message: types.Message):
   players = hltv.top_players()
   for i, ply in enumerate(players):
      await message.reply(f"#{i+1} {ply['nickname']} - {ply['name']}\nRating - {ply['rating']}\nGames - {ply['maps-played']}", reply=False)


@dp.message_handler(commands='matches')
async def send_allmatch(message: types.Message):
   matchs = hltv.get_matches()
   for i,match in enumerate(matchs):
      if i %10 == 0:
         time.sleep(10)
      await message.reply(f"{match['event']}\n{match['team1']} VS {match['team2']}\nНачало в {match['time']} - {match['date']}", reply=False)



@dp.message_handler(Text(equals='Результаты дня'))
async def send_res(message: types.Message):
   today_iso = datetime.datetime.today().isoformat().split('T')[0]
   res = hltv.get_results_by_date(today_iso, today_iso)
   for i, q in enumerate(res):
      await message.reply(f'Матч №{i+1} - {q["map"]}\n{q["team1"]} - {q["team2"]}\nСчет {q["team1score"]} - {q["team2score"]}', reply=False)
      if i - 10 == 0:
         time.sleep(5)