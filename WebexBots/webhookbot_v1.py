from webexteamsbot import TeamsBot
import os
from file_read_backwards import FileReadBackwards
import re
import logging
import requests


# Setup logging, change '<REDACTED>' to "/path/to/your/webhookbot.log"
logging.basicConfig(filename='<REDACTED>', filemode='w', format='%(asctime)s - %(levelname)s - '
                                                                                      '%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


# Start Ngrok, change <REDACTED> to your bot's port number
logging.info("Starting ngrok (http) on port <REDACTED>, then sleeping for 5 sec...")
os.system("ngrok http <REDACTED> > /dev/null &")
os.system("sleep 5")


# Use FileReadBackwards to search most recent ngrok.log entries first
logging.info("Opening ngrok.log with FileReadBackwards...")
# Change <REDACTED> to "/path/to/your/ngrok.log"
with FileReadBackwards("<REDACTED>", encoding="utf-8") as frb:
    # getting lines by lines starting from the last line up
    for line in frb:
        try:
            new_url = str(line)
            # Look for the "url=blahblahblah" chunk of chars
            logging.info("Looking for most recent string url=...")
            url_chunk = re.findall(r"url=https://[A-Za-z0-9\-]+\.ngrok-free\.app", new_url)
            # Ignore blank result lines
            if str(url_chunk) != "[]":
                # Pull the actual url from "url=blahblahblah"
                url = re.findall(r"https://[A-Za-z0-9\-]+\.ngrok-free\.app", str(url_chunk))
                # Strip the brackets from url contents in simplest way possible
                ngrok_logged_url = url[0]
                logging.info("...Found ngrok.log url: " + ngrok_logged_url)
                # Immediately exit the loop, creating a "first match wins" loop
                break
        except:
            logging.critical("...FAILED to find ngrok.log url via regex.")
            quit()


# Bot Variables. Chage <REDACTED> to your variables
bot_email = "<REDACTED>"  # botname@webex.bot
teams_token = "<REDACTED>"  # the super long token you initially got from developer.webex.com for this bot
bot_url = ngrok_logged_url
bot_name = "<REDACTED>"  # the friendly botname
approved_users = ["<REDACTED>"]  # the email address of the webex user you use to interact with the bot


# Create a Bot Object.
#logging.info("Creating bot object...")
bot = TeamsBot(
        teams_bot_name=bot_name,
        teams_bot_token=teams_token,
        teams_bot_url=bot_url,
        teams_bot_email=bot_email,
        approved_users=approved_users,
)


# A simple command that returns a basic string that will be sent as a reply
logging.info("Declaring def do_something...")
def do_something(incoming_msg):
    return "i did what you said - {}".format(incoming_msg.text)


# Command handler for "/senddata", change <REDACTED> to your test API URL
logging.info("Declaring def send_data...")
def send_data(incoming_msg):
    # Strip somedata from incoming message "/send somedata"
    data = bot.extract_message("/send", incoming_msg.text).strip()
    # If data is present...
    if data:
        print("Data string found: " + data)
        reply = "Can send this: " + data
        headers = {"Content-Type": "application/json"}
        json = {"data": data}
        url = "<REDACTED>"
        # Send the POST to above URL
        response = requests.post(url=url, json=json, headers=headers)
        print(response.status_code)
        # If successful...
        if response.status_code == 200:
            reply = "200 OK"
            return reply
        # If NOT successful...
        else:
            reply = str(response.status_code)
            return reply
        return reply
    # If data is NOT present...
    else:
        reply = "Please provide some data after /send"
        return reply
    # Return the appropriate reply, from the above options Success, Not Success, or No Data Present.
    return reply


# Add new commands to the box.
#logging.info("Adding new commands to the bot...")
bot.add_command("/dosomething", "Echo's back your text. \tUsage: '/dosomething <text>'", do_something)
bot.add_command("/send", "Sends command word to an API. \tUsage: '/send <command>'", send_data)

if __name__ == "__main__":

    # Run Bot, change <REDACTED> to your bot's port number
    #logging.info("Starting bot, host 0.0.0.0, port <REDACTED>...")
    bot.run(host="0.0.0.0", port=<REDACTED>)
