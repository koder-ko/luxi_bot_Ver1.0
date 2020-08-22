import discord
import luxia.db.DbConnection
from luxia.EmbedSet import error_msg, join_msg, stay_join_msg, search_msg, search_not_found_msg, search_add_msg
import luxia.CommandHandle

staying_user = []


# join function
def join(message: discord.message, control: luxia.db.DbConnection.db_control, is_member: bool, lang: dict):
    if is_member:
        return error_msg(lang["error_command_already_joined"], lang)
    if staying_user.__contains__(message.author.id):
        staying_user.remove(message.author.id)
        control.add_user(message.author.id, message.author.name + "#" + message.author.discriminator)
        return join_msg(lang)
    else:
        staying_user.append(message.author.id)
        return stay_join_msg(lang)


def search(control: luxia.db.DbConnection.db_control, lang: dict, search_val: str):

    values: list = control.search_link_get(search_val)

    if values is None:
        if search_val == "":
            return search_not_found_msg(lang, " ")
        return search_not_found_msg(lang, search_val)

    embed_search = search_msg(lang)
    for i in range(len(values)):
        embed_search.add_field(name=lang["search_field_name"].format(i + 1, values[i]["search_key"]),
                               value=lang["search_field_value"].format(values[i]["search_val"]), inline=False)
    return embed_search


def search_add(add_val: str, lang: dict, message: discord.message, control: luxia.db.DbConnection.db_control):
    try:
        key, val = add_val.split("^")
        control.search_link_add(author=message.author.id, key=key, val=val)
        return search_add_msg(lang, key, val)
    except BaseException:
        return error_msg(lang["error_command_incorrect_usage"], lang)
