from pyrogram import Client, filters

OWNER_ID = 5294965763
API_HASH = "ca5085c3f41b16df46dbeebed6e56081"
APP_ID = 28160559
BOT_TOKEN = "6308227197:AAHweeHPdwsa9SDWpr7g627qxpqtbZsaWsU"

# Initialize the bot with your API credentials
app = Client(
    "my_bot",
    api_id=APP_ID,           # Replace with your own API ID
    api_hash=API_HASH, # Replace with your own API Hash
    bot_token=BOT_TOKEN # Replace with your bot token
)

# Define a simple command handler
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! I am your Pyrogram bot. How can I assist you today?")

# Run the bot
app.run()
