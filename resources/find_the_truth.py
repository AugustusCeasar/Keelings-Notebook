import asyncio

from discord import Thread

from config import find_the_truth_role_id, brewing_channel_id


async def add_everyone_to_thread(thread: Thread, theatrics=True, all_parents=False) -> None:
    if all_parents or thread.parent_id == brewing_channel_id:
        temp_message = await thread.send("New deck thread detected, summoning bioroids with detective directives.")

        if theatrics:
            await asyncio.sleep(1)
            temp_message = await temp_message.edit(content=temp_message.content + "\n....")
            await asyncio.sleep(1)

        temp_message = await temp_message.edit(
            content=temp_message.content + f"\nNet signal going out <@&{find_the_truth_role_id}>"
        )

        if theatrics:
            await asyncio.sleep(1)
            temp_message = await temp_message.edit(content=temp_message.content + "\n....")
            await asyncio.sleep(1)
            temp_message = await temp_message.edit(content=temp_message.content + "\n....")
            await asyncio.sleep(1)
            temp_message = await temp_message.edit(
                content=temp_message.content + "\nCall Finished. Terminating Process")
            await asyncio.sleep(1)
            temp_message = await temp_message.edit(content=temp_message.content + "\n....")
            await asyncio.sleep(1)

        await temp_message.delete()
