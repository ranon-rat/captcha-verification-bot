from discord import File
from discord.ext.commands.context import Context
from discord.utils import get
from threading import Thread
from queue import Queue
from .generatestuff import Generate
from .database import delete_data, insert_data, selecting_data


async def get_captcha(ctx: Context):
    captcha_output, image = Generate().generate_image()
    image.seek(0)
    file = File(image, filename="captcha.png")
    Thread(target=insert_data, args=(captcha_output, ctx.author.id,)).start()
    await ctx.send(file=file)


async def receive_captcha(ctx: Context, arg: str):

    id = Queue[str]()
    threadID = Thread(target=selecting_data, args=(
        arg.format(), ctx.author.id, id,))
    threadID.start()

    if id.get() is None:
        await ctx.send("jajaja que botsito , no puede contra un captcha")
        return
    guild = ctx.guild

    if get(ctx.author.guild.roles, name="captcha-verify") is None:
        await guild.create_role(name="captcha-verify", read_messages=True, read_message_history=True, connect=True, speak=True, send_messages=True)

    delete_data(id)
    role = get(guild.roles, name="captcha-verify")
    await ctx.author.add_roles(role)
    await ctx.send("bien , ya estas verificado")
