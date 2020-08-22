import yaml
import glob

files = glob.glob("lang/*.yml")


def get_lang_file():
    lang_list = []
    for file in files:
        lang_list.append(get_lang_yaml(file))
    return lang_list


def get_lang_yaml(path: str):
    # open lang/lang.yml
    with open(path, encoding="utf-8") as file:
        members = yaml.load(file, Loader=yaml.FullLoader)
    return members


def language_detect(lang_list: list, prefix: str):
    for i in range(len(lang_list)):
        if prefix == lang_list[i]["command_prefix"]:
            return lang_list[i]
