#https://github.com/ONETAPL3G3ND

import discord
from discord import utils
from discord.ext import commands
import config
import random
from discord.voice_client import VoiceClient
from discord.utils import get
import time
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import asyncio
client = discord.Client()


class MyClient(discord.Client):
# Проверка готовности бота
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))




bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
@bot.command()
async def creatlobby(ctx, channel : discord.VoiceChannel):
    #member = ctx.author
    #await member.move_to(channel)
    #await ctx.send(f"lobby created lobby number: {channel}")
    if ctx.author.voice.channel == "WAIT":
        member = ctx.author
        await member.move_to(channel)
        await ctx.send(f"lobby created lobby number: {channel}")
    elif ctx.author.voice.channel != "WAIT":
        if ctx.author.voice.channel == 'WAIT':
            member = ctx.author
            await member.move_to(channel)
            await ctx.send(f"lobby created lobby number: {channel}")
        else:
            chanle = ctx.author.voice.channel
            chanle = str(chanle)
            if chanle == "WAIT":
                member = ctx.author
                await member.move_to(channel)
                await ctx.send(f"lobby created lobby number: {channel}")
            else:
                print(ctx.author.voice.channel)
                await ctx.send(f"[ERROR] you must be in voice chat (WAIT)")
                member = ctx.author
                print(member)
    else:
        await ctx.send(f"[error]")

@bot.command()
async def connectplayertolobby(ctx, member : discord.Member):
    print(member)
    if ctx.author.voice.channel == "WAIT":
        await ctx.send(f"cannot be invited to the waiting room")
    else:
        channel = ctx.author.voice.channel
        await member.move_to(channel)
        await ctx.send(f"connect player to lobby number: {channel}")

@bot.command()
@commands.has_permissions(administrator = True)
async def vote(ctx):
    emb = discord.Embed( title = 'Голосование', colour = discord.Color.blue())
    emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    message = input("предложение: ")
    emb.add_field( name = "Предложение", value = message)
    message = input("выгода: ")
    emb.add_field( name = "Выгода", value = message)
    message = input("потери:  ")
    emb.add_field( name = "Потери: ", value = message)
    msg = await ctx.send(embed = emb)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')#добавляем реакции для голосования
    await asyncio.sleep(10)

    msg = await msg.channel.fetch_message(msg.id)

    for reaction in msg.reactions:
        print(reaction, reaction.count)#Этот код мне дали в ответах и он ничего не выводит
    if msg.reactions[0].count > msg.reactions[1].count:
        embed = discord.Embed(title =f"Голосование окончено!", description ='Удачно ✅', colour = discord.Colour.from_rgb(0, 204, 102))
        await ctx.send(embed=embed)#тут нужно сделать подсчёт количество нажатых реакций на каждой реакции. Далее сравниваем и выводим победителя
    elif msg.reactions[0].count == msg.reactions[1].count:
        embed = discord.Embed(title =f"Голосование окончено!", description ='(ничья) Неудачно ❌', colour = discord.Colour.red())
        await ctx.send(embed=embed)#тут нужно сделать подсчёт количество нажатых реакций на каждой реакции. Далее сравниваем и выводим победителя
    else:
        embed = discord.Embed(title =f"Голосование окончено!", description ='Неудачно ❌', colour = discord.Colour.red())
        await ctx.send(embed=embed)#тут нужно сделать подсчёт количество нажатых реакций на каждой реакции. Далее сравниваем и выводим победителя



@bot.command()
async def leave(ctx):
    member = ctx.author
    print(member)
    await ctx.send(f"you successfully exited")
    channel = client.get_channel(947112816769380403)
    await member.move_to(channel)

@bot.command()
async def reconectlobby(ctx):
    try:
        if ctx.author.voice.channel != '':
            member = ctx.author
            print(member)
            cha = ctx.author.voice.channel
            await ctx.send(f"go to voice chat WAIT, you have 10 second")
            channel = client.get_channel(947112816769380403)
            await member.move_to(channel)
            time.sleep(10)
            await member.move_to(cha)
        else:
            await ctx.send(f"to use this command you need to be in the lobby")
    except Exception as e:
        await ctx.send(f"to use this command you need to be in the lobby")
@bot.command()
async def mylobby(ctx):
    channel = ctx.author.voice.channel
    if channel is None:
        await ctx.send(f"you are not in the lobby")
    else:
        await ctx.send(f"your lobby number: {channel}")

@bot.command()
async def kicklobby(ctx, member : discord.Member):
    au = ctx.author.voice.channel
    mv = ctx.member.voice.channel
    channel = client.get_channel(947112816769380403)
    if au == mv:
        if au != 'WAIT':
            await member.move_to(channel)
            await ctx.send(f"you successfully kicked")
        else:
            await ctx.send(f"you can't kick someone from voice chat (WAIT)")
    else:
        await ctx.send(f"you are not in the same lobby")




@bot.command()
async def mtm(ctx):
    member = 'ONETAP_L3G3ND#7597'
    channel = 'WAIT'
    member = str(member)
    channel = str(channel)
    print(member)
    print(channel)
    await member.move_to(ctx.author.voice.channel)


bot.run(config.TOKEN)
