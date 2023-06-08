import codecs

import yaml

file = codecs.open('./configs/config.yml', 'r', 'utf-8')
config = yaml.safe_load(file)

openai_token = config["openai-token"]
picovoice_token = config["picovoice-token"]
yandex_token = config["yandex-token"]
