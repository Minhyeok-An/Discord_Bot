#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('연라에몽!'): # 만약 $hello로 시작하는 채팅이 올라오면
        await message.channel.send('연라에몽 프로토타입 가동') # Hello!라고 보내기


client.run('ODU2MTk1ODkwODMzMjYwNTY1.YM9gjw.24BP2mHXhRf8afDqrgFiRJyuv48')