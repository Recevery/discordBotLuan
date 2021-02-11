#!/usr/bin/env python3.9

import discord
import time

client = discord.Client()



@client.event
async def on_ready():
    print("{}: I'm ready my capitain!".format(client.user))

@client.event
async def on_message(message):
    print(message.content)
    if message.content == "-ping":
        await ping(message.channel)
        return
    elif message.content[0] == "-" and message.content[1] == "s" and message.content[2] == "a" and message.content[3] == "y":
        var = message.content.replace('"', '')
        var = var.split(' ')
        j = 0
        test = ''
        for i in var:
            if j != 0:
                test = test + ' ' + i
            j += 1
        await message.channel.send('{0}'.format(test))
        return

@client.event
async def ping(ctx):
    await ctx.send('Pong!Latency: {0}ms'.format(round(int(client.latency * 1000), 1)))


client.run("a toi de metre")