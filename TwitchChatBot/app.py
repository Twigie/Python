import constants
import asyncio
import websockets
from CommandHandler import CommandHandler

uri = 'ws://irc-ws.chat.twitch.tv:80'

cmdHandler = CommandHandler()

async def msg(websocket, msg):
  print('SENT: ', msg)
  await websocket.send('PRIVMSG ' + constants.CHANNEL_NAME +  ' :' + msg)

async def connection():
  uri = 'ws://irc-ws.chat.twitch.tv:80'
  async with websockets.connect(uri) as websocket:
    await websocket.send('PASS ' + constants.OAUTH_TOKEN + '\n')
    await websocket.send('NICK ' + constants.BOT_USERNAME + '\n')
    await websocket.send('JOIN ' + constants.CHANNEL_NAME + '\n')
    await websocket.send('PRIVMSG ' + constants.CHANNEL_NAME +  ' :Bot has joined the Chat')

    while True:
      r = await websocket.recv()
      if 'PRIVMSG' in r:
        await msg(websocket, cmdHandler.run(r.lower()))
      elif 'PING' in r:
        print(r)
        await websocket.send('PONG :tmi.twitch.tv')
      else:
        print(r)


asyncio.get_event_loop().run_until_complete(connection())
