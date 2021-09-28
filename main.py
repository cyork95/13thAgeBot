import os
import discord
import random as random
from commands.apis import inspire
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
starter_encouragements = [
  "Cheer Up!", 
  "Hang in there.", 
  "You are a great person! (or bot)"
  ]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('hello') or message.content.startswith('hi'):
    await message.channel.send('Hello!')

  if msg.startswith('-inspire'):
    quote = inspire.get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    options = starter_encouragements
    if "encourgements" in db.keys():
      options = options + db['encourgements']
    await message.channel.send(random.choice(options))

  if msg.startswith("-new_encourage"):
    encouraging_message = msg.split("-new_encourage ",1)[1]
    inspire.update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added!")

  if msg.startswith("-del_encourage"):
    if "encouragements" in db.keys():
      index = int(msg.split("-del_encourage ",1)[1])
      inspire.delete_encouragements(index)
    await message.channel.send("Encouraging message deleted!")

  if msg.startswith("-lst_encourage"):
    encouragments = []
    if "encouragements" in db.keys():
      encouragments = db["enncouragments"]
    await message.channel.send(encouragments)

client.run(os.environ['TOKEN'])