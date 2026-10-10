
import time
import datetime
import requests

# 1. Configuration Setup
# Fully locked in with your custom token and Dynasty Records channel handle!
BOT_TOKEN = "8853517787:AAFcYkWFj6dT_EdbnEeilJ8QmYiZ8XZ3q9U"
CHAT_ID = "@mctq01"

# 2. Your Official Mc TQ Release Assets
FEATURE_FM_SMARTLINK = "https://ffm.to"
AUDIOMACK_FIGURE_IT_OUT = "https://audiomack.com"
AUDIOMACK_IDAN_ORI_TA = "https://audiomack.com"
YOUTUBE_HUB = "https://youtube.com"

MARKETING_MESSAGE = (
    "🚨 MC TQ - OFFICIAL MUSIC OUTREACH! 🧠🔥\n\n"
    "The independent grind never stops. Stream the catalog directly on all platforms without heavy email attachments:\n\n"
    f"👉 Main Smart Link (Spotify/Apple): {FEATURE_FM_SMARTLINK}\n"
    f"🎵 Listen to 'Figure it Out' on Audiomack: {AUDIOMACK_FIGURE_IT_OUT}\n"
    f"🔥 Listen to 'Idan Ori Ta' on Audiomack: {AUDIOMACK_IDAN_ORI_TA}\n"
    f"🎥 Official YouTube Visuals: {YOUTUBE_HUB}\n\n"
    "Pure quality, zero compromise. Tap to listen, support, and share! 🚀🌍\n\n"
    "#McTQ #FigureItOut #IdanOriTa #AfroHipHop #NigerianRap #GNT #Simdef"
)

# 3. Core Automation Engine
def send_marketing_post():
    """Sends the marketing campaign packet to the community endpoint."""
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
            print(f"Failed to post. Status Code: {response.status_code}. Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 4. Chronological Scheduler Core (Peak Hour Trigger)
PEAK_HOUR = 18  # 6:00 PM WAT (Peak evening traffic in Nigeria)

print("GNT Auto-Promoter Core initialized. Monitoring clock...")

while True:
    now = datetime.datetime.now()

    # Check if the current time strikes peak hour precisely
    if now.hour == PEAK_HOUR and now.minute == 0:
        send_marketing_post()
        time.sleep(65)  # Prevents multiple duplicate triggers within the same minute

    time.sleep(30)  # Sleep interval to keep server processing cycles minimal
