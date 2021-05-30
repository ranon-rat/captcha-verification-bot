from  discord.ext.commands import Bot,CommandNotFound
from discord.ext.commands.context import Context
from app.managecommands import get_captcha, receive_captcha
from json import load

bot:Bot = Bot(command_prefix="$",)
with open("settings.json", "r") as config:
    token = load(config)["token"]

@bot.command(name="getCaptcha")
async def output(ctx):

    if len(ctx.author.roles):
        await ctx.send("mal parido , ya tienes un role")
        return
    
    await get_captcha(ctx)


@bot.command(name="verify")
async def output(ctx:Context, arg=None):

    
    if len(ctx.author.roles):
        await ctx.send("mal parido , ya tienes un role")
        return
    if not arg:
        await ctx.send("mal parido te falto un argumento")
        return

    await receive_captcha(ctx, arg)


@bot.event
async def on_command_error(_:Context, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
bot.run(token)
