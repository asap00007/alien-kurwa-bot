import discord
import asyncio
import random
from discord.ext import commands
from datetime import datetime, timedelta
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

wiadomosci = [
    "Alien ty kurwo",
    "Alien ty jebany orku",
    "Alien co ty odjebałeś znowu",
    "Alien kurwa ogarnij się",
    "Alien, twoje IQ to typ None",
    "Alien, twój mózg to callback bez funkcji",
    "Alien, jesteś deprecated i nikt nie robi update'a",
    "Alien, nawet HTML cię nie zamyka",
    "Alien, twój kod to `pass` i `except: pass`",
    "Alien, zasługujesz na `while True: pass`"
]

@bot.event
async def on_ready():
    print(f'✅ Bot zalogowany jako {bot.user}')
    bot.loop.create_task(send_daily_message())

@bot.command()
async def alien(ctx):
    msg = random.choice(wiadomosci)
    await ctx.send(msg)

async def send_daily_message():
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.now()
        target = now.replace(hour=19, minute=0, second=0, microsecond=0)
        if now >= target:
            target += timedelta(days=1)
        wait_time = (target - now).total_seconds()
        print(f"🕖 Czekam {wait_time/60:.1f} minut do 19:00")
        await asyncio.sleep(wait_time)
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            msg = random.choice(wiadomosci)
            await channel.send(msg)
            print(f"🧨 Auto-wiadomość poszła: {msg}")
        await asyncio.sleep(86400)

bot.run(TOKEN)
