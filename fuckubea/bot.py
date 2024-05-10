import asyncio
import TOKEN
import discord
from discord import *
import keyboard as kb
from typing import Any
import os

# --- UI ---
def clear_lines(amt: int):
    print("\033[F\033[K"*amt, end="")

def clear_all_lines():
    os.system('cls' if os.name=='nt' else 'clear')

def filtered_key():
    keys = []
    while len(keys) < 2:
        keys.append(kb.read_key())
    return keys[0]

def select_menu(options, return_index=False) -> Any:
    selected_index = 0
    last_index = len(options)-1
    
    while True:
        for i, v in enumerate(options):
            if i == selected_index:
                print('>', v)
            else:
                print(v)
        key = filtered_key()
        clear_lines(len(options))

        match key:
            case "up":
                if selected_index != 0:
                    selected_index -= 1
                else:
                    selected_index = last_index
            case "down":
                if selected_index != last_index: 
                    selected_index += 1
                else:
                    selected_index = 0
            case "enter":
                print("\033[K", end="")
                return options[selected_index] if not return_index else selected_index

# --- BOT ---
testguild=1238263344226369618
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
bot = Bot(command_prefix='&', intents = intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pornhub.com", state="Edging"),status=discord.Status.do_not_disturb)
    bot.application_commands.clear()

# --- PRE-PROCESS ---
def getChannelByName(chnlName):
    return discord.utils.get(client.get_all_channels(), name=chnlName)
# --- CMDS ---
@bot.slash_command(name="iamnotsupsipshus", guild=testguild)
async def iamnotsupsipshus(ctx):
    if ctx.author.id != 741087093958246420:
        await ctx.respond("I AM NOT SUPSIPSHUS!!")
    else:
        await ctx.respond("FUCK YOU BITCH U CANT CRASH ME :middle_finger:", ephemeral=True)

@bot.slash_command(name="moderate", guild=testguild)
async def mederate(ctx):
    await ctx.respond("MODERATION MODE ACTIVATING...", ephemeral=True)
    await ctx.respond("https://tenor.com/view/hacker-pc-meme-matrix-codes-gif-16730883", ephemeral=True)
    await asyncio.sleep(1)
    await ctx.respond("Please upgrade your bot subscription before continuing! Thank you!", ephemeral=True)


# --- NAV ---
def home_menu(): 
    clear_all_lines()
    print("What would you like to do?\n")
    if not select_menu(["Enter manual mode", "Exit the program"], return_index=True):
        manual_mode()
    else:
        quit()

def manual_mode():
    clear_all_lines()
    print("Manual mode panel:\n")


if __name__ == "__main__":
    home_menu()
    bot.run(TOKEN.TOKEN)