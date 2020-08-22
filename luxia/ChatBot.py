import discord
import luxia.CommandHandle
import luxia.db.DbConnection
import discord.ext.commands


def db_enter():
    try:
        db = luxia.db.DbConnection.db_control("localhost", "root", "{k1o2d3e4r.db}", "luxia_db")  # connect with db
        print("db connect succeed")
        return db
    except():
        print("db connect failed")
        return None


token = input("token:")
client = discord.Client()
controler = db_enter()

bot = discord.ext.commands.Bot
@client.event
async def on_ready():
    print("bot is ready to use")
    await client.change_presence(activity=discord.Game(name="luxi help\\럭시야 도움"))
    pass


# command
@client.event
async def on_message(message: discord.message):
    # delete space and prefix
    if message.author.bot:
        return

    # check command
    await luxia.CommandHandle.check_command(message.content, message, controler)


try:
   client.run(token)
except Exception:
    print("token is wrong")
