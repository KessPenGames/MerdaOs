import yaml
import os
import codecs

DUMP_STR = """
openai-token: 'paste_your_token'
picovoice-token: 'paste_your_token'
yandex-token: 'paste_your_token'
"""


def createIfNotExist():
    if not os.path.exists("./configs/config.yml"):
        with codecs.open('./configs/config.yml', 'w', 'utf-8') as file:
            config_dump = yaml.safe_load(DUMP_STR)
            yaml.dump(config_dump, file)
