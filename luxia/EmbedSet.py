import discord


# embed return function
def embed_getter(title: str, description: str, thumbnail: str, name_field: list = [], value_field: list = []):
    if name_field is None:
        name_field = []
    embed_send = discord.Embed(title=title, description=description)
    try:
        for i in range(len(name_field)):
            embed_send.add_field(name=name_field[i], value=value_field[i], inline=False)
    except IndexError:
        print("name_field and value_field length are not matching")
    embed_send.set_thumbnail(url=thumbnail)
    return embed_send


# help msg setting
def help_msg(lang: dict):
    return embed_getter(title=lang["help_title"],
                        description=lang["help_description"],
                        thumbnail="https://i.ibb.co/HP40wmz/lluxi-help.png",
                        name_field=[lang["help_field_join_name"], lang["help_field_license_name"],
                                    lang["help_field_search_name"], lang["help_field_search_add_name"]],
                        value_field=[lang["help_field_join_description"], lang["help_field_license_description"],
                                     lang["help_field_search_description"], lang["help_field_search_add_description"]])


# error msg setting
def error_msg(error_msg: str, lang: dict):
    return embed_getter(title=lang["error_title"],
                        description=lang["error_description"].format(error_msg),
                        thumbnail="https://i.ibb.co/fGyT3gJ/lluxi-error.png")


# stay join msg
def stay_join_msg(lang: dict):
    return embed_getter(title=lang["join_stay_title"],
                        description=lang["join_stay_description"],
                        thumbnail="https://i.ibb.co/kxrzXZx/lluxi-join.png",
                        name_field=[lang["join_stay_field_license_name"], lang["join_stay_field_stay_save_name"]],
                        value_field=[lang["join_stay_field_license_value"], lang["join_stay_field_stay_save_value"]])


# join msg
def join_msg(lang: dict):
    return embed_getter(title=lang["join_title"],
                        description=lang["join_description"],
                        thumbnail="https://i.ibb.co/kxrzXZx/lluxi-join.png",
                        name_field=[lang["join_field_service"]],
                        value_field=[lang["join_field_service_value"]])


# search msg
def search_msg(lang: dict):
    return embed_getter(title=lang["search_title"],
                        description=lang["search_description"],
                        thumbnail="https://i.ibb.co/C5KP3wj/lluxi-search.png")


def search_not_found_msg(lang: dict, search_val: str):
    return embed_getter(title=lang["search_title"],
                        description=lang["search_description"],
                        thumbnail="https://i.ibb.co/C5KP3wj/lluxi-search.png",
                        name_field=[lang["search_field_not_found_name"]],
                        value_field=[lang["search_field_not_found_value"].format(search_val)])


# search add msg
def search_add_msg(lang: dict, key: str, val: str):
    return embed_getter(title=lang["search_title"] + " " + lang["search_add_title"],
                        description=lang["search_add_description"],
                        thumbnail="https://i.ibb.co/C5KP3wj/lluxi-search.png",
                        name_field=[lang["search_add_field_name"].format(key, val)],
                        value_field=[lang["search_add_field_value"]])
