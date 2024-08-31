import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Define the !ltc command
@bot.command(name='ltc')
async def ltc(ctx):
    # Send the LTC wallet address
    await ctx.send('Here is my LTC wallet address: `ltc1q2xlad5d58y7hu5ffvtlcqsky3tnj6qpjswh9cf`')

# Run the bot with the token
bot.run(TOKEN)
