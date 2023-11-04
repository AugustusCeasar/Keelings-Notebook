import os
import discord
import atexit

import pytz

from config import help_message, bot_state_json_path, owner_user_id
from resources.bot_state import BotState
from resources.find_the_truth import add_everyone_to_thread
from resources.quality_time import parse_time_message
# from resources.net_interface import get_online_team_members


bot_state = BotState(user_timezone_dict={}, connected_channels=[])


def save_bot_state():
    if os.path.exists(bot_state_json_path+".bak"):
        os.remove(bot_state_json_path+".bak")
    if os.path.exists(bot_state_json_path):
        os.rename(bot_state_json_path, bot_state_json_path+".bak")
    bot_state.save_to_json(bot_state_json_path)


def main():  # this might be the rare situation tha twe run this all on import and not just main?
    intents = discord.Intents.all()
    bot = discord.Bot(intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        if os.path.exists(bot_state_json_path):
            global bot_state
            bot_state = BotState.load_from_json_path(bot_state_json_path)
        atexit.register(save_bot_state)

    @bot.event
    async def on_message(message):
        if message.author.id != bot.application_id:
            print(message)
            possible_time = parse_time_message(message.content, message.author.id, bot_state)
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

    @bot.command(description="Set yourself up to have automatic timezone handling")
    async def set_up_timezone(context, timezone: str):
        if timezone in pytz.all_timezones:
            bot_state.user_timezone_dict[int(context.author.id)] = timezone
            await context.respond(f"Your personal timezone has been set to {timezone}!", ephemeral=True)
        else:
            await context.respond(f"{timezone} is not a valid timezone, "
                                  f"see https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568 "
                                  f"for correct formatting", ephemeral=True)

    @bot.command(description='Owner only')  # magic discord bs for fixing slash commands becoming invisible
    async def sync(ctx):
        print("sync command")
        if ctx.author.id == owner_user_id:
            await bot.tree.sync()
            await ctx.send('Command tree synced.')
        else:
            await ctx.send('You must be the owner to use this command!')

    bot.run(os.getenv("KEELING_BOT_TOKEN"))


if __name__ == '__main__':
    main()
