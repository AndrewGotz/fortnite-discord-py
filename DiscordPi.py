import discord
import FortniteAPI
import json

TOKEN = 'fakeToken'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!god'):
        msg = '{0.author.mention} is a god at fortnite'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!fStats'):
        apiCall = message.content.split(':')
        msg = str(apiCall[1]) + 's ' + ' win total on ' + str(apiCall[2]) + ' is ' + FortniteAPI.totalWins(str(apiCall[1]), str(apiCall[2])).format(message)
        await client.send_message(message.channel, msg)

# async def fortnite_stats(player):

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)