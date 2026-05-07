GNU nano 8.6                                                         bot.py
import discord
from discord.ext import commands

# === CONFIGURATION ===
TOKEN = "MTQzNTMyNjk5MjAzMDQ5ODgxNg.GUXL2j.bf7JquuoG1eAG4yc9eZ_5rBSRJ4gd81VS3Jp3s"  # replace with your bot token
BAD_WORDS = ["badword1", "badword2", "curse"]  # add your banned words

# === INTENTS ===
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# === ON READY ===
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# === GREET NEW MEMBERS ===
@bot.event
async def on_member_join(member):
    # Sends greeting message in the server's default channel
    if member.guild.system_channel:
        await member.guild.system_channel.send(f"👋 Welcome to the server, {member.mention}!")

# === MODERATE MESSAGES ===
@bot.event
async def on_message(message):
