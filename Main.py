import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask
import threading

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

# Create a simple Flask web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Discord bot's web server!"

@app.route('/ltc')
def ltc_address():
    return "LTC Wallet Address: ltc1q2xlad5d58y7hu5ffvtlcqsky3tnj6qpjswh9cf"

# Function to run the Flask app
def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# Start the Flask web server in a separate thread
web_server_thread = threading.Thread(target=run_web_server)
web_server_thread.start()

# Run the bot with the token
bot.run(TOKEN)
