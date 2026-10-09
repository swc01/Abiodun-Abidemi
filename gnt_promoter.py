import time
import datetime
import requests

# 1. Configuration Setup
# For Telegram: You create a bot via BotFather to get a token and a chat ID for music groups
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "@YOUR_TARGET_MUSIC_COMMUNITY_OR_CHANNEL"

# 2. Your Official Campaign Marketing Assets
TRACK_LINK = "https://ffm.to"
YOUTUBE_HUB = "https://youtube.com"

MARKETING_MESSAGE = (
    "🚨 MC TQ - FIGURE IT OUT IS LIVE! 🧠🔥\n\n"
    "No matter the hurdles, independent artists always figure it out! "
    "Check out the heavy Afro-Hip Hop vibes right now via our official hubs.\n\n"
    f"🎵 Stream on All Platforms: {TRACK_LINK}\n"
    f"🎥 Watch on YouTube: {YOUTUBE_HUB}\n\n"
    "#McTQ #FigureItOut #AfroHipHop #NigerianRap #GNT #Simdef"
)

# 3. Core Automation Engine
def send_marketing_post():
    """Sends the marketing message to the configured community endpoint."""
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MARKETING_MESSAGE,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"[{datetime.datetime.now()}] Campaign successfully posted to community!")
        else:
            print(f"Failed to post. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 4. Chronological Scheduler Core (Peak Hour Trigger)
PEAK_HOUR = 18  # 18:00 represents 6:00 PM WAT, a massive traffic peak in Nigeria

print("GNT Auto-Promoter Core initialized. Monitoring clock...")

while True:
    now = datetime.datetime.now()
    
    # Check if the current hour matches our target peak hour at minute 00
    if now.hour == PEAK_HOUR and now.minute == 0:
        send_marketing_post()
        # Sleep for 65 seconds to prevent multiple triggers in the same minute
        time.sleep(65)
        
    # Check the clock every 30 seconds to keep CPU cycles low
    time.sleep(30)
