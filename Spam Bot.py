import discord
import time
import datetime
Client = discord.Client()
@Client.event   
async def on_ready():
    print("Connected")
    streaming=discord.Streaming(name="Mass shootings", url="https://www.twich.tv")
    await Client.change_presence(activity=streaming)
@Client.event
async def on_message(message):
    x=0
    if message.author == Client.user:   
        return
    if message.content == "Jericho":
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""Screwing with 'people'""")
        await Client.change_presence(activity=game)
        while x < 50:
            await message.channel.send(#Your spam phrase#)
            x=x+1
        else:
            return
Client.run(#NzEwNTU3ODA4OTE1MTIwMTU5.Xr2Ncw.6Ay9vd_oOJXSWWAX_fOo_IFK_u8#)
