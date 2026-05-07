
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("MTQzNTMyNjk5MjAzMDQ5ODgxNg.GUXL2j.bf7JquuoG1eAG4yc9eZ_5rBSRJ4gd81VS3Jp3s")

BAD_WORDS = ["badword1", "badword2", "curse"]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    if member.guild.system_channel:
        await member.guild.system_channel.send(
            f"👋 Welcome to the server, {member.mention}!"
        )

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    for word in BAD_WORDS:
        if word.lower() in message.content.lower():
            await message.delete()
            await message.channel.send(
                f"⚠️ {message.author.mention}, that word is not allowed."
            )
            return

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(TOKEN)
```
