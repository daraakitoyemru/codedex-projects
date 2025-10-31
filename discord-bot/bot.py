import discord
import os
from dotenv import load_dotenv
import requests,json


def get_meme():
    res = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(res.text)
    return json_data['url']



# log into discord server
intents = discord.Intents.default() # assigned default settings
intents.message_content = True #allows bot to interact with messages

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))


# Allow our bot to read messages and respond to them
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$meme'):
        await message.channel.send(get_meme())


load_dotenv()
token = os.environ.get("DISCORD_KEY") # get the token from environment variable
client.run(token)