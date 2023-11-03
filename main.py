import os
import discord

from config import help_message
from resources.find_the_truth import add_everyone_to_thread
from resources.quality_time import parse_time_message
# from resources.net_interface import get_online_team_members


def main():  # this might be the rare situation tha twe run this all on import and not just main?
    intents = discord.Intents.all()
    bot = discord.Bot(intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    @bot.event
    async def on_message(message):
        if message.author.id != bot.application_id:
            print(message)
            possible_time = parse_time_message(message.content)
            if possible_time is not None:
                await message.reply(possible_time)
                print("found time")

    @bot.event
    async def on_thread_create(thread):
        print(f"{thread} has been created")
        await add_everyone_to_thread(thread)

    @bot.command(description="Get help for all bot uses")
    async def help(context):
        await context.respond(help_message)

    bot.run(os.getenv("KEELING_BOT_TOKEN"))


if __name__ == '__main__':
    main()
