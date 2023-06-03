from webex_bot.models.command import Command
import logging

log = logging.getLogger(__name__)

class POST(Command):
    def __init__(self):
        super().__init__(
            command_keyword="POST",
            help_message="Send a POST to some endpoint",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # Message may include spaces. Strip whitespace:
        payload = message.strip()

        # Define our URL, with requested ZIP code & API Key
        url = "https://api.openweathermap.org/data/2.5/weather?"
        url += f"zip={payload}&units=imperial&appid={OPENWEATHER_KEY}"

        # Query weather
        response = requests.get(url)
        weather = response.json()

        # Pull out desired info
        city = weather['name']
        conditions = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']

        response_message = f"In {city}, it's currently {temperature}F with {conditions}. "
        response_message += f"Wind speed is {wind}mph. Humidity is {humidity}%"

        return response_message