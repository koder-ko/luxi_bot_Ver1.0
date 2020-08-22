import discord
import luxia.db.DbConnection
import datetime
import luxia.LanguageGet
from luxia.EmbedSet import error_msg, help_msg
from luxia.CommandSet import join, search, search_add


async def check_command(cmd: str, message: discord.message, control: luxia.db.DbConnection.db_control):
    global prefix, embed

    # get prefix
    try:
        prefix = cmd.split()
        prefix = prefix[0]
    except IndexError:
        return

    # get lang file to dict
    language = luxia.LanguageGet.language_detect(luxia.LanguageGet.get_lang_file(), prefix)

    # language not detected
    if language is None:
        return
    # is member check
    is_member_bool = control.is_member(message.author.id)

    cmd = remove_pre(cmd, prefix)

    if is_member_bool:
        control.user_update(name=message.author.name + "#" + message.author.discriminator, id=message.author.id)

    if cmd == language["help_title"]:

        # set help embed
        embed = help_msg(language)

    elif cmd == language["license_title"]:

        # set license embed
        embed = error_msg(language["error_command_incomplete"], language)

    elif cmd == language["join_title"]:

        # set join embed
        embed = join(message, control, is_member_bool, language)

    elif not is_member_bool:

        # set error embed
        embed = error_msg(language["error_command_not_joined"], language)
    elif cmd.startswith(language["search_title"] + language["search_add_title"]):

        embed = search_add(remove_pre(cmd, language["search_title"] + language["search_add_title"]), language, message, control)

    elif cmd.startswith(language["search_title"]):

        # set search embed
        embed = search(control, language, remove_pre(cmd, language["search_title"]))
    else:

        # send not find command embed
        embed = error_msg(language["error_command_not_found"].format(cmd), language)

    embed.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()

    await message.channel.send(embed=embed)


def remove_pre(__cmd: str, __prefix: str):
    return __cmd[len(__prefix) + 1:]
