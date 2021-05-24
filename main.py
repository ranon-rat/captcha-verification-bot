

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from app.managecommands import get_captcha, receive_captcha
from json import load

bot = commands.Bot(command_prefix="$",)
with open("settings.json", "r") as config:
    token = load(config)["token"]

@bot.command(name="getCaptcha")
async def output(ctx):
    await get_captcha(ctx)


@bot.command(name="verify")
async def output(ctx, arg=None):
    if len(ctx.author.roles):
        await ctx.send("mal parido , ya tienes un role")
        return
    if not arg:
        await ctx.send("mal parido te falto un argumento")
        return

    await receive_captcha(ctx, arg, bot)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
bot.run(token)
